#include <stdio.h>
#include <stdlib.h>
#include <string.h>


class Park{
public:
    Park() {
        offsetTable = new unsigned int [1000+1];
        earnTable = new unsigned int [1000+1];
    };
    ~Park() {
        if (offsetTable) delete[] offsetTable;
        if (earnTable) delete[] earnTable;
    };

    void Clear() {
        memset(offsetTable, 0, sizeof(unsigned int)*1000);
        memset(earnTable, 0, sizeof(unsigned int)*1000);
    };
    void Load(unsigned int R, unsigned int K, unsigned int N, unsigned int* grpNum) {
        this-> R = R;
        this-> K = K;
        this-> N = N;
        this->grpNum = grpNum;

        int beg = 0; // inclusive
        int people = grpNum[beg];
        int end = 1 % N; // exclusive
        while (people + grpNum[end] <= K && beg != end) {
            people += grpNum[end];
            end++;
            if (end == N ) end = 0;
            if (end == beg) break;
        } 
        earnTable[beg] = people;
        offsetTable[beg] = end;

        for (int i = 1 ; i< N; i++) {
            beg = i;
            people -= grpNum[i-1];
            while (people + grpNum[ end ] <= K) {
                people += grpNum[end];
                end++;
                if (end == N ) end = 0;
                if (end == beg) break;
            } 
            earnTable[beg] = people;
            offsetTable[beg] = end;
        }
        // Debug();
    };
    unsigned int Total() {
        unsigned int total = 0;
        int pos = 0;
        for (int i = 0; i< R; i++) {
            total += earnTable[pos];
            pos = offsetTable[pos];
        }
        return total;
    };
    void Debug() {
        for (int i = 0; i < N; i++) {
            printf("%d ", offsetTable[i]);
        }
        printf("\n");
        for (int i = 0; i < N; i++) {
            printf("%d ", earnTable[i]);
        }
        printf("\n");
    };
    unsigned int R;
    unsigned int K;
    unsigned int N;
    unsigned int* grpNum;
    unsigned int * offsetTable;
    unsigned int * earnTable;

};
int main(int argc, char** argv) {
    int totalLine;
    FILE * fp = fopen(argv[1] , "r");
    fscanf(fp, "%d", &totalLine);
    unsigned int R; // times per day
    unsigned int K; // capacity
    unsigned int N; // # of group 
    unsigned int grpNum[1000];
    Park p;
    for (int i = 0; i < totalLine; i++) {
        fscanf(fp, "%d %d %d", &R, &K, &N);
        for (int j = 0; j < N ; j++) {
            fscanf(fp, "%d", &grpNum[j]);
        }

        p.Clear();
        p.Load(R, K, N, grpNum);
        printf("Case #%d: %d\n", i+1, p.Total());
    }
    return 0;
}

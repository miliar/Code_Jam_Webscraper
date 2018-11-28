#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

const int MaxN = 100;

typedef struct TTrainTime {
        int start, end;
        bool used;
        int uses;
};
typedef TTrainTime TIntArr[MaxN + 1];

// Function requered for algorithm.h function sort
bool cmpFunction(TTrainTime a, TTrainTime b) {
        return a.start < b.start;
}

void SetTrains(TIntArr &TrainsA, TIntArr &TrainsB, int NA, int NB,
               int &Train_in_A, int &Train_in_B) {
        Train_in_A = 0;
        Train_in_B = 0;
        int A = 1, B = 1; // Pointer to train time
        while((A <= NA)||(B <= NB)) {
                if (((B > NB)||(TrainsA[A].start <= TrainsB[B].start))&&(A <= NA)) {
                        for(int i = 1; i <= NB; i++)
                                if((!TrainsB[i].used)&&(TrainsB[i].start >= TrainsA[A].end)) {
                                        TrainsB[i].used = true;
                                        TrainsA[A].uses = i;
                                        break;
                                }
                        A++;
                } else if (B <= NB) {
                        for(int i = 1; i <= NA; i++)
                                if((!TrainsA[i].used)&&(TrainsA[i].start >= TrainsB[B].end)) {
                                        TrainsA[i].used = true;
                                        TrainsB[B].uses = i;
                                        break;
                                }
                        B++;
                }
        }
        for(int i = 1; i<= NA; i++)
                if (!TrainsA[i].used)
                        Train_in_A++;
        for(int i = 1; i <= NB; i++)
                if (!TrainsB[i].used)
                        Train_in_B++;    
}

int main () {
        int N, NA, NB, T;
        TIntArr TrainsA, TrainsB;
        ifstream fin("train.in");
        ofstream fout("train.out");
        fin >> N;
        for(int i = 1; i <= N; i++) {
                // Read initial data
                string reader;
                int tmp;char c;
                int Train_in_A, Train_in_B;
                fin >> T >> NA >> NB;
                for(int u = 1; u <= NA; u++) {
                        fin >> tmp;
                        TrainsA[u].start = tmp*100;
                        fin >> c;
                        fin >> tmp;
                        TrainsA[u].start += tmp;
                        fin >> tmp;
                        TrainsA[u].end = tmp*100;
                        fin >> c;
                        fin >> tmp;
                        TrainsA[u].end += tmp;                     
                        TrainsA[u].used = false;
                        TrainsA[u].uses = 0;
                        TrainsA[u].end += T;
                        if (TrainsA[u].end % 100 >= 60) {
                                TrainsA[u].end += 100;
                                TrainsA[u].end -= 60;
                        }
                }
                for(int u = 1; u <= NB; u++) {
                        fin >> tmp;
                        TrainsB[u].start = tmp*100;
                        fin >> c;
                        fin >> tmp;
                        TrainsB[u].start += tmp;
                        fin >> tmp;
                        TrainsB[u].end = tmp*100;
                        fin >> c;
                        fin >> tmp;
                        TrainsB[u].end += tmp;  
                        TrainsB[u].used = false;
                        TrainsB[u].uses = 0;    
                        TrainsB[u].end += T;
                        if (TrainsB[u].end % 100 >= 60) {
                                TrainsB[u].end += 100;
                                TrainsB[u].end -= 60;
                        }                  
                }
                sort(TrainsA+1, TrainsA+NA+1, cmpFunction);
                sort(TrainsB+1, TrainsB+NB+1, cmpFunction);
                SetTrains(TrainsA, TrainsB, NA, NB, Train_in_A, Train_in_B);
                fout << "Case #" << i << ": " << Train_in_A << " " << Train_in_B << endl;
        }
        fin.close();
        fout.close();
        return 0;
}

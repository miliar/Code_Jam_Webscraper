#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    int T;
    int N;
	freopen("A-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
    cin >> T;
	unsigned long long matrix[64];
    for(int cc=1;cc<=T;cc++) {
        cin >> N;

        string bitseq;
        

        for(int i=0;i<N;i++) {
            cin >> bitseq;

            matrix[i]=0;
            unsigned long long pos=1;
            for(int j=N-1; j>=0; j--, pos<<=1) {
                if(bitseq[j]=='1') matrix[i]|=pos;
            }
        }

        int count = 0;
        unsigned long long now=1;
        for(int i=0;i<N-2;i++) now = now | now<<1;

        for(int i=0;i<N;i++) {
            int candidate;
            for(candidate=i; candidate<N; candidate++) {
                if((now & matrix[candidate]) == 0) break;
            }

            if(candidate!=i) {
                while(candidate>i) {
                    swap(matrix[candidate], matrix[candidate-1]);
                    count++;
                    candidate--;
                }
            }

            now>>=1;
        }
		if ( N == 1 ) count = 0;
        printf("Case #%d: %d\n", cc, count);
    }

    return 0;
}
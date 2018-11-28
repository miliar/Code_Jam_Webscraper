#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <strstream>

using namespace std;

int A[40];
char line[41];

int process(int A[], int N)
{
    int ans = 0;
    int i,j;
    for (i=0; i<N; i++) {
        if (A[i] > i+1) {
            for (j=i+1; j<N; j++) {
                if (A[j] <= i+1) break;
            }
            int tmp = A[j];
            for (j--; j>=i; j--) {
                ans ++;
                A[j+1] = A[j];
            }
            A[i] = tmp;
        }
    }
    return ans;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int T,Ti;
    cin >> T;
    for (Ti=0; Ti<T; Ti++) {
        int N,Ni,i;
        cin >> N;
        for (Ni=0; Ni<N; Ni++) {
            A[Ni] = 0;
            cin >> line;
            for (i=0; i<N; i++) {
                if (line[i] == '1') A[Ni] = i+1;
            }
        }
        printf("Case #%d: %d\n", Ti+1, process(A,N) );
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;
#define MAX 10000000
#define PMAX 100000

bool prime[PMAX];
long i,j,n,m,k;
long T,A,B,P;
long SET[PMAX];
ifstream fin("in.in");
ofstream fout("out.out");

void mark(long x, long y) {
     long i;
     for (i=A;i<=B;i++) 
         if (SET[i] == SET[y]) SET[i] = SET[x];
     }

int main() {
    // Erastoten
    fill(prime,prime+PMAX,true);
    for (i=2;i<PMAX/2;i++)
        for (j=2*i;j<PMAX;j+=i)
            prime[j] = false;
            
    fin >> T;
    for (long t=1;t<=T;t++) {
        fout << "Case #" << t << ": ";
        fin >> A >> B >> P;
        long SOL(B-A+1);
        set<long> found;
        
        for (i=A;i<=B;i++) SET[i] = i;
        
        for (i=A;i<=B;i++)
            for (j=i+1;j<=B;j++) {
                if (SET[i] == SET[j]) continue;
                for (k=P;k<=max(A,B)/2;k++) {
                    if (!prime[k]) continue;
                    if (i%k==0 && j%k==0) { mark(i,j); SOL--; break; }
                    }
                }
        SOL = 0;
        for (i=A;i<=B;i++)
            if (!found.count(SET[i])) {
               found.insert(SET[i]);
               SOL++;
               }
        fout << SOL << endl;
        }
    system("pause");
}

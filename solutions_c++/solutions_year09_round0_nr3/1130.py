#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define NMAX 520
#define LMAX 30
#define MODUL 10000

string phrase="welcome to code jam";

int f[NMAX][LMAX];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int L=phrase.length(), nTest;
    
    scanf("%d\n", &nTest);
    
    for (int test=1; test<=nTest; ++test) {
        string s;
        getline(cin, s);
        int N=s.length();        

        
        memset(f,0,sizeof(f));
        for (int i=0; i<N; ++i)
            for (int j=0; j<L; ++j) {
                if (s[i]==phrase[j]) {
                if (j==0) f[i][j]=1; else
                for (int i2=0; i2<i; ++i2) {
                    f[i][j]=(f[i][j]+f[i2][j-1])%MODUL;
                }                            
                //cout << i << "  " << j << " " << f[i][j] << endl;
            }
            
        }
            
        int ret=0;
        for (int i=0; i<N; ++i)
            ret=(ret+f[i][L-1])%MODUL;
            
        printf("Case #%d: %04d\n", test, ret);
    }
    
    return 0;
}

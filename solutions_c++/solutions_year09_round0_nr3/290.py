#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

const string table="~welcome to code jam";

int n;
int f[500][20];
string st;

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d\n",&n);
    for (int t=1; t<=n; ++t){
        getline(cin,st);
        printf("Case #%d: ",t);
        memset(f,0,sizeof(f));
        f[0][0] = 1; if (st[0] == 'w') f[0][1] = 1;
        for (int i=1; i != st.size(); ++i)
            for (int j=0; j <=19; ++j){
                f[i][j] += f[i-1][j]; 
                if (st[i] == table[j])
                   f[i][j] += f[i-1][j-1];
                f[i][j] = f[i][j] % 10000;
            }
        if (f[st.size()-1][19] < 1000) printf("0");
        if (f[st.size()-1][19] < 100) printf("0");
        if (f[st.size()-1][19] < 10) printf("0");
        printf("%d\n",f[st.size()-1][19]);
    }
}

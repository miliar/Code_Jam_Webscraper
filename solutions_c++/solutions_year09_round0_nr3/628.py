#include <algorithm>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

string ss="welcome to code jam";
char s[10000];
int cont,tam;

int m[505][20];


int main(){
    int n,i,ii,j,tam2;
    //string s;
    scanf("%d\n",&n);
    for(int ii=0;ii<n;ii++){
        cont=0;
        gets(s);
        memset(m,0,sizeof(m));
        tam=strlen(s);
        tam2=ss.length();
        for(i=0;i<=tam;i++)
            m[i][0]=1;
        for(i=1;i<=tam2;i++){
            for(j=1;j<=tam;j++){
                if(s[j-1]==ss[i-1]) m[j][i]=(m[j-1][i]%10000+m[j][i-1]%10000)%10000;
                else    m[j][i]=m[j-1][i]%10000;
            }
        }
        printf("Case #%d: %04d\n",ii+1,m[tam][tam2]);
    }
    return 0;
}

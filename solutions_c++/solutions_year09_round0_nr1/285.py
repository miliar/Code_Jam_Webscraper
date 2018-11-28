#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

string word[5000],st;
int l,n,d;
bool ok[15][200];

bool match(int k){
     for (int i=0; i<l; ++i)
         if (! ok[i][word[k][i]]) return false;
     return true;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d %d %d\n",&l,&d,&n);
    for (int i=0; i<d; ++i)
        cin >> word[i];
    for (int t=1; t<=n; t++){
        printf("Case #%d: ",t);
        memset(ok,false,sizeof(ok));
        cin >> st;
        int i=0,j=0; 
        while (i != st.size()){
              if (st[i] == '('){
                 i++;
                 while (st[i] != ')'){
                       ok[j][st[i]] = true; i++;
                 }
              }
              else ok[j][st[i]] = true;
              i++; j++;
        } 
        int ans=0;
        for (i=0; i<d; ++i)
            if (match(i)) ans++;
        printf("%d\n",ans);
    }
}

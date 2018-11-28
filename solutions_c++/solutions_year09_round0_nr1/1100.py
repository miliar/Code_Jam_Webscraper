#include<iostream>

using namespace std;
string s[5001];
bool f[16][26];
int main(){

    int l,d,n;
    scanf("%d%d%d",&l,&d,&n);
    
    for (int i=1;i<=d;++i)
        cin >> s[i];
            char c;
    scanf("%c",&c);
    for (int i=1;i<=n;++i){

        int ans=0;
        memset(f,0,sizeof(f));
        for (int j=1;j<=l;++j){
            scanf("%c",&c);
            if (c=='('){
                        scanf("%c",&c);
                        while(c!=')'){
                           f[j][c-'a']=true;                   
                           scanf("%c",&c);
                           }
                        }
            else f[j][c-'a']=true;
            }
        scanf("%c",&c);
        for (int j=1;j<=d;++j){
            int tmp=0;
            for (int k=1;k<=l;++k)
                if (f[k][s[j][k-1]-'a']==true) tmp++;
            if (tmp==l) ans++;
            }
        cout <<"Case #"<<i<<": "<<ans<<endl;
        }
    

    }

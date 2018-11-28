#include<iostream>
#define LEN 19
using namespace std;
string s="welcome to code jam",st;
int f[501][20],t[5];
int main(){
    int n;
    cin >> n;
    char c;
    scanf("%c",&c);
    for (int i=1;i<=n;++i){
        int ans=0;


        getline(cin,st);
        memset(f,0,sizeof(f));
        for (int j=0;j<=st.size();++j){
            if (st[j]=='w') f[j][0]=1;
            for (int k=1;k<LEN;++k)
                if (st[j]==s[k])
                                 for (int tk=0;tk<j;++tk)
                                     if (st[tk]==s[k-1]) f[j][k]=(f[j][k]+f[tk][k-1])%10000;
            ans=(ans+f[j][18])%10000;                                          
            }
        
        cout <<"Case #"<<i<<": ";
        for (int j=1;j<=4;++j){
            t[j]=ans%10;
            ans/=10;
            }
        for (int j=4;j>=1;--j) cout << t[j];
        cout << endl;
            
        }

    }

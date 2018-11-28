#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
const int base = 10000;
string wcom = "welcome to code jam";
string st;
int F[555][22];
int main(){
    
    freopen("welcome2.in", "r", stdin);
    freopen("welcome.out", "w", stdout);
    
    int n0fTest;
    scanf("%d\n", &n0fTest);
    int m = wcom.size()-1;
    For(kase,1,n0fTest){
//        scanf("%s", st[i]);
        getline(cin, st);
        int n=st.size()-1;        
        memset(F, 0, sizeof(F));

        if (st[0]==wcom[0]) F[0][0]=1;

        For(i,1,n) For(j,0,m){
            F[i][j]=F[i-1][j];
            if (st[i]==wcom[j]) 
                if (j==0) F[i][j]++;
                     else F[i][j]+=F[i-1][j-1];
            if (F[i][j]>=base) F[i][j]-=base;
        }

        int kq=F[n][m];
        cout<<"Case #"<<kase<<": ";
        if (kq<10) cout<<"000";
        else if (kq<100) cout<<"00";
        else if (kq<1000) cout<<"0";
        cout<<kq<<endl;
    }
    return 0;
}

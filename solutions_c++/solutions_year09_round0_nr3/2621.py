#include<iostream>
#include<string>
using namespace std;

const string aim("welcome to code jam");
const int maxlen=500+5;
const int mask=10000;

string s;
int n,m;
int f[20][maxlen];

//f[i,j][0.. 19][0.. m]=f[i,j-1]+(aim=s)f[i-1,j-1];
void solve(){
    getline(cin,s);
    m=s.length();
    int i,j;
    for (i=1;i<=19;++i) f[i][0]=0;
    for (i=0;i<=m;++i) f[0][i]=1;
    for (i=1;i<=19;++i)
        for (j=1;j<=m;++j){
            f[i][j]=f[i][j-1];
            if (aim[i-1]==s[j-1]) f[i][j]+=f[i-1][j-1];
            f[i][j]%=mask;
        }
    cout<<f[19][m]/1000<<(f[19][m]/100)%10<<(f[19][m]/10)%10<<f[19][m]%10<<endl;
}

int main(){
    cin>>n; cin.get();
    for (int i=1;i<=n;++i){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

#include<fstream>
#include<iomanip>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m,ans,c[10000],s[10000];
double anss;
ifstream cin("4.in");
ofstream cout("4.out");
int main()
{
    int i,j,l;
    cin>>n;
    for(l=1;l<=n;l++){
        cin>>m;ans=0;
        for(j=0;j<m;j++){
            cin>>s[j];
            c[j]=s[j];
        }
        sort(&s[0],&s[j]);
        for(j=0;j<m;j++)
            if(c[j]!=s[j]) ans++;
        anss=double(ans);
        cout<<"Case #"<<l<<": "<<fixed<<setprecision(6)<<anss<<endl;
    }
    return 0;
}

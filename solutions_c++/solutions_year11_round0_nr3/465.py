#include<cstdio>
#include<fstream>
using namespace std;
int n,m,ans,sum,mmin=1000001,s[10000];
ifstream cin("3.in");
ofstream cout("3.out");
int main()
{
    int i,j,k,l;
    cin>>n;
    for(l=0;l<n;l++){
        cin>>m;
        mmin=1000001;ans=0;sum=0;
        for(i=0;i<m;i++){
            cin>>s[i];
            ans^=s[i];
            sum+=s[i];
            if(mmin>s[i])
                mmin=s[i];
        }
        cout<<"Case #"<<l+1<<": ";
        if(ans==0) cout<<sum-mmin<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

#include <iostream>
#include <cstdlib>
#include <string>
#include <iomanip>
using namespace std;

string p = "welcome to code jam";
string s;
int a[600][20];

int count()
{
    int l = s.size();
    if(l<19)return 0;
    for(int i=0;i<=l;i++)a[i][0]=1;
    if(s[0]=='w')a[0][1]=1;
    for(int i=1;i<l;i++){
        for(int j=1;j<=19;j++){
            a[i][j]=a[i-1][j];
            if(s[i]==p[j-1]){
                a[i][j]+=a[i-1][j-1];
                a[i][j]%=10000;
            }
        }
    }
   return a[l-1][19];
}
int main(int argc, char const* argv[])
{
    int t,i=1;
    cin>>t;
    getline(cin,s);
    while (t--) {
        getline(cin,s);
        memset(a,0,sizeof a);
        cout<<"Case #"<<i<<": ";
        //printing business
        int r = count();
        { 
            int x=r,c=0;
            while(x){
              c++;
              x/=10;
              }
            if(c<4){c=4-c;while(c--)cout<<"0";}
            if(r)cout<<r<<endl;
            else cout<<endl;
        }
        i++;
    }
    return 0;
}

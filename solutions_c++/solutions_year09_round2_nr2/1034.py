#define ll long long
#include <iostream>
using namespace std;
int per[100],per2[100];
int i,cnt;
string s;
ll n;
int main(){
    int t;
    cin>>t;getchar();
    for (int c=1;c<=t;c++){
        getline(cin,s);
        memset(per,0,sizeof per); cnt=s.length();
        cout<<"Case #"<<c<<": ";
        bool ok = true;
        for (i=0;i<cnt;i++){
            if (i!=0 && s[i]>s[i-1]) ok=false;
            per[i] = s[i] - 48;
        }
        next_permutation(per,per+cnt);
        if (per[0]==0){
            int min=10,mini;
            for (int i=1;i<cnt;i++){
                if (per[i]<min && per[i]!=0){min=per[i];mini=i;}
            }
            int tt=per[0];
            per[0]=per[mini];
            per[mini]=tt;
        }
        for (i=0;i<cnt;i++) {
            cout<<per[i];
            if (i==0 && ok) cout<<"0";
        }
        cout<<endl;
    }
}

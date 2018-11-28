#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
#define _ACM_DBG_SMALL
//#define _ACM_DBG_LARGE
bool isPrime[100001]={0};
int sound[10000]={0};
int n;
int l,h;
int gcd();
int main()
{
    ifstream cin("C-small-attempt1.in");
    if(!cin) return 0;
    #ifdef _ACM_DBG_SMALL
    ofstream cout("retc.txt");
    #endif
    #ifdef _ACM_DBG_LARGE
    ofstream cout("reta_large.txt");
    #endif
    int ncase;
    cin>>ncase;
    for(int kcase=1;kcase<=ncase;kcase++){
        cout<<"Case #"<<kcase<<": ";

        cin>>n>>l>>h;
        for(int i=0;i<n;i++){
            cin>>sound[i];
        }
        bool flag=false;
        for(int i=l;i<=h;i++){
            flag=false;
            for(int j=0;j<n;j++){
                if(i%sound[j]!=0&&sound[j]%i!=0) {flag=true;break;}
            }
            if(flag==false){
                cout<<i<<endl;
                break;
            }
        }
        if(flag) cout<<"NO\n";

    }
}

int gcd(int *a,int n)
{
int i,d,c;
c=1;

d=a[0];
while(c==1){
for(i=0,c=0;i<n;i++){
if(d%a[i]!=0)
{c=1;d++;}
}
}
return d;
}



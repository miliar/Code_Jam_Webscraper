#include <iostream>
#include <cstdio>
using namespace std;
#define  For(i,a,b) for(int i=a; i<=b; i++)
#define Ford(i,a,b) for(int i=a; i>=b; i--)
#define fillchar(a) memset(a, 0, sizeof(a))
#define maxn 808

long long kq=0, a[maxn], b[maxn];
int n;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out","w", stdout);
    int ntest;
    cin>>ntest;
    For(test,1,ntest){
        cin>>n;
        For(i,1,n) cin>>a[i];
        For(j,1,n) cin>>b[j];
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        kq=0;
        For(i,1,n) kq+=a[i]*b[n-i+1];
        cout<<"Case #"<<test<<": "<<kq<<endl;
    }    
    return 0;
}

#include <iostream>
using namespace std;

char s[511],a[]="welcome to code jam";
long f[511][20];

int main() {
//    freopen("c-small-attempt0.in","r",stdin);
    freopen("c-large.in","r",stdin);
    freopen("c.out","w",stdout);
    long test;
    scanf("%ld\n",&test);
    while (test--) {
        gets(s); 
        
        long n=strlen(s);
        memset(f,0,sizeof f);
        for(long i=0; i<=n; i++) f[i][0]=1;
        
        for(long i=1; i<=n; i++)
        for(long j=1; j<=19; j++)
            f[i][j]=(f[i-1][j]+((s[i-1]==a[j-1])?f[i-1][j-1]:0))%10000;
            
        cout<<"Case #"<<100-test<<": ";
        if (f[n][19]<10) cout<<"000";
        else if (f[n][19]<100) cout<<"00";
        else if (f[n][19]<1000) cout<<"0";
        cout<<f[n][19]<<endl;
    }
}

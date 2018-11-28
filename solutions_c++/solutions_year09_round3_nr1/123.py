#include <iostream>
#include <cstdio>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)

int main(){
    
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int n0fTest;
    cin>>n0fTest;
    For(test,1,n0fTest){

        char st[110];     
        scanf("%s", st);
        int a[110];
        
        int n=-1;
        int m=strlen(st);
        For(i,0,m-1) if (st[i] != ' ') {
            ++n;            
            if (n==0) a[i]=1; 
            else if (n==1) a[i]=0;
            else a[i]=n;
            For(j,i+1,m-1) if (st[i]==st[j]) {
                st[j]=' ';
                a[j]=a[i];
            }
        }
        long long res=a[0];
        ++n;
        if (n==1) n=2;
        For(i,1,m-1){
            res*=n;
            res+=a[i];
        }
        cout<<"Case #"<<test<<": ";        
        cout<<res<<endl;
    }
    return 0;
}

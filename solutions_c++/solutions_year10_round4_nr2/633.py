#include <cstdio>
#include <iostream>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))

int tst,test,p,m[3000],nothing,ans;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tst);
    for(int test=1;test<=tst;test++){
        scanf("%d",&p);        
        ans = 0;
        for(int i=0;i<(1<<p);i++)
            scanf("%d",&m[i]);
        for(int i=0;i<(1<<p)-1;i++)
            scanf("%d",&nothing);
        for(int i=p;i!=0;i--)
            for(int j=0;j<(1<<(i-1));j++){
                if(m[2*j]==0 || m[2*j+1]==0)
                    m[j]=0,ans++;
                else
                    m[j]=min(m[2*j],m[2*j+1])-1;                
            }
        cerr << test << "\n";
        printf("Case #%d: %d\n",test,ans);
    }
}

#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<set>

using namespace std;

typedef long long lld;


int a1,a2,b1,b2,R,C;

int sol(int a,int b){
    
        if(a>b) swap(a,b);
    
        if(a==b) return -1;
        else if(b%a==0) return 1;
        else {
            int x=1,y=1;
            if(b%a!=a || a!=b) x=sol(b%a,a);
            if(b%a+a!=b)       y=sol(a,b%a+a);
            if(x>0 && y>0) return -1;
            else return 1;
        }
        
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int C;
    scanf("%d",&C);
    for(int c=1;c<=C;c++){
        int ans=0;
        scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
        for(int i=a1;i<=a2;i++)
            for(int j=b1;j<=b2;j++)
                if(sol(i,j)>0) ans++;
        printf("Case #%d: %d\n",c,ans);
    }
return 0;
}

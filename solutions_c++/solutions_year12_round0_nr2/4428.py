#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int mx[31]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10},
    maxs[31]={-1,-1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,-1,-1},
    c[40];
int n,p,N,t,s;


int main(){
    scanf("%d",&N);
    freopen("output2.txt","w",stdout);
    
    for(int T=1;T<=N;T++)
    {
        scanf("%d %d %d",&n,&s,&p);
    
        for(int i=0;i<n;i++)
        scanf("%d",&c[i]);
        
        sort(c,c+n);
        int coun=0;

        for(int i=0;i<n;i++)
        {   
            if(mx[c[i]]>=p)
            coun++;
            else if(maxs[c[i]]>=p&&s>0)
            {
                s--; coun++;
            }
        }
        
        printf("Case #%d: %d\n",T,coun);
    }
    
//    system("pause");
    return 0;   
}

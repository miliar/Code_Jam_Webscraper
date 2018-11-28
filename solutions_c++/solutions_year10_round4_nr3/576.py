#include<stdio.h>
#include<string.h>

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t,i,j,k,n,l,a[110][110],b[110][110],ans,x1,x2,y1,y2,flag;
    
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%d",&n);
        for(i=0;i<n;i++) {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for(j=x1;j<=x2;j++) for(l=y1;l<=y2;l++) a[j][l]=1;
        }
        ans=0;
        while(1) {
            flag=0;
            for( i=1; i<=100; i++ ) {
                for( j=1; j<=100; j++ ) 
                    if(a[i][j]==1) 
                        flag = 1;
            }
            if(flag==0) break;
            for(i=1;i<=100;i++) {
                for(j=1;j<=100;j++) {
                    if(a[i][j]==1) {
                        if(a[i-1][j]==1||a[i][j-1]==1) 
                            b[i][j]=1;
                        else 
                            b[i][j]=0;
                    }
                    else {
                        if(a[i-1][j]==0||a[i][j-1]==0) 
                            b[i][j]=0;
                        else 
                            b[i][j]=1;
                    }
                }
            }
            for(i=1; i<=100; i++) 
                for(j=1;j<=100;j++) 
                    a[i][j]=b[i][j];
            ans++;
        }
        
        printf("Case #%d: %d\n",k,ans);
    }
    
    return 0;
}

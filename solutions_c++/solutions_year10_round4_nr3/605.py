#include <cstdio>
#include <iostream>

using namespace std;

int test,tst,n,x1,x2,y1,y2,cnt,ans;
int a[200][200],b[200][200];

void clear(){
    for(int i=0;i<101;i++)
        for(int j=0;j<101;j++)
            a[i][j]=0;
}

void clearB(){
    for(int i=0;i<101;i++)
        for(int j=0;j<101;j++)
            b[i][j]=0;
}


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tst);
    for(int test=1;test<=tst;test++){
        scanf("%d",&n);cnt=0;
        for(int i=0;i<n;i++){
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            for(int x=x1;x<=x2;x++)
                for(int y=y1;y<=y2;y++)
                    a[x][y] = 1,cnt++;
        }
        for(int i=0;i<7;i++){
            for(int j=0;j<7;j++)
                fprintf(stderr,"%d",a[i][j]);
            fprintf(stderr,"\n");
        }
                    fprintf(stderr,"\n");
        ans = 0;
        while (cnt){
            cnt=0;
            clearB();
            for(int x=1;x<101;x++)
                for(int y=1;y<101;y++)
                    if(a[x][y]+a[x-1][y]+a[x][y-1]>=2)
                        b[x][y]=1,cnt++;
            for(int x=0;x<101;x++)
                for(int y=1;y<101;y++)
                    a[x][y]=b[x][y];
            ans++;
        }
        cerr<<test<<"\n";
        printf("Case #%d: %d\n",test,ans);
    }
}

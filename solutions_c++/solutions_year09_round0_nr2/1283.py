#include<iostream>
#include<queue>
using namespace std;
int x[101][101],y[101][101],z[101][101];
char d[101][101],r[101];
queue<pair<pair<int,int>,int> > q;
main(){
    int t,tt,h,w,i,j,zz,b,k,c;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++){
        scanf("%d",&h);
        scanf("%d",&w);
        for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                scanf("%d",&x[i][j]);
            }
        }
        b=0;
        c='a';
        while(!q.empty()){
            q.pop();
        }
        for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                zz=x[i][j];
                d[i][j]='D';
                if(i>0&&x[i-1][j]<zz){
                    d[i][j]='N';
                    zz=x[i-1][j];
                }
                if(j>0&&x[i][j-1]<zz){
                    d[i][j]='W';
                    zz=x[i][j-1];
                }
                if(j<w-1&&x[i][j+1]<zz){
                    d[i][j]='E';
                    zz=x[i][j+1];
                }
                if(i<h-1&&x[i+1][j]<zz){
                    d[i][j]='S';
                    zz=x[i+1][j];
                }
                if(d[i][j]=='D'){
                    b++;
                    q.push(pair<pair<int,int>,int>(pair<int,int>(i,j),b));
                    y[i][j]=tt;
                    z[i][j]=b;
                }
            }
        }
        for(i=1;i<=b;i++){
            r[i]='.';
        }
        /*for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                printf("%c",d[i][j]);
            }
            printf("\n");
        }
        fflush(stdout);*/
        while(!q.empty()){
            i = ((q.front()).first).first;
            j = ((q.front()).first).second;
            k = ((q.front()).second);
            if(i>0&&d[i-1][j]=='S'){
                y[i-1][j]=tt;
                z[i-1][j]=k;
                q.push(pair<pair<int,int>,int>(pair<int,int>(i-1,j),k));
            }
            if(j>0&&d[i][j-1]=='E'){
                y[i][j-1]=tt;
                z[i][j-1]=k;
                q.push(pair<pair<int,int>,int>(pair<int,int>(i,j-1),k));
            }
            if(j<w-1&&d[i][j+1]=='W'){
                y[i][j+1]=tt;
                z[i][j+1]=k;
                q.push(pair<pair<int,int>,int>(pair<int,int>(i,j+1),k));
            }
            if(i<h-1&&d[i+1][j]=='N'){
                y[i+1][j]=tt;
                z[i+1][j]=k;
                q.push(pair<pair<int,int>,int>(pair<int,int>(i+1,j),k));
            }
            q.pop();
        }
        printf("Case #%d:\n",tt);
        for(i=0;i<h;i++){
            for(j=0;j<w;j++){
                if(r[z[i][j]]=='.'){
                    r[z[i][j]]=c++;
                }
                printf("%c ",r[z[i][j]]);
            }
            printf("\n");
        }
    }
}

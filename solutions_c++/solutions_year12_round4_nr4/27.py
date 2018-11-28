#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
int n,m;
char in[100][100];
struct XD{
    int yl,yr,p;
    int x;
    void print(){
        printf("x=%d (%d,%d)\n",x,yl,yr);
    }
    int w(){return yr-yl+1;}
}block[4000];
int bn[100][100],bc;
int tx[10],ty[10];
int que[4000][2],qs,qe;
inline void add(int x,int y){
    int ly=y,ry=y;
    while(in[x][ly]=='.')ly--;
    while(in[x][ry]=='.')ry++;
    ly++;
    ry--;
    for(int i=ly;i<=ry;i++){
        que[qe][0]=x;
        que[qe][1]=i;
        qe++;
        bn[x][i]=bc;
    }
    block[bc].x=x;
    block[bc].yl=ly;
    block[bc].yr=ry;
    bc++;
}
int _l[4000],lc;
int _l2[4000],lc2;
int avail[100];
int u[4000],uid;
int *l=_l,*l2=_l2;
inline void run(){
    int i,hd=0;
    for(i=0;i<lc;i++){
        int x=block[l[i]].x;
        int y=block[l[i]].p;
        if(in[x+1][y]=='.'){
            if(bn[x+1][y]==-1)break;
            else hd=1;
        }
    }
    if(i<lc)return;
    if(!hd)return;
    uid++;
    for(i=0;i<lc;i++){
        int x=block[l[i]].x;
        int y=block[l[i]].p;
        if(in[x+1][y]=='.'){
            u[bn[x+1][y]]=uid;
        }else{
            u[l[i]]=uid;
        }
    }
    lc2=0;
    for(i=0;i<bc;i++)if(u[i]==uid)l2[lc2++]=i;
    throw 514;
}
inline bool solve(int sx,int sy,int& cnt){
    cnt=0;
    qs=qe=0;
    memset(bn,-1,sizeof(bn));
    bc=0;
    add(sx,sy);
    while(qs<qe){
        int x=que[qs][0];
        int y=que[qs][1];
        qs++;
        if(bn[x-1][y]==-1&&in[x-1][y]=='.'){
            add(x-1,y);
        }
    }
    cnt=0;
    int i,j;
    lc=0;
    for(i=0;i<bc;i++){
        //block[i].print();
        cnt+=block[i].w();
        l[lc++]=i;
    }
    for(i=block[0].yl;i<=block[0].yr;i++){
        if(in[block[0].x+1][i]=='.')avail[i]=0;
        else avail[i]=1;
    }
    while(lc>1){
        int minw=10000,maxw=0;
        for(i=0;i<lc;i++){
            int w=block[l[i]].w();
            minw=min(minw,w);
            maxw=max(maxw,w);
        }
        bool f=0;
        try{
            int s,t;
            for(s=0;s<minw;s++){
                if(!avail[block[0].yl+s])continue;
                for(i=0;i<lc;i++){
                    block[l[i]].p=block[l[i]].yl+s;
                }
                run();
            }
            for(s=minw;s<maxw;s++){
                for(t=0;t<maxw;t++){
                    block[0].p=max(min(block[0].yl+s,block[0].yr)-t,block[0].yl);
                    if(!avail[block[0].p])continue;
                    for(i=1;i<lc;i++){
                        block[l[i]].p=max(min(block[l[i]].yl+s,block[l[i]].yr)-t,block[l[i]].yl);
                    }
                    run();
                }
            }
        }catch(...){
            /*printf("lc=%d lc2=%d\n",lc,lc2);
            for(i=0;i<lc;i++)printf("%d,%d ",l[i],block[l[i]].p);
            puts("");*/
            swap(l,l2);
            swap(lc,lc2);
            f=1;
        }
        if(f==0)return 0;
    }
    return 1;
}
int main(){
    int t,i,j,cas=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)scanf("%s",in[i]);
        printf("Case #%d:\n",cas++);
        int q=0;
        for(i=0;i<n;i++)for(j=0;j<m;j++)if(in[i][j]<='9'&&in[i][j]>='0'){
            tx[in[i][j]-'0']=i;
            ty[in[i][j]-'0']=j;
            q=max(q,in[i][j]-'0'+1);
            in[i][j]='.';
        }
        for(i=0;i<q;i++){
            printf("%d: ",i);
            int v;
            int r=solve(tx[i],ty[i],v);
            printf("%d %s\n",v,r?"Lucky":"Unlucky");
        }
    }
}


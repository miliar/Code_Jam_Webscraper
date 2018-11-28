#include<iostream>
#include<cstdio>
# define MAX 100
using namespace std;

int V[MAX][MAX],alt[MAX][MAX],H,W;
char out[MAX][MAX];

void rec(int x,int y,char *pc)
{    int dl,c=0;
     dl=0;
     if(x>0){{if(dl<(alt[x][y]-alt[x-1][y])) {dl=alt[x][y]-alt[x-1][y]; c=1;}}}
     if(y>0) {{if(dl<(alt[x][y]-alt[x][y-1])) {dl=alt[x][y]-alt[x][y-1]; c=2;}}}
     if(y<(W-1)) {{if(dl<(alt[x][y]-alt[x][y+1])) {dl=alt[x][y]-alt[x][y+1]; c=3;}}}
     if(x<(H-1)){{if(dl<(alt[x][y]-alt[x+1][y])) {dl=alt[x][y]-alt[x+1][y]; c=4;}}}
     if(c==0) {  if(V[x][y]==0) { V[x][y]=-1; *pc=*pc+1; out[x][y]=*pc; }return; }
     V[x][y]=1;
     if(c==1)   if(V[x-1][y]==-1|| V[x-1][y]==1) *pc=out[x-1][y]; else rec(x-1,y,pc);
     if(c==2)           if(V[x][y-1]==-1 || V[x][y-1]==1) *pc=out[x][y-1]; else rec(x,y-1,pc);
     if(c==3)           if(V[x][y+1]==-1|| V[x][y+1]==1) *pc=out[x][y+1]; else rec(x,y+1,pc);
     if(c==4)           if(V[x+1][y]==-1 || V[x+1][y]==1) *pc=out[x+1][y]; else rec(x+1,y,pc);
    out[x][y]=*pc;
}
    

main()
{
      int t,v=1;
      char pc;
      cin>>t;
      while(t--)
      {
                cin>>H>>W;
                for(int i=0;i<H;i++) for(int j=0;j<W;j++) cin>>alt[i][j];
                for(int i=0;i<100;i++) for(int j=0;j<100;j++) V[i][j]=0;
                 
                pc='a'-1;   
                 for(int i=0;i<H;i++) for(int j=0;j<W;j++) rec(i,j,&pc);
                 printf("Case #%d:\n",v++);
                for(int i=0;i<H;i++){ for(int j=0;j<W;j++){ cout<<out[i][j]<<" ";} cout<<endl; }
                
      }
      return 0;
}

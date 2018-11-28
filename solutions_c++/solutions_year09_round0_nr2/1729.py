#include<iostream>
#include<queue>
using namespace std;
bool adjm[10010][10010];
void bfsFill(char out[][110],int &H,int &W,char &label,int i,int j,int M)
{
     int v=i*W+j,i1,t,x,y;
     char color[10010]={0};
     color[v]=1;
     if(out[i][j]) return;
     queue<int> q;
     q.push(v);
     while(!q.empty()) {
                        t=q.front();q.pop();
                        color[t]=2;
                        x=t/W;y=t%W;
                        out[x][y]=label;
                        for(i1=0;i1<M;i1++) if(adjm[t][i1] && color[i1]==0) {color[i1]=1;q.push(i1);} 
                       }
     label++;
}
int main()
{
    int T,H,W,i,j,k,alt[110][110],n,nx,ny,s,sx,sy,e,ex,ey,w,wx,wy,v,nV,Rx,Ry,R,A;
    char label,out[110][110];
    cin>>T;
    for(k=0;k<T;k++) {
                      cin>>H>>W;nV=H*W;
                      for(i=0;i<H;i++) for(j=0;j<W;j++) cin>>alt[i][j];
                      //for(i=0;i<H;i++) {for(j=0;j<W;j++) cout<<(i*W+j)<<" ";cout<<endl;}
                      for(i=0;i<=nV;i++) for(j=0;j<=nV;j++) {adjm[i][j]=false;out[i][j]=0;}
                      for(i=0;i<H;i++) for(j=0;j<W;j++) {
                                                         v=i*W+j;
                                                         nx=i-1;ny=j;if(nx>=0 && nx<H && ny>=0 && ny<W) n=nx*W+ny; else n=-1;
                                                         sx=i+1;sy=j;if(sx>=0 && sx<H && sy>=0 && sy<W) s=sx*W+sy; else s=-1;
                                                         wx=i;wy=j-1;if(wx>=0 && wx<H && wy>=0 && wy<W) w=wx*W+wy; else w=-1;
                                                         ex=i;ey=j+1;if(ex>=0 && ex<H && ey>=0 && ey<W) e=ex*W+ey; else e=-1;
                                                         //cout<<n<<" "<<w<<" "<<e<<" "<<s<<endl;
                                                         A=100000;
                                                         if(n>=0) {if(alt[nx][ny]<alt[i][j] && alt[nx][ny]<A) {Rx=nx;Ry=ny;R=n;A=alt[nx][ny];}}
                                                         if(w>=0) {if(alt[wx][wy]<alt[i][j] && alt[wx][wy]<A) {Rx=wx;Ry=wy;R=w;A=alt[wx][wy];}}
                                                         if(e>=0) {if(alt[ex][ey]<alt[i][j] && alt[ex][ey]<A) {Rx=ex;Ry=ey;R=e;A=alt[ex][ey];}}
                                                         if(s>=0) {if(alt[sx][sy]<alt[i][j] && alt[sx][sy]<A) {Rx=sx;Ry=sy;R=s;A=alt[sx][sy];}}
                                                         //cout<<Rx<<" "<<Ry<<" "<<R<<" "<<A<<endl;
                                                         if(A!=100000) adjm[R][v]=adjm[v][R]=true;
                                       }                     
                      //for(i=0;i<nV;i++) {for(j=0;j<nV;j++) cout<<adjm[i][j]<<" ";cout<<endl;}
                      label='a';
                      for(i=0;i<H;i++) for(j=0;j<W;j++) bfsFill(out,H,W,label,i,j,nV);  
                      cout<<"Case #"<<k+1<<":"<<endl;
                      for(i=0;i<H;i++) {for(j=0;j<W;j++) cout<<out[i][j]<<" ";cout<<endl;}                  
                     }
    return 0;
}

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
using namespace std;
#define INF 10000000

map<vector<int>,int> memo;

int M[16][16];

long long getState(const vector<int> &p)
{
 long long r=0;
 for(int i=0;i<p.size();i++){
  r=r*256+p[i];
 }
 return r;
}

void fromState(long long s,vector<int> &p)
{
 for(int i=p.size()-1;i>=0;i--){
  p[i]=s&255;
  s>>=8;
 }
}

bool adj(int a,int b){
 int ax=a&15;
 int ay=a>>4;
 int bx=b&15;
 int by=b>>4;
 return abs(ax-bx)+abs(ay-by)==1;
}

vector<int> visited(10);
void solve(const vector<int>&p,int pos,int n)
{
 for(int i=0;i<n;i++){
  if(visited[i])continue;
  if(!adj(p[i],p[pos]))continue;
  visited[i]=1;
  solve(p,i,n);
 }
}

bool isCon(const vector<int> &p)
{
 int n=p.size();
 for(int i=0;i<n;i++) visited[i]=0;
 visited[0]=1;
 solve(p,0,n);
 for(int i=0;i<n;i++)if(!visited[i])return false;
 return true;
}

void show(const vector<int> &boxes,bool isDan,int X, int Y){
for(int y=0;y<Y+2;y++){for(int x=0;x<X+2;x++){
bool a=false;for(int t=0;t<boxes.size();t++)if(boxes[t]==x+y*16)cout<<'o',a=true;if(!a)cout<<(char)M[y][x];
}cout<<endl;}
cout<<isDan<<endl;
cout<<"---"<<endl;
}


int main( void )
{
 int T;
 cin>>T;
 for(int XX=1;XX<=T;++XX){
  int X,Y;
  cin>>Y>>X;
  for(int y=0;y<Y+2;y++)
   for(int x=0;x<X+2;x++)
    M[y][x]='#';
  vector<int> boxes;
  vector<int> goals;
  for(int y=0;y<Y;y++){
   string str;
   cin>>str;
   //cout<<str<<endl;
   for(int x=0;x<X;x++){
    switch(str[x]){
    case 'o':
     //cout << (x+1) << " " << (y+1) << endl;
     //cout << ((y+1)*16+(x+1)) << endl;
     M[y+1][x+1]='.';
     boxes.push_back((y+1)*16+(x+1));
     break;
    case 'w':
     M[y+1][x+1]='.';
     boxes.push_back((y+1)*16+(x+1));
     goals.push_back((y+1)*16+(x+1));
     break;
    case 'x':
     M[y+1][x+1]='.';
     goals.push_back((y+1)*16+(x+1));
     break;
    default:
     M[y+1][x+1]=str[x];
      break;
    }
   }
  }
  // parse done
  queue< pair<int,long long> > wl;
  wl.push(pair<int,long long>(0,getState(boxes)));
  int N=boxes.size();
  long long gs=getState(goals);
  int ans=-1;
  const int dx[]={-1,1,0,0};
  const int dy[]={0,0,-1,1};
  vector<int> boxes2=boxes;
/*
   for(int i=0;i<N;i++){
    cout<<(boxes2[i]%16)<<' '<<(boxes2[i]/16)<<endl;
   }
   cout << "---" << endl;
*/
  set<long long> VISITED;
  while(!wl.empty()){
   int D=wl.front().first;
   long long s=wl.front().second;
   wl.pop();
   if(s==gs){ans=D;break;}
   if(VISITED.count(s)>0)continue;
   VISITED.insert(s);
   fromState(s,boxes);
   bool isDan=isCon(boxes);
   //show(boxes,isDan,X,Y);
   /*
   for(int i=0;i<N;i++){
    cout<<boxes[i]%16<<' '<<boxes[i]/16<<endl;
   }
   cout << "---" << endl;
   */
   for(int i=0;i<N;i++){
    int ix=boxes[i]&15;
    int iy=boxes[i]>>4;
    //cout<<ix<<" " <<iy<<endl;
    for(int d=0;d<4;d+=2){
     int DX=dx[d],DY=dy[d];
     int p1=(ix+DX)+((iy+DY)<<4);
     int p2=(ix-DX)+((iy-DY)<<4);
     if(M[iy+DY][ix+DX]=='.'&&M[iy-DY][ix-DX]=='.'){
      for(int j=0;j<N;j++)
       if(boxes[j]==p1 || boxes[j]==p2) goto NEX;
      {
       boxes2=boxes;
       boxes2[i]=p1;
       if(isDan||isCon(boxes2)){
        sort(boxes2.begin(),boxes2.end());
        wl.push(pair<int,long long>(D+1,getState(boxes2)));
       }
      }
      {
       boxes2=boxes;
       boxes2[i]=p2;
       if(isDan||isCon(boxes2)){
        sort(boxes2.begin(),boxes2.end());
        wl.push(pair<int,long long>(D+1,getState(boxes2)));
       }
      }
     } // if
     NEX:;
    } // d
   } // i
  } // end of BFS
  printf("Case #%d: %d\n",XX,ans);
 }
 return 0;
}


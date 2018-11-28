#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdio>
#include <map>
#include <list>

using namespace std;

//union find
int p[10000],rank[10000];

void make_set(int x){
    p[x]=x;
    rank[x]=0;
}
void link(int x,int y){
    if(rank[x]>rank[y])
        p[y]=x;
    else{
        p[x]=y;
        if(rank[x]==rank[y]){
            rank[y]++;
        }
    }
}
int find_set(int x){
    if(x!=p[x]){
        p[x]=find_set(p[x]);
    }
    return p[x];
}
void Union(int x,int y){
    link(find_set(x),find_set(y));
}
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

int main(){
    int T;cin>>T;
    int g[100][100];
    for(int tt=1;tt<=T;tt++){
      
      int h,w;
      cin>>h>>w;
      
      for(int i=0;i<h;i++) for(int j=0;j<w;j++){
	cin>>g[i][j];
	make_set(i*w+j);
      }
      
      for(int i=0;i<h;i++) for(int j=0;j<w;j++){
	 int mini=g[i][j];
	 //if(i==3&&j==0) cout<<"llega"<<endl;
	 for(int k=0;k<4;k++){
	  int ni=i+dx[k];
	  int nj=j+dy[k];
	  if(ni<0||nj<0||ni>=h||nj>=w) continue;
	  mini=min(mini,g[ni][nj]);
	 }
	 //if(i==3&&j==0) cout<<mini<<endl;
	 if(mini<g[i][j]){
	   //if(i==3&&j==0) cout<<mini<<endl;
	  for(int k=0;k<4;k++){
	  int ni=i+dx[k];
	  int nj=j+dy[k];
	  if(ni<0||nj<0||ni>=h||nj>=w) continue;
	  if(g[ni][nj]==mini){
	   Union(i*w+j,ni*w+nj);
	   //if(i==3&&j==0) cout<<mini<<" "<<i<<" "<<j<<" - "<<ni<<" "<<nj<<" - "<<p[i*w+j]<<" "<<p[ni*w+nj]<<endl;
	   break;
	  }
	 } 
	 }
      }
      
      map<int,char> mapa;
      char maxi='a';
      cout<<"Case #"<<tt<<":"<<endl;
      for(int i=0;i<h;i++){
	for(int j=0;j<w;j++){
	  int aux=find_set(i*w+j);
	  if(mapa.find(aux)==mapa.end()) mapa[aux]=maxi++; 
	  cout<<mapa[aux];
	  if(j<w-1) cout<<" ";
	  else cout<<endl;
	}
      }
    }
}
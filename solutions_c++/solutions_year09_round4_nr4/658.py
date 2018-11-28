#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cassert>
#include<cmath>
#define sq(x) ((x)*(x))

using namespace std;

struct circle{
  int x,y,r;
};

circle pts[5];

int main(){
  int PC;
  cin>>PC;
  for(int pc=1;pc<=PC;pc++){
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
      scanf("%d %d %d",&pts[i].x,&pts[i].y,&pts[i].r);
    }
    printf("Case #%d: ",pc);
    assert(N<=3);
    if(N==1){printf("%.8lf\n",(double)pts[0].r);}
    if(N==2){printf("%.8lf\n",(double)(pts[0].r>pts[1].r?pts[0].r:pts[1].r));}
    if(N==3){
      vector<int> A(3,0);
      A[2]=1;A[1]=1;
      double ans=1000.0;
      do{
	bool first=false;
	int x,y,z;
	for(int i=0;i<3;i++)if(!A[i])z=i;
	for(int i=0;i<3;i++){
	  if(A[i] and !first){x=i;first=true;}
	  if(A[i] and first)y=i;
	}
	double r1=(sqrt(sq(pts[x].x-pts[y].x)+sq(pts[x].y-pts[y].y))+pts[x].r+pts[y].r)/2;
	double r2=pts[z].r;
	double rm=r1>r2?r1:r2;
	ans=ans>rm?rm:ans;
      }while(next_permutation(A.begin(),A.end()));
      printf("%.8lf\n",ans);
    }
  }
}

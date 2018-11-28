#include <cstdio>
#include <list>
using namespace std;
struct Point{
  int x;
  int y;
  Point(int a, int b){
    x=a;
    y=b;
  }
};
int regions[150][150];
list<Point> listy[150][150];

void oznacz(Point a, int id){
   regions[a.x][a.y]=id;
   for(list<Point>::iterator it=listy[a.x][a.y].begin(); it!=listy[a.x][a.y].end(); it++)
     oznacz(*it, id);
}

using namespace std;
const int INF=50000;
int main(){
   int T;
   scanf("%d",&T);
   for(int mapId=1; mapId<=T; mapId++){
	int H,W;
	scanf("%d%d",&H,&W);
	int mapa[H+2][W+2];	
	for(int i=0;i<=W+1;i++)
	   mapa[0][i]=mapa[H+1][i]=INF;
	for(int i=0;i<=H+1;i++)
	   mapa[i][0]=mapa[i][W+1]=INF;
	
	for(int i=1; i<=H; i++)
	  for(int j=1; j<=W; j++)
	    scanf("%d",&mapa[i][j]);
	
	list<Point> sinks;
	for(int i=0; i<=H+1; i++)
	  for(int j=0; j<=W+1; j++)
	    listy[i][j].clear();

	for(int i=1; i<=H; i++)
	  for(int j=1; j<=W; j++){
	    int min=INF;
	    if(mapa[i-1][j]<min)min=mapa[i-1][j];
	    if(mapa[i][j-1]<min)min=mapa[i][j-1];
	    if(mapa[i][j+1]<min)min=mapa[i][j+1];		
	    if(mapa[i+1][j]<min)min=mapa[i+1][j];

	    if(min>=mapa[i][j])sinks.push_back(Point(i,j));
	    else if(mapa[i-1][j]==min)listy[i-1][j].push_back(Point(i,j));
	    else if(mapa[i][j-1]==min)listy[i][j-1].push_back(Point(i,j));
	    else if(mapa[i][j+1]==min)listy[i][j+1].push_back(Point(i,j));
	    else if(mapa[i+1][j]==min)listy[i+1][j].push_back(Point(i,j));
	    
	  }
	 int k=0;
	 for(list<Point>::iterator it=sinks.begin(); it!=sinks.end(); it++)
	    oznacz(*it, k++);

	 char label[50];
	 for(int i=0; i<k; i++)
	    label[i]=0;
	 int curlab='a';
	 for(int i=1; i<=H; i++)
	    for(int j=1; j<=W; j++)
	       if(label[regions[i][j]]==0)
		  label[regions[i][j]]=curlab++;

	 printf("Case #%d:\n", mapId);
	 for(int i=1; i<=H; i++){
	   for(int j=1; j<=W; j++)
	      printf("%c ",label[regions[i][j]]);
	   printf("\n");
	 }

   }
}

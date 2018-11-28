#include <cstdio>
#include <vector>
#define inlimits(i,j) (0 <= (i) && (i) < H && 0 <= (j) && (j) < W)

const int inf=0x7FFFFFFF;
using namespace std;
typedef vector<int> vi;

int u=0;
char ff(const vector<vi> &M, vector<vector<char> > &C, int i, int j,int H, int W )
{
   if(C[i][j])
   return C[i][j];
   
   int dr[4]={1,0, 0,-1};
   int dc[4]={0,1,-1, 0};
   
   int mink=-1,minv=inf;
   for(int k=0 ; k < 4; k++)
   {
   	int r=i+dr[k];
   	int c=j+dc[k];
    
    	if(inlimits(r,c) && M[i][j] > M[r][c] && M[r][c] <= minv)
    	{
    	 mink=k;
    	 minv=M[r][c];	
    	}
   }
   
   if(mink == -1)
   {
   C[i][j]=(char)(97+u);
   u++;
   return C[i][j];
   }
   else
   return C[i][j]=ff(M,C,i +dr[mink],j+dc[mink],H,W);
}


int main()
{
	int T,H,W;
	scanf("%d ",&T);
	for(int t=0; t < T; t++)
	{
		u=0;
	  scanf("%d %d",&H,&W);
	  vector<vi> M(H,vi(W,0));
	  vector< vector<char> > C(H,vector<char>(W,0));
	  
	  for(int i=0; i < H; i++)
	   	for(int j=0; j < W; j++)
	    scanf("%d",&M[i][j]);
	    
	  for(int i=0; i < H; i++)
	   for(int j=0; j < W; j++)
	   ff(M,C,i,j,H,W);	
	   
	   printf("Case #%d:\n",(t+1));
	   for(int i=0; i < H; i++)
	   {
	   	 for(int j=0; j < W; j++)
	   	 {
	   	 if(j == 0)
	   	 printf("%c",C[i][j]);
	   	 else
	   	 printf(" %c",C[i][j]);
	   	 }
	   printf("\n");	
	   }
	}
	
	return 0;
}

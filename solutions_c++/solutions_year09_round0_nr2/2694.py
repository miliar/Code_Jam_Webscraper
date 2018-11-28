#include <iostream>
#include <cstdio>

using namespace std;

#define FOR(i,N) for(int i=0; i<(N); ++i)

int T,H,W,S;
int mat[105][105];
int ans[105][105];
char A[105][105];
bool v[105][105];

int dfs(int,int);

int main()
  {


    cin>>T;

    char sinks[26];
    int cnt=0;

    FOR(i,T)
      {
	scanf("%d %d",&H,&W);

        FOR(r,105) FOR (c,105) mat[r][c]=20000,v[r][c]=false,ans[r][c]=-1,A[r][c]=-1;

	FOR(r,H) FOR(c,W) scanf("%d", &mat[r+1][c+1]);
        
	S=0;
	
	FOR(r,H) {
	  FOR(c,W) {
	    if((mat[r+1][c+1]<=mat[r][c+1]) && (mat[r+1][c+1]<=mat[r+2][c+1]) && (mat[r+1][c+1]<=mat[r+1][c]) && (mat[r+1][c+1]<=mat[r+1][c+2])) ans[r][c]=S,S++;
	  }
	}
	
	FOR(r,H) FOR(c,W) if(ans[r][c]==-1) dfs(r,c);
	
	FOR(k,S) sinks[k]=-1;
        cnt=0;

	FOR(r,H)
	  {
	    FOR(c,W) 
	      {
		if(sinks[ans[r][c]]==-1) {
		  sinks[ans[r][c]]='a'+cnt;
		  cnt++;
		}
	      }
	  }

	printf("Case #%d:\n",i+1);

	FOR(r,H) { FOR(c,W) printf("%c ",sinks[ans[r][c]]); printf("\n");}
        
      }
	

    return(0);
  }

int dfs(int r, int c)
  {
    if(r < 0 || c < 0 || r>=H || c>=W) return(-1);
    
    if(ans[r][c]!=-1) return(ans[r][c]);

    if((mat[r][c+1]<=mat[r+1][c]) && (mat[r][c+1]<=mat[r+1][c+2]) && (mat[r][c+1]<=mat[r+2][c+1])) ans[r][c]=dfs(r-1,c);
    if((mat[r+1][c]<mat[r][c+1]) && (mat[r+1][c]<=mat[r+1][c+2]) && (mat[r+1][c]<=mat[r+2][c+1])) ans[r][c]=dfs(r,c-1);
    if((mat[r+1][c+2]<mat[r][c+1]) && (mat[r+1][c+2]<mat[r+1][c]) && (mat[r+1][c+2]<=mat[r+2][c+1])) ans[r][c]=dfs(r,c+1);
    if((mat[r+2][c+1]<mat[r+1][c]) && (mat[r+2][c+1]<mat[r+1][c+2]) && (mat[r+2][c+1]<mat[r][c+1])) ans[r][c]=dfs(r+1,c);



    return(ans[r][c]);
    
  }

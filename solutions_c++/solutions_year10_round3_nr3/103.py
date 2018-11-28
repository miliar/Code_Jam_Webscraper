#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;

bool board[512][512];
bool check[513][512][512];
bool used[512][512];

void fill(int i, int j, int sz)
{
  for(int a=i; a<i+sz; a++){
    for(int b=j; b<j+sz; b++){
      used[a][b] = true;
    }
  }
}

int main()
{
  int cases;
  scanf("%d", &cases);
  for(int T=1; T<=cases; T++){
    printf("Case #%d: ", T);
    int M, N;
    scanf("%d%d", &M, &N);
    for(int i=0; i<M; i++){
      for(int j=0; j<N/4; j++){
	int x;
	scanf("%1x", &x);
	board[i][j*4] = x&8;
	board[i][j*4+1] = x&4;
	board[i][j*4+2] = x&2;
	board[i][j*4+3] = x&1;
      }
    }

    for(int i=0; i<M; i++){
      for(int j=0; j<N; j++){
	used[i][j]=false;
      }
    }
    /*
    printf("\n");
    for(int i=0; i<M; i++){
      for(int j=0; j<N; j++){
	printf("%d", board[i][j]);
      }
      printf("\n");
    }
    */
    
    for(int sz=1; sz<=min(M, N); sz++){
      for(int i=0; i<M; i++){
	for(int j=0; j<N; j++){
	  if(sz==1) {check[sz][i][j] = true; continue;}
	  check[sz][i][j] = check[sz-1][i][j] and check[sz-1][i+1][j+1] and
	    board[i+sz-1][j]==board[i][j+sz-1] and 
	    board[i+sz-1][j]!=board[i+sz-1][j+1] and
	    board[i][j] == board[i+sz-1][j+sz-1];
	}
      }
    }

    vector < pair<int, int> > ret;
    int ans=0;

    for(int sz=min(M, N); sz>=1; sz--){
      int count=0;
      for(int i=0; i<M; i++){
	for(int j=0; j<N; j++){
	  if(check[sz][i][j] and 
	     !used[i][j] and 
	     !used[i+sz-1][j] and
	     !used[i][j+sz-1] and
	     !used[i+sz-1][j+sz-1]){
	    //if(sz==6) printf("i=%d j=%d used=%d\n", i, j, used[i][j]);
	    count++;
	    fill(i, j, sz);
	  }
	}
      }
      if(count>0){ 
	ans++;
	ret.push_back(make_pair(sz, count));
      }
    }
    
    printf("%d\n", ans);

    for(int i=0; i<ret.size(); i++) printf("%d %d\n", ret[i].first, ret[i].second);
        
  }
  return 0;
}

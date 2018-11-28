#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <map>
#include <set>
using namespace std;

#define INF 1000000000
// 1e9 < INT_MAX/2

void tos(){
  int R,C;
  cin>>R>>C;
  vector<vector<int> > S(R,C);
  for(int i=0; i<R; i++){
    for(int j=0; j<C; j++){
      cin>>S[i][j];
    }
  }
  int T=R+C-1;
  int res=-1;
  vector<vector<int> > A(R+1,C+1);
  for(int bi=0; bi<(1<<T); bi++){
    for(int i=0; i<R; i++){
      A[i][C-1]=(bi>>i)&1;
    }
    for(int j=0; j<C-1; j++){
      A[R-1][j]=(bi>>(R+j))&1;
    }
    for(int i=R-1; i-->0; ){
      for(int j=C-1; j-->0; ){
	A[i][j]=S[i+1][j+1];
	for(int k=0; k<=2; k++){
	  for(int l=0; l<=2; l++){
	    if(k+l==0) continue;
	    A[i][j]-=A[i+k][j+l];
	  }
	}
	if(A[i][j]<0 || A[i][j]>1) goto FAIL;
      }
    }
    if(S[0][0]!=A[0][0]+A[0][1]+A[1][0]+A[1][1]) goto FAIL;
    for(int i=1; i<R; i++){
      int j=0;
      int cnt=0;
      for(int k=-1; k<=1; k++){
	for(int l=0; l<=1; l++){
	  cnt+=A[i+k][j+l];
	}
      }
      if(cnt!=S[i][j]) goto FAIL;
    }
    for(int j=1; j<C; j++){
      int i=0;
      int cnt=0;
      for(int k=0; k<=1; k++){
	for(int l=-1; l<=1; l++){
	  cnt+=A[i+k][j+l];
	}
      }
      if(cnt!=S[i][j]) goto FAIL;
    }

    {
      //cout<<endl;
      //for(int i=0; i<R; i++){
	//for(int j=0; j<C; j++){
	  //cout<<A[i][j]<<" ";
	//}cout<<endl;
      //}
      int cnt=0;
      for(int j=0; j<C; j++){
	cnt+=A[R/2][j];
      }
      res=max(res,cnt);
    }
FAIL:;
  }
  cout<<res<<endl;
}

int main(){
  int nCases;
  cin>>nCases;
  for(int c=1; c<=nCases; c++){
    cout<<"Case #"<<c<<": ";
    tos();
  }
  return 0;
}

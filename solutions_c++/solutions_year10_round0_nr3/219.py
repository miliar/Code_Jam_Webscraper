#include <string>
#include <iostream>
#include <cstdio>
#include <set>
typedef long long ll;
using namespace std;
int R, K, N, A[1024],Nindx[1024];
ll W[1024], last;
int main()
{
  int T;
  int c = 1;
  scanf("%d", &T);
  while(T--)
    {
      scanf("%d %d %d", &R, &K, &N);
      for(int i = 0 ; i < N; i++){
	scanf("%d", A + i);
	Nindx[i] = i;
	W[i] = 0;
      }
      for(int i = 0 ; i < N; i++)
	{
	  set<int> st;
	  while(W[i] <= K)
	    {
	      W[i] += A[ Nindx[i] ];
	      last = A[ Nindx[i] ];
	      if( st.find(Nindx[i]) != st.end() ){
		Nindx[i] = (Nindx[i] + 1) % N;
		break;
	      }
	      st.insert(Nindx[i]);
	      Nindx[i] = (Nindx[i] + 1) % N;
	    }
	  Nindx[i] = (Nindx[i] - 1 + N) % N;
	  W[i] -= last;
	}
      ll Total = 0;
      int ci = 0;
      for(int i = 0 ; i < R; i++)
	{
	  Total += W[ci];
	  ci = Nindx[ci];
	}
      printf("Case #%d: %lld\n", c++, Total);
      
	
      

    }
  
}

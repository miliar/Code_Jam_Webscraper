#include <string>
#include <cstdio>
#include <iostream>
using namespace std;
string G[100];
int main()
{
  int T;
  cin >> T;
  int C = 1;

  while(T--)
    {
      int N, M;
      cin >> N >> M;
      for(int i = 0 ; i < N; i++)
	cin >> G[i];
      for(int i = 0 ; i < N - 1; i++)
	for(int j  = 0 ; j < M - 1; j++)
	  {

	    if( (G[i][j] == '#') && (G[i][j + 1] == '#') && (G[i + 1][j] == '#') && (G[i + 1][j + 1] == '#') )
	      {
		G[i][j] = '/' ;
		G[i][j + 1] = '\\' ;
		G[i + 1][j] = '\\';
		G[i + 1][j + 1] ='/';
	      }
	  }
      bool ok = true;
      for(int i = 0 ; i < N; i++)
	for(int j = 0 ; j < M; j++)
	  if( G[i][j] == '#' )
	    ok = false;
      if( !ok ){
	printf("Case #%d:\nImpossible\n", C++ );
	continue;
      }
      printf("Case #%d:\n", C++);
      for(int i = 0 ; i < N; i++)
	cout<<G[i]<<endl;
    }

}

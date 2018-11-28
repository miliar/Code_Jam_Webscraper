#include <iostream>
#include <vector>
#include <utility>

using namespace std;

typedef unsigned long long ull;
typedef pair<ull,ull> pii;

pii history[1000];

int main()
{
  int T,R,N,k;
  vector<int> g;
  cin >> T;
  for (int t=0; t<T; t++)
    {
      cout << "Case #" << t+1 << ": ";

      cin >> R >> k >> N;
      g.resize(N);
      for (int i=0; i<N; i++)
	{
	  cin >> g[i];
	  history[i]=make_pair(~(0LLU),~(0LLU));
	}

      ull c=0;
      ull pos=0;
      for (ull i=0; i<R; i++)
	{
	  if (history[pos].first==-1)
	    history[pos]=make_pair(c,i);
	  else
	    {
	      ull periodlength=i-history[pos].second;
	      ull periodcost=c-history[pos].first;
	      ull periods=(R-i)/periodlength;
	      i+=periods*periodlength;
	      c+=periods*periodcost;
	      //	      cout << "period found" << endl;
	    }
	  if (i>=R) break;

	  ull cc=0;
	  ull q=0;
	  while (cc+g[pos]<=k && q<N)
	    {
	      cc+=g[pos];
	      pos=(pos+1)%N;
	      q++;
	    }
	  c+=cc;
	  //	  cout << cc << endl;
	}
      cout << c;

      cout << endl;
    }

  return 0;
}

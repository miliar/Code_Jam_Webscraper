#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int L, D, N;
vector<string> words;

vector<string> places;


int solve()
{
 
  int ret = 0;
  for(int i = 0; i < words.size(); ++i)
    {
      string cw = words[i];
      bool add = true;
      for(int j = 0; j < cw.length(); ++j)
	{

	  string s1 =  "";
	  s1 += cw[j];
	  if(places[j].find(s1) == string::npos)
	    {
	      add = false; break;
	    }
	}
      if(add == true) ret++;
    }
  return ret;
	      



}


int main()
{
  scanf("%d%d%d\n",&L,&D,&N);
  char w[20];
  for(int i = 0; i < D; ++i)
    {
      scanf("%s",w);
      string s(w);
      words.push_back(w);
    }
  for(int i = 0; i < N; ++i)
    {
      places.clear();
      char c;
      char ops[30];
      scanf("\n");
      for(int j = 0; j < L; ++j)
	{
	  scanf("%c",&c);
	  string s;
	  if(c != '(')
	    s += c;
	  else
	    while((c = getchar())!= ')')
	       s += c;
	  places.push_back(s);
	}

      int u = solve();
      cout << "Case #"  << i+1 << ": " << u << endl;
    }
}


  

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
  int qnum = 0;
  scanf("%d", &qnum);

  int x = 0;
  while (qnum--)
    {
      x++;

  int N;
  long M;

  scanf("%d", &N);
  scanf("%d", &M);
  //printf("%d %d\n", N, M);

  char str0[100][110];
  std::set<string> path;

  path.insert("");

  int i, j;
  for (i  = 0; i < N; ++i)
    {
      scanf("%s", str0[i]);
	    string s;
   for (int k = 0; k < strlen(str0[i]); ++k)
      {
	if (str0[i][k] == '/')
	  {
	  path.insert(s);
	  //printf("A:%s\n", s.c_str());
	  }
	  s += str0[i][k];
      }
      path.insert(s);
      //printf("A:%s\n", s.c_str());
    }

      int count = 0;
  for (i  = 0; i < M; ++i)
    {
      scanf("%s", str0[i]);

      //printf("BA:%s\n", str0[i]);
	string s;
   for (int k = 0; k < strlen(str0[i]); ++k)
      {
	if (str0[i][k] == '/')
	  {
	    if (path.find(s) == path.end())
	      {
		count++;
	  path.insert(s);
	  //printf("B:%s\n", s.c_str());
	      }
	  }
	  s += str0[i][k];
      }
	    if (path.find(s) == path.end())
	      {
		count++;
	    path.insert(s);
	    //printf("B:%s\n", s.c_str());
	      }
    }





  printf("Case #%d: %d\n", x, count);
    }
}

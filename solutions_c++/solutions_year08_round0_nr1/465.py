#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int main()
{
  int N,S,Q;
  char engines[100][100];
  string sengines[100];
  int queries[1000];
  char tmp[100];
  map<string, int> index;
  map<string, bool> hit;
  int switches,hits;
  scanf("%d\n",&N);

  for (int n=0; n<N; n++)
    {
      printf("Case #%d: ",n+1);
      switches=0;

      scanf("%d\n",&S);
      for (int i=0; i<S; i++)
	{
	  gets(engines[i]);
	  sengines[i]=engines[i];
	  index[sengines[i]]=i;
	  //	  printf("%s\n",engines[i]);
	}

      scanf("%d\n",&Q);
      //      printf("Q: %d\n",Q);
      for (int i=0; i<Q; i++)
	{
	  gets(tmp);
	  string s(tmp);
	  queries[i]=index[s];
	  //	  printf("%d\n",queries[i]);
	}


      for (int i=0; i<S; i++)
	{
	  hit[sengines[i]]=false;
	}
      hits=0;

      for (int i=0; i<Q; i++)
	{
	  if (!hit[sengines[queries[i]]])
	    {
	      hits++;
	      hit[sengines[queries[i]]]=true;
	      if (hits==S)
		{
		  switches++;
		  for (int j=0; j<S; j++)
		    {
		      hit[sengines[j]]=false;
		    }
		  hit[sengines[queries[i]]]=true;
		  hits=1;
		}
	    }
	}

      printf("%d\n",switches);
    }

  return 0;
}

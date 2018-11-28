#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define IMPO 0x7000000

int canMake(int root, int val, vector<pair<int,int> > &tree)
{

  int ret = IMPO;
  if (root >= tree.size()) ret =  IMPO;

  else if (tree[root].second == -1 && tree[root].first == val) ret =  0;
  else if (tree[root].second == -1 && tree[root].first != val) ret =  IMPO; 
  else if (val == 1 && tree[root].second == 0 && tree[root].first == 0)
    {
      ret =  min(canMake((root+1)*2-1,1,tree),canMake((root+1)*2,1,tree));
    }
  else if (val == 0 && tree[root].second == 0 && tree[root].first == 0)
    {
      ret =  min(canMake((root+1)*2-1,0,tree)+canMake((root+1)*2,0,tree),IMPO); 
    }
  else if (val == 1 && tree[root].second == 0 && tree[root].first == 1)
    {
      ret = min(canMake((root+1)*2-1,1,tree)+canMake((root+1)*2,1,tree),IMPO); 
    }
  else if (val == 0 && tree[root].second == 0 && tree[root].first == 1)
    {
      ret = min(canMake((root+1)*2-1,0,tree),canMake((root+1)*2,0,tree));
    }
  else if (val == 1 && tree[root].second == 1 && tree[root].first == 0)
    {
      ret = min(min(canMake((root+1)*2-1,1,tree),canMake((root+1)*2,1,tree)),
		 min(canMake((root+1)*2-1,1,tree)+canMake((root+1)*2,1,tree),IMPO)+1);
    }
  else if (val == 0 && tree[root].second == 1 && tree[root].first == 0)
    {
      ret =  min(min(canMake((root+1)*2-1,0,tree)+canMake((root+1)*2,0,tree),IMPO),
		 min(canMake((root+1)*2-1,0,tree),canMake((root+1)*2,0,tree))+1);
    }
  else if (val == 1 && tree[root].second == 1 && tree[root].first == 1)
    {
      ret =  min(min(canMake((root+1)*2-1,1,tree)+canMake((root+1)*2,1,tree),IMPO),
		 min(canMake((root+1)*2-1,1,tree),canMake((root+1)*2,1,tree))+1);
    }
  else if (val == 0 && tree[root].second == 1 && tree[root].first == 1)
    {
      ret = min(min(canMake((root+1)*2-1,0,tree),canMake((root+1)*2,0,tree)),
		 min(canMake((root+1)*2-1,0,tree)+canMake((root+1)*2,0,tree),IMPO)+1);
    }
  //  cout << root << " " << val << " " << tree[root].first << " " << tree[root].second << ":" << ret << endl;

  return ret;

}

int main()
{
  int trials;
  cin >> trials;
  int cases = 1;

  while (trials--)
    {
      int m,v;
      cin >> m >> v;
      int c = (m-1)/2;
      vector<pair<int,int> > items;
      for(int i = 0; i < c; i++)
	{
          int a,b;
	  cin >> a >> b;
	  items.push_back(pair<int,int>(a,b));
	  
        }
      c = (m+1)/2;
      for(int i = 0; i < c; i++)
	{
	  int a;
	  cin >> a;
	  items.push_back(pair<int,int>(a,-1));
	}

      int val = canMake(0,v,items);
      //cout << canMake(2,1,items) << endl;
      //      cout << canMake(1,1,items) << endl;
      if (val == 0x7000000)
	cout << "Case #" << cases++ << ": " << "IMPOSSIBLE" << endl;
      else
	cout << "Case #" << cases++ << ": " << val << endl;


    }

}

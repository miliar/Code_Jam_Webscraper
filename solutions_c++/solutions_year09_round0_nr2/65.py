
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>

using namespace std;

int main(int,char**)
{
  int T;
  cin >> T;

  for(int t=0;t<T;++t)
  {
    int H,W;
    cin >> H >> W;
#define AT(Y,X) ((Y)*W+(X))

    vector<pair<int,pair<int,int> > > f;
    vector<int> level(W*H);
    for(int y=0;y<H;++y)
      for(int x=0;x<W;++x)
      {
	int a;
	cin >> a;
	f.push_back(make_pair(a,make_pair(y,x)));
	level[AT(y,x)] = a;
      }
    sort(f.begin(),f.end());

    int label = 0;
    vector<int> field(H*W);
    for(int i=0;i<H*W;++i)
    {
      int a = f[i].first;
      int x = f[i].second.second;
      int y = f[i].second.first;


      const int inf = 100000000;
      int lvs[] = {(y>0?level[AT(y-1,x)]:inf),
		   (x>0?level[AT(y,x-1)]:inf),
		   (x<(W-1)?level[AT(y,x+1)]:inf),
		   (y<(H-1)?level[AT(y+1,x)]:inf)};
      int flow[] = {AT(y-1,x),AT(y,x-1),AT(y,x+1),AT(y+1,x)};
      int* dir = min_element(lvs,lvs+4);
      if(*dir < a)
	field[AT(y,x)] = field[flow[dir-lvs]];
      else
	field[AT(y,x)] = label++;
    }

    char lb = 'a';
    map<int,char> used;
    cout << "Case #" << (t+1) << ":\n";
    for(int j=0;j<H;++j)
    {
      for(int i=0;i<W;++i)
      {
	map<int,char>::iterator itr = used.find(field[AT(j,i)]);
	if(itr==used.end())
	  cout << (used[field[AT(j,i)]] = lb++) << ' ';
	else
	  cout << itr->second << ' ';
      }
      cout << '\n';
    }
  }

  return 0;
}

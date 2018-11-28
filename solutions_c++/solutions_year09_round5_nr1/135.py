#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <deque>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int DR[4] = {-1, 0, 1, 0};
const int DC[4] = {0, 1, 0, -1};

int T, R, C, B, total;
VI positions;
VVI states;
map<VI, int> indexmap;
vector<string> grid;

bool connected[5][5];
bool visited[5];

void visit(int id)
{
  visited[id] = true;
  for (int k = 0; k < B; k++)
    if (!visited[k] && (connected[id][k] || connected[k][id])) visit(k);
}

bool isdangerous(VI boxes)
{
  for (int i = 0; i < B; i++)
    for (int j = 0; j < B; j++)
      connected[i][j] = false;
  for (int i = 0; i < B; i++)
    {
      int ri = boxes[i]/C;
      int ci = boxes[i]%C;
      for (int j = i+1; j < B; j++)
	{
	  int rj = boxes[j]/C;
	  int cj = boxes[j]%C;
	  if ((abs(ri-rj) == 1 && ci == cj) || (abs(ci-cj) == 1 && ri == rj)) 
	    connected[i][j] = true;
	}
    }

  for (int i = 0; i < B; i++) visited[i] = false;
  visit(0);
  for (int i = 0; i < B; i++) 
    if (!visited[i]) return true;
  return false;
}

int putstate(VI p)
{
  sort(p.begin(), p.end());
  if (indexmap.count(p) == 0)
    {
      indexmap[p] = total;
      states.push_back(p);
      total++;
    }
  return indexmap[p];
}

VI getchildren(int cur)
{
  VI children;
  VI boxes = states[cur];

  bool danger = isdangerous(boxes);
  for (int i = 0; i < B; i++)
    for (int d = 0; d < 4; d++)
      {
	int r = boxes[i]/C;
	int c = boxes[i]%C;
	int fr = r+DR[d];
	int fc = c+DC[d];
	int br = r-DR[d];
	int bc = c-DC[d];
	bool ok = true;
	for (int j = 0; j < B; j++)
	  if (boxes[j] == br*C+bc) ok = false;
	if (!ok) continue;
	if (fr >= 0 && fr < R && fc >= 0 && fc < C && grid[fr][fc] != '#' && 
	    br >= 0 && br < R && bc >= 0 && bc < C && grid[br][bc] != '#')
	  {
	    VI newboxes(boxes);
	    newboxes[i] = fr*C+fc;
	    bool ok = true;
	    for (int j = 0; j < B; j++)
	      if (j != i && newboxes[j] == newboxes[i]) ok = false;
	    if (!ok) continue;
	    if (!danger || !isdangerous(newboxes))
	      {
		sort(newboxes.begin(), newboxes.end());
		children.push_back(putstate(newboxes));
	      }
	  }
      }
  return children;
}
	    	    
int solve()
{
  deque<int> q;
  vector<int> moves(1000000);
  
  VI initialposition;
  VI finalposition;
  for (int i = 0; i < R; i++)
    for (int j = 0; j < C; j++)
      {
	if (grid[i][j] == 'o' || grid[i][j] == 'w') initialposition.push_back(i*C+j);
	if (grid[i][j] == 'x' || grid[i][j] == 'w') finalposition.push_back(i*C+j);
      }
  int initial = putstate(initialposition);
  int final = putstate(finalposition);

  q.push_back(initial);
  for (int i = 0; i < 1000000; i++) moves[i] = (int)1e9;
  moves[initial] = 0;

  while (!q.empty() && moves[final] == (int)1e9)
    {
      int cur = q.front();
      q.pop_front();

      VI children = getchildren(cur);
      for (int i = 0; i < children.size(); i++)
	if (moves[children[i]] == (int)1e9)
	  {
	    q.push_back(children[i]);
	    moves[children[i]] = moves[cur]+1;
	  }
    }

  if (moves[final] == (int)1e9)
    return -1;
  else
    return moves[final];
}

int main()
{
  cin >> T;

  for (int casenum = 0; casenum < T; casenum++)
    {
      cin >> R >> C;
      grid.resize(R);
      B = 0;
      for (int i = 0; i < R; i++)
	{
	  cin >> grid[i];
	  for (int j = 0; j < C; j++)
	    if (grid[i][j] == 'o' || grid[i][j] == 'w') B++;
	}

      total = 0;
      states.clear();
      indexmap.clear();

      cout << "Case #" << casenum+1 << ": " << solve() << endl;
      if (total >= 1000000)
	{
	  cout << "WRONG" << endl;
	  return 0;
	}
      //cout << "total=" << total << endl;
    }
  return 0;
}

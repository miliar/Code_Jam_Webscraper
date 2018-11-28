#include<iostream>
#include<cstring>
using namespace std;

const int maxn = 100;
const int maxh = 100;
const int maxw = 100;
const int mov[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int n;
int h, w;
int mp[maxh+3][maxw+3];
int dset[maxh*maxw+3];
int label[maxh*maxw+3];

void init()
{
  cin >> h >> w;
  for (int i = 0; i < h; ++i) 
    for (int j = 0; j < w; ++j) 
      cin >> mp[i][j];
}

int getfather(int a) 
{
  int t = a;
  int t1;
  int f;
  while (dset[t] != -1) t = dset[t];
  f = t;
  t = a;
  while (dset[t] != -1) {
    t1 = dset[t];
    dset[t] = f;
    t = t1;
  }
}

void merge(int a, int b)
{
  int x = getfather(a);
  int y = getfather(b);
  if (x != y)
    dset[x] = y;
}

int lb(int a, int &cur)
{
  int x = getfather(a);
  if (label[x] == -1) {
    ++cur;
    label[x] = cur;
    label[a] = cur;
  } else {
    label[a] = label[x];
  }
  return label[a];
}

void proc()
{
  int ed;
  memset(dset, 255, sizeof(dset));
  memset(label, 255, sizeof(label));
  for (int i = 0; i < h; ++i) 
    for(int j = 0; j < w; ++j) {
      ed = -1;
      for (int t = 0; t < 4; ++t) 
	if ((i+mov[t][0] >= 0) && (i+mov[t][0] < h)
	    && (j+mov[t][1] >= 0) && (j+mov[t][1] < w)){
	if (mp[i+mov[t][0]][j+mov[t][1]] < mp[i][j]) {
	  if (ed == -1) {
	    ed = (i+mov[t][0])*w+j+mov[t][1];
	  } else if (mp[ed/w][ed%w] > mp[i+mov[t][0]][j+mov[t][1]]) {
	    ed = (i+mov[t][0])*w+j+mov[t][1];
	  }
	}
	}
      if (ed != -1) {
	merge(i*w+j, ed);
      }
    }
  int cur = -1;
  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      if (j != 0) cout << ' ';
      cout << char('a'+lb(i*w+j, cur));
    }
    cout << endl;
  }
}

int main()
{
  cin >> n;
  for (int i = 0; i < n; ++i) {
    init();
    cout << "Case #" << i+1<< ":" << endl;
    proc();
  }
}

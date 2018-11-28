#include <iostream>
#include <map>

class disjoint {
  disjoint* father;
  int count;
public:
  char name;
  disjoint* get() {
    if(father == this) return this;
    else return father = father->get();
  }

  void join(disjoint& other) {
    if(this!=father || other.father!=&other)
      get()->join(*other.get());
    else
      if(other.count > count) {
	father = &other;
	other.count += count;
      } else {
	other.father = this;
	count += other.count;
      }
  }

  void reset() {
    count = 1;
    father = this;
    name = 0;
  }

  disjoint() : father(this), count(1), name(0) {}
private:
  disjoint(disjoint&);
  disjoint(const disjoint&);
  disjoint operator=(const disjoint&);
};

const int maxh = 100;
const int maxw = 100;

int h, w;
disjoint grid[maxh][maxw];
int height[maxh][maxw];

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int tcase=1;tcase<=T;tcase++) {
    cout << "Case #" << tcase << ":\n";
    cin >> h >> w;
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++){
	grid[i][j].reset();
	cin >> height[i][j];
      }
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++){
	int basin = height[i][j];
	int x = i, y = j;
	if(i > 0 && height[i-1][j] < basin) {
	  basin = height[i-1][j];
	  x = i - 1;
	  y = j;
	}
	if(j > 0 && height[i][j-1] < basin) {
	  basin = height[i][j-1];
	  x = i;
	  y = j - 1;
	}
	if(j + 1 < w && height[i][j+1] < basin) {
	  basin = height[i][j+1];
	  x = i;
	  y = j + 1;
	}
	if(i + 1 < h && height[i+1][j] < basin) {
	  basin = height[i+1][j];
	  x = i + 1;
	  y = j;
	}
	//cerr << "(" << i << ", " << j << ")=>(" << x << ", " << y <<")\n";
	if(i != x || j != y)
	  grid[i][j].join(grid[x][y]);
      }
    char cur = 'a';
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	if(!grid[i][j].get()->name) grid[i][j].get()->name = cur++;
	cout << grid[i][j].get()->name;
	if(j!=w-1) cout << ' ';
      }
      cout << '\n';
    }
  }
}

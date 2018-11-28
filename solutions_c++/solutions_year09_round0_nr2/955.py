
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, s) for(__typeof((s).begin() i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) (s).begin(), (s).end()

#define N 10000

vector<int> data(N, -1);

int rootOf(int a) {
  return data[a] < 0 ? a : (data[a] = rootOf(data[a]));
}

void unify(int a, int b) {
  int ra = rootOf(a);
  int rb = rootOf(b);
  if(ra != rb){
    if(data[ra] > data[rb])
      swap(ra, rb);
    data[ra] += data[rb];
    data[rb] = ra;
  }
}


int field[100][100];
vector<char> assign;


int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases){
    int w, h;
    scanf("%d%d", &h, &w);
    data = vector<int>(h * w, -1);
    assign = vector<char>(h * w, '\0');

    REP(i, h) REP(j, w)
      scanf("%d", &field[i][j]);
    
    REP(i, h){
      REP(j, w){
	int root = i*w + j;
	int height = field[i][j];
	if(i > 0 && field[i-1][j] < height){
	  root = (i-1)*w + j;
	  height = field[i-1][j];
	}

	if(j > 0 && field[i][j-1] < height){
	  root = i*w + j-1;
	  height = field[i][j-1];
	}

	if(j < w - 1 && field[i][j+1] < height){
	  root = i*w + j+1;
	  height = field[i][j+1];
	}

	if(i < h-1 && field[i+1][j] < height){
	  root = (i+1)*w + j;
	  height = field[i+1][j];
	}
	
	unify(i*w+j, root);
      }
    }
    
    printf("Case #%d:\n", iCase+1);
    char cur = 'a';
    REP(i, h){
      REP(j, w){
	int id = i*w+j;
	int root = rootOf(id);
	if(assign[root] == '\0')
	  assign[root] = cur++;
	printf("%c%c", assign[root], j < w-1 ? ' ' : '\n');
      }
    }
  }
  
  return 0;
}

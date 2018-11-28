#include <iostream>
#include <set>
#include <math.h>

using namespace std;

int p[1010], rank[1010];

void make_set(int x){
  p[x] = x;
  rank[x] = 0;
}

void link(int x, int y){
  if (rank[x] > rank[y]){
    p[y] = x;
  }else{
    p[x] = y;
    if (rank[x] == rank[y]){
      rank[y]++;
    }
  }
}

int find_set(int x){
  if (x != p[x]){
    p[x] = find_set(p[x]);
  }
  return p[x];
}

void make_union(int x, int y){
  link(find_set(x), find_set(y));
}

void initset(int i){ p[i] = i; }
int findSet(int i){ return (p[i]==i)? i : (p[i] = findSet(p[i])); }
void merge(int i, int j){ p[findSet(i)] = findSet(j); }
int sameSet(int i, int j){ return findSet(i)==findSet(j); }


bool share(int a, int b, int p){
  if (b < a) swap(a, b);

  long i;                 /* counter */
  long c;                 /* remaining product to factor */
  c = a;
  while ((c % 2) == 0) {
    if (2 >= p && (b%2 == 0)) return true;
    c = c / 2;
  }
  i = 3;
  while (i <= (sqrt(c)+1)) {
    if ((c % i) == 0) {
      if (i >= p && (b%i == 0)) return true;
      c = c / i;
    }
    else
      i = i + 2;
  }
  if (c > 1) return (c >= p && (b%c == 0));
  return false;
}

int main(){
  int C;
  cin >> C;
  for (int c=1; c<=C; ++c){
    cout << "Case #" << c << ": ";
    int a, b, p;
    cin >> a >> b >> p;
    for (int i=a; i<=b; ++i){
      make_set(i);
      //initSet(i);
    }
    for (int i=a; i<=b; ++i){
      for (int j=i+1; j<=b; ++j){
        //printf("share (%d, %d, %d) -> ", i, j, p);
        if (share(i, j, p)){
          make_union(i, j);
          //printf("true");
        }
        //printf("\n");
      }
    }
    set<int> counted;
    for (int i=a; i<=b; ++i){
      //printf("find_set(%d) = %d\n", i, find_set(i));
      counted.insert(find_set(i));
    }
    cout << counted.size() << endl;
  }
  return 0;
}

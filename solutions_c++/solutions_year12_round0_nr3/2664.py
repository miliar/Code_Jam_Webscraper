#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

typedef long long ll;


int pt[10];

int inverte(int n, int i, int d)
{
  int x = (n % pt[i]);
  n /= pt[i];
  n += x * pt[d-i];
  return n;  
}

int main()
{
  int casos;
  scanf("%d", &casos);
  for(int h = 1; h <= casos; h++){
    ll conta = 0LL;
    int a, b;
    scanf(" %d %d", &a, &b);

    pt[0] = 1;
    for(int i = 1; i < 10; i++)
      pt[i] = 10 * pt[i-1];

    int d = 1;
    while(a >= pt[d])
      d++;

    for(int n = a; n < b; n++){
      set<int> S;
      for(int i = 1; i < d; i++){
	int m = inverte(n, i, d);
	if(n < m && m <= b){
	  S.insert(m);
	}
      }
      conta += S.size();
    }

    printf("Case #%d: %lld\n", h, conta);
  }
  return 0;
}

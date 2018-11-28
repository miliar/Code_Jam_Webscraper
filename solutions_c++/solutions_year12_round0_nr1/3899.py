#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define ff first
#define ss second
#define rep(i, n) for(LL i = 0; i < (LL)n; i++)
#define INF (1 << 30)
#define debug(x) cout << x << endl

int main()
{
  int t = 0;
  char s;
  rep(i, 3) {
    s = getchar();
    if (s == '\n') break;
    t = t * 10 + s - '0'; 
  }
  rep(j, t) {
    printf("Case #%d: ", (int)j + 1);
    while (1) { 
      s = getchar();
      if (s == '\n') {
	cout << endl;
	break;
      }
      switch (s) {
      case 'y' : putchar('a'); break;
      case 'n' : putchar('b'); break;
      case 'f' : putchar('c'); break;
      case 'i' : putchar('d'); break;
      case 'c' : putchar('e'); break;
      case 'w' : putchar('f'); break;
      case 'l' : putchar('g'); break;
      case 'b' : putchar('h'); break;
      case 'k' : putchar('i'); break;
      case 'u' : putchar('j'); break;
      case 'o' : putchar('k'); break;
      case 'm' : putchar('l'); break;
      case 'x' : putchar('m'); break;
      case 's' : putchar('n'); break;
      case 'e' : putchar('o'); break;
      case 'v' : putchar('p'); break;
      case 'z' : putchar('q'); break;
      case 'p' : putchar('r'); break;
      case 'd' : putchar('s'); break;
      case 'r' : putchar('t'); break;
      case 'j' : putchar('u'); break;
      case 'g' : putchar('v'); break;
      case 't' : putchar('w'); break;
      case 'h' : putchar('x'); break;
      case 'a' : putchar('y'); break;
      case 'q' : putchar('z'); break;
      case ' ' : putchar(' '); break;
      }
    }
  }
  return 0;
}

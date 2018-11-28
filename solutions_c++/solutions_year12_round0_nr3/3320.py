#include <algorithm>
#include <cstdio>
#include <set>
#include <sstream>
#include <string>

using namespace std;

// Thanks ACRush!
template<class T> string to_string(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int to_int(string s){int r=0;istringstream sin(s);sin>>r;return r;}

int tc;

int rotate(int x, int n)
{
	string s = to_string(x);
	reverse(s.begin(), s.begin() + n);
	reverse(s.begin() + n, s.end());
	reverse(s.begin(), s.end());
	return to_int(s);
}

void process(int n)
{
	int a, b;

	scanf("%d %d", &a, &b);
	int ans = 0;

	for (int i = a; i <= b; i++) {
		set<int> done;
		for (int j = 1; j < to_string(i).length(); j++) {
			int rot = rotate(i, j);
			if (rot != i && rot >= a && rot <= b && to_string(rot).length() == to_string(i).length()
			    && !done.count(rot)) {
				done.insert(rot);
				ans++;
			}
		}
	}

	ans >>= 1;

	printf("Case #%d: %d\n", n, ans);
		
}

int main()
{
	scanf("%d", &tc);
	
	for (int i = 0; i < tc; i++)
		process(i + 1);		
		
	return 0;
}

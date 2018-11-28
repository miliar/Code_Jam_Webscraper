#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

using namespace std;


// WRITE ALL CODE BELOW THIS

void func() {
	int n, m;
	scanf("%d%d", &n, &m);
	char tmp[120];
	vector<string> x;
	int res = 0;
	for (int i = 0; i < n; i++) {
		scanf("%s", tmp);
		x.push_back(string(tmp));
	}
	for (int i = 0; i < m; i++) {
		scanf("%s", tmp);
		string p = tmp;
		int max = 0;
		for (int j = 0; j < n; j++)
			if (p.find(x[j]) == 0) {
				if (p.length() > x[j].length())
					if (p[x[j].length()] != '/')
						continue;
				if (x[j].length() > max)
					max = x[j].length();
			}
		string basic = p.substr(0, max);
		p = p.substr(max);
		while (p.length() > 0) {
			int l;
			if (p.find_last_of('/') == 0)
				l = p.length();
			else
				l = p.find_first_of('/', 1);
			basic += p.substr(0, l);
			x.push_back(string(basic));
			n++;
			p = p.substr(l);
			res++;
		}
	}
	cout << " " << res << endl;
}


int main() {
  freopen("in.in", "r", stdin);
  freopen("output.out", "w", stdout);

  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
  	cout << "Case #" << i << ":";
  	func();
  }

  fclose(stdin);
  fclose(stdout);
}

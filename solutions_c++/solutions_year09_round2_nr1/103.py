#include <string>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

struct node
{
	string f;
	double p;
	int left, right;
} a[100000];
string input;
char buf[1000];
int num;
set<string> s;

void go(int n, int &ind)
{
	string tmp;
	++ind;
	while (input[ind] != '(' && input[ind] != ')')
		tmp += input[ind++];
	stringstream ss(tmp);
	ss >> a[n].p;
	ss >> a[n].f;
	if (input[ind] == ')')
		a[n].left = a[n].right = -1;
	else {
		a[n].left = num++;
		go(num - 1, ind);
		a[n].right = num++;
		while (input[ind] != '(')
			++ind;
		go(num - 1, ind);
	}
}

void go2(int n, double &res)
{
	res *= a[n].p;
	if (a[n].left == -1)
		return;
	if (s.count(a[n].f))
		go2(a[n].left, res);
	else
		go2(a[n].right, res);
}

int main()
{
	int T, L, A;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &L);
		gets(buf);
		input.clear();
		while (L--) {
			gets(buf);
			input += buf;
		}
		num = 1;
		int i = 0;
		while (input[i] != '(')
			++i;
		go(0, i);
		scanf("%d", &A);
		printf("Case #%d:\n", t);
		while (A--) {
			double res = 1;
			s.clear();
			scanf("%*s %d", &L);
			while (L--) {
				scanf("%s", buf);
				s.insert(buf);
			}
			go2(0, res);
			printf("%.7lf\n", res);
		}
	}
	return 0;
}

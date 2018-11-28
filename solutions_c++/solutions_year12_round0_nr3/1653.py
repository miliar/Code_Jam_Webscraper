#include <iostream>
#include <set>
using namespace std;


int main(int ac, char* av[])
{
	int N; cin >> N;
	for (int x=1;x<=N;x++) {
		int a, b;
		cin >> a >> b;
		int r = 0;
		int d = 1;
		int p=10;
		for (; d<10; d++, p=p*10) {
			if (p > a) {
				break;
			}
		}
		p /= 10;
		//cout << "p:" <<p << endl;
		for (int i = a; i <= b; i++) {
			set <int> sol;
			for (int j=1, s=i; j<d; j++) {
				int f = s/p;
				s = (s%p)*10 + f;
				if (s > i && s <= b) {
					sol.insert(s);
				}
			}
			r += sol.size();
		}
		cout << "Case #" << x << ": " << r << endl;
	}
	return 0;
}
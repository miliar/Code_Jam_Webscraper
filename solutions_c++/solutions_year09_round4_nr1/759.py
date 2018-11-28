#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

int *origin;
int *cur;

void doit(int now)
{
	int n;
	cin >> n;
	string line;
	for (int i = 0; i < n; i++) {
		cin >> line;
		int val = 0;
		for (int j = 0; j < n; j++) {
			if (line[j] == '1')
				val = j;
		}
		origin[i] = val;
	}
	int move = 0;
	for (int i = 0; i < n; i++) {
		//cout << "--> ";
		//for (int j = 0; j < n; j++)
		//	cout << origin[j] << " ";
		//cout << endl;
		// find first i
		int tmp = 0;
		for (int j = i; j < n; j++) {
			//cout << origin[j] << " " << i << endl;
			if (origin[j] <= i) {
				for (int k = j; k > i; k--) {
					int a = origin[k - 1];
					origin[k - 1] = origin[k];
					origin[k] = a;
					tmp++;
					//cout << "tmp " << tmp << endl;
				}
				move += tmp;
				//cout << "move " << move << endl;
				break;
			}
		}
	}
	printf("Case #%d: %d\n", now, move);
}

int main()
{
	origin = new int[100];
	cur = new int[100];

	int c;
	cin >> c;
	for (int i = 1; i <= c; i++)
		doit(i);
}

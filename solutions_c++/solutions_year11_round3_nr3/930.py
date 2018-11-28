#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

#define min(a, b) (((a)<(b))?(a):(b))
#define max(a, b) (((a)>(b))?(a):(b))
#define abs(a) ((a)>(0)?(a):(-(a)))

using namespace std;


int mas[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t;

	cin >> t;

	for(int ii = 0; ii < t; ++ii){
		int l, r;
		cin >> n >> l >> r;
		for(int i = 0; i < n; ++i)
			cin >> mas[i];
		bool ans = false;
		int anss;
		for(int i = l; i <= r; ++i){
			ans = true;
			for(int j = 0; j < n; ++j){
				if (((mas[j] % i) != 0) && ((i % mas[j]) != 0)){
					ans = false;
					break;
				}

			}
			if (ans){
				anss = i;
				break;
			}
		}

		cout << "Case #" << ii + 1 << ':'<< ' ';
		if (ans)
			cout << anss << endl;
		else
			cout << "NO" << endl;

	}



	return 0;
}
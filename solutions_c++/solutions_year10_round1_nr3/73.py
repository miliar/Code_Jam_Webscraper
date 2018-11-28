#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int first[1000002];
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	first[1] = 1;
	first[2] = 2;
	int fre = 3, t;
	for (int i=2; i<=1000000; i++){
		if (fre == 1000000)
			break;
		for (; fre - first[i] < i && fre <= 1000000; fre++){
			first[fre] = i;
		}
	}
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		long long ret = (long long)(a2 - a1 + 1) * (b2 - b1 + 1);
		for (int i=a1; i<=a2; i++){
			int beg = max(b1, first[i]), last = min(b2, first[i] + i - 1);
			if (beg <= last){
				ret -= last - beg + 1;
			}
		}
		cout << ret << endl;
	}
	return 0;
}
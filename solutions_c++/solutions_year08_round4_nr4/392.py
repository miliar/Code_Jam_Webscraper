#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
const int MAXN = 5;
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt != cases; ++tt){
		int k;
		cin >> k;
		string str; cin >> str;
		int order[MAXN];
		for (int i = 0; i != k; ++i) order[i] = i;
		int best = 9999;
		do{
			string temp = str;
			for (int i = 0; i != str.size() / k; ++i){
				int x = i * k;
				for (int j = 0; j != k; ++j) temp[x + j] = str[x + order[j]];
			}
			//cout << temp << endl;
			char old = ' ';
			int count = 0;
			for (int i = 0; i != temp.size(); ++i){
				if (temp[i] != old){
					++count; old = temp[i];
				}
			}
			if (count < best) best = count;
		} while (next_permutation(order, order + k));
		printf("Case #%d: %d\n", tt + 1, best);
	}
	return 0;
}
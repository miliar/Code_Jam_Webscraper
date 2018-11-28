#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

bool there[20][26];
string dict[10000];
int L, D, N;

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	cin >> L >> D >> N;
	for(int i = 0 ; i < D ; i++)
		cin >> dict[i];

	for(int i = 0 ; i < N ; i++){

		memset(there, 0, sizeof there);
		string str; cin >> str;
		int k = 0;
		for(int j = 0 ; j < str.size() ; j++){
			if(islower(str[j])){
				there[k][str[j]-'a'] = true;
				k++;
				continue;
			}
			j++;
			while(islower(str[j])){
				there[k][str[j]-'a'] = true;
				j++;
			}
			k++;
		}
		assert(k == L);

		int res = 0;
		for(int j = 0 ; j < D ; j++){
			int k;
			for(k = 0 ; k < L ; k++)
				if(!there[k][dict[j][k]-'a'])
					break;
			if(k == L)
				res++;
		}

		cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}

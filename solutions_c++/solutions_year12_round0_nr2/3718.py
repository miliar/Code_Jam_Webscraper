#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T;
	cin >> T;
	cin.ignore();
	int N, S, p, yes, maybe, low;
	float ave, diff;
	for(int t = 0; t < T; t++){
		cin >> N;
		cin >> S;
		cin >> p;
		yes = 0;
		maybe = 0;
		int scores[N];
		for(int i = 0; i < N; i++)
			cin >> scores[i];
		for(int i = 0; i < N; i++){
			ave = (float)scores[i]/3;
			diff = ave - (float)p;
			if(diff > -1)
				yes++;
			else{
				low = 2*(p-2);
				if(low < 0)
					low = 0;
				if(p + low <= scores[i])
					maybe++;
			}
		}
		if(maybe > S)
			maybe = S;
		cout << "Case #" << t+1 << ": " << yes+maybe << endl;
	}
	return 0;
}

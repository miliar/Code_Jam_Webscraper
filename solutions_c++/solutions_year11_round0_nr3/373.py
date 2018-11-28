#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;

struct SCOPE
{
	int N;
	int run(int Case)
	{
		cin >> N;
		int m;
		int x=0;
		int sum=0;
		for(int i=0;i<N;i++){
			int c;
			cin>>c;
			if(i==0){
				m=c;
			}
			else {
				m=min(c,m);
			}
			x^=c;
			sum+=c;
		}
		cout << "Case #" << Case << ": ";
		if(x==0){
			cout << sum-m << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
		return 0;
	}
};

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		SCOPE* pSCOPE = new SCOPE();
		if(pSCOPE->run(t)){
			return 0;
		}
		delete pSCOPE;
	}
}

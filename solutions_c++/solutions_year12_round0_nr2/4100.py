#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

void runCase()
{
	int N,S,p,t;
	cin >> N >> S >> p;
	
	vector<int> m1(N),m2(N);
	
	int res = 0;
	for(int i =0; i < N; i++) {
		cin>>t;
		m1[i] = (t+2)/3;
		if(t<=1) {m2[i] = -1;}
		else {m2[i] = t/3+1;if(t%3==2) m2[i]+=1;}
	}
	
	for(int i = 0; i < N; i++) {
		if(m1[i]>=p) {
			res++;
			m1[i] = -1;
		}
	}
	
	for(int i = 0; i < N && S; i++) {
		if(m1[i] != -1) {
			if(m2[i] >= p) {
				res++;
				S--;
			}
		}
	}
	
	cout << res << endl;
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();
	
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}

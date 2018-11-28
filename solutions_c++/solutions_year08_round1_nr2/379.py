
#include <iostream>
#include <vector>
typedef long long LL;
using namespace std;
int bpop(int n){
	int t = 0;
	while(n){
		t += n&1;
		n >>= 1;
	}
	return t;
}
int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int n,m;
		cin >> n >> m;
		vector<int> unmask(m);
		vector<int> malted(m, n);
		for(int i=0; i<m; i++){
			int t;
			cin >> t;
			for(int j=0; j<t; j++){
				int a,b;
				cin >> a >> b;
				a--;
				if(b)
					malted[i] = a;
				else
					unmask[i] |= 1<<a;
			}
		}
		int ans = -1;
		for(int i=0; i<(1<<n); i++){
			bool ok = true;
			for(int j=0; j<m; j++)
				ok &= (i&(1<<malted[j])) || ((~i)&unmask[j]);
			if(ok && (ans == -1 || bpop(i)<bpop(ans)))
				ans = i;
		}
		cout << "Case #"<<case_no<<":";
		if(ans == -1){
			cout << " IMPOSSIBLE";
		}else{
			for(int i=0; i<n; i++)
				cout << " " << ((ans >> i)&1);
		}
		cout << endl;
	}
	return 0;
}

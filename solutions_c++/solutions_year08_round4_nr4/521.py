#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		cout << "Case #" << ts << ": ";
		int M;
		int k;
		string S;
		cin >> k >> S;
		vector<int> v(k);
		fu(i,0,k) v[i]=i;
		int bst=1000000;
		do {
			string T=S;
			fu(i,0,S.size()) T[i]=S[k*(i/k) + v[i%k]];
			int blk=1;
			fu(i,1,S.size()) if(T[i]!=T[i-1]) blk++;
			bst<?=blk;
		} while(next_permutation(v.begin(),v.end()));
		cout << bst << endl;
	}
}

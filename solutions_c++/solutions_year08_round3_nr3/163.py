#include <iostream>

using namespace std;

const int nmax = 1005;
const long long mod = 1000000007;

long long f[nmax][nmax],a[nmax],b[nmax];

long long rec(int last,int cur,int n){
	if (f[last][cur] > -1)
		return f[last][cur];

	if (cur == n)
		return 1;

	long long ans = 0;

	if (b[cur] > b[last]) 
		ans = (ans+ rec(cur,cur+1,n)) % mod;

	ans = (ans + rec(last,cur+1,n)) % mod;
	f[last][cur] = ans;
	return ans;	
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){

		int n,m,X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;

		for (int i = 0;i < m; ++i) cin >> a[i];

		for (int i = 0;i < n; ++i){
			b[i] = a[i % m];
			a[i % m] = (X * a[i % m] + (long long)Y * (i+1)) % Z;
		}

		memset(f,-1,sizeof(f));

		long long sum = 0;

		for (int i = 0;i < n; ++i)
			sum = (sum + rec(i,i+1,n)) % mod;
		
		cout << "Case #"<<t<<": "<<sum<<endl;	
	}

	return 0;
}
#include <iostream>
#include <vector>

#define X first
#define Y second
#define show(x) cerr<<#x<<'='<<x<<endl
using namespace std;
typedef pair<int, int> pii;

int n, p, s, t, ans;
vector<int> v1;
vector<pii> v2;
int main() {
	cin>>t;
	for (int i=0; i<t; ++i) {
		v1.clear();
		v2.clear();
		ans=0;
		cin>>n>>s>>p;
		if (p==0) {
			for (int j=0; j<n; ++j) {
				int x;
				cin>>x;
			}
			cout<<"Case #"<<i+1<<": "<<n<<endl;
			continue;
		}
		for (int j=0; j<n; ++j) {
			int x;
			cin>>x;
			if (x==0)
				continue;
			if (x%3==0) 
				v2.push_back(pii(x/3, x/3+1));
			else if (x%3==1)
				v1.push_back(x);
			else
				v2.push_back(pii(x/3+1, x/3+2));
		}
		for (int j=0; j<(int) v2.size(); ++j)
			if (v2[j].Y==p&&s) {
				s--;
				ans++;
			}
			else if (v2[j].X>=p)
				ans++;
		for (int j=0; j<(int) v1.size(); ++j)
			if (v1[j]/3+1>=p)
				ans++;
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}

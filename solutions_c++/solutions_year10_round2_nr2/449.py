#include <iostream>
#include <vector>

using namespace std;

vector<long long> x;
vector<long long> v;		
long long b,t;
int n,k;

bool good(int i){
	if (i >= x.size()) return true;
	return (b - x[i] <= t * v[i]);
}

void _swap(int i, vector<long long> & z){
	long long buf = z[i];
	z[i] = z[i + 1];
	z[i + 1] = buf;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int ttt; //scanf("%d",&t);
	cin >> ttt;
	for (int tt = 0; tt < ttt; tt++){
		x.clear(); v.clear();
		cin >> n >> k >> b >> t;
		for (int j = 0; j < n; j++)
		{
			long long xx; cin >> xx; x.push_back(xx);
		}

		for (int j = 0; j < n; j++)
		{
			long long vv; cin >> vv; v.push_back(vv);
		}
	
		int ans = 0;
		int now = 0;
		for (int i = n - 1; i >= 0; i--){
			if (now >= k) break;
			if (!good(i)) continue;
			if (good(i)){
				int j = i;
				while (!good(j + 1)){
					ans++; _swap(j,x); _swap(j, v);
					j++;
				}				
			}
			now++;
		}
		printf("Case #%d: ", tt + 1);
		if (now < k) printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}

	return 0;
}
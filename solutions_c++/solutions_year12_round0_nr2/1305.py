#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int t , n , s , p , t_case , i; 

int solve(int n, int s, int p, vector<int> v) {
	
	int i , ans = 0;
	vector <int> maxx(n);
	vector <bool> can_up(n , false);
	
	sort(v.begin(), v.end());
	
	for(i = 0; i < n; ++i) {
		if(v[i] % 3 == 0) {
			maxx[i] = v[i] / 3;
			if(v[i] >= 2)
				can_up[i] = true;
		}
		
		if(v[i] % 3 == 1) 
			maxx[i] = v[i] / 3 + 1;
		
		if(v[i] % 3 == 2) {
			maxx[i] = v[i] / 3 + 1;
			if(v[i] >= 2)
				can_up[i] = true;
		}
	}
	
	for(i = 0 ; i < n ; ++i) {
		if(maxx[i] >= p)
			ans++;
		else if(maxx[i] == p - 1 && can_up[i] && s) {
			ans++;
			s--;
		}
	}
	
	return ans;
			
}

int main()
{
	freopen("dancing.in","r",stdin);
	freopen("dancing.out","w",stdout);
	
	scanf("%d",&t);
	
	for(t_case = 1; t_case <= t; ++t_case) {
		
		scanf("%d %d %d",&n,&s,&p);
		
		vector <int> sum(n);
		
		for(i = 0; i < n; ++i)
			scanf("%d",&sum[i]);
		
		printf("Case #%d: %d\n", t_case, solve(n , s , p , sum));
	}
	
return 0;
}
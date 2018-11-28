#include<iostream>
#include<cstring>
#include<map>
using namespace std;
typedef map<string, int>  MAKE;
MAKE mp;

bool mark[120];
int ans,sum,a[1200];

void Color(int k){
	if(mark[k])return ;
	sum++;
	mark[k] = 1;
}

int main()
{
	int i,j,k,t,n,s,q;
	char str[1002];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &n);
	for(t = 1; t <= n; t++){
		scanf("%d", &s);
		gets(str);
		mp.clear();
		for(i = 1; i <= s; i++){
			gets(str);
			mp[string(str)] = i;
		}
		scanf("%d", &q);
		MAKE::iterator pos;
		gets(str);
		for(i = 1; i <= q; i++){
			gets(str);
			pos = mp.find(string(str));
			if(pos != mp.end())
				a[i] = (*pos).second;
		}
		ans = sum = 0;
		for(i = 1; i <= q; i = j){
			sum = 0;
			memset(mark, 0, sizeof(mark));
			for(j = i; j <= q; j++){
				Color(a[j]);
				if(sum == s){
					break;
				}
			}
			ans++;
		}
		if(ans == 0)ans++;
		printf("Case #%d: %d\n", t,ans-1);
	}
	return 0;
}
			

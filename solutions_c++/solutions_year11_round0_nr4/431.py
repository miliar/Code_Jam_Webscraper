#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

#define CASE_MAX 1001
double table[CASE_MAX][CASE_MAX] = {0.0};

double cnm(int n, int m)
{
	double res = 1.0;
	for(int i = 0; i < m; i++) {
		res *= 1.0*(n-i);
		res /= 1.0*(i+1);
	}
	return res;
}

double calc(int cnt)
{
	static map<int,double> mask;
	mask[0] = 0.0;
	mask[1] = 0.0;
	mask[2] = 2.0;
//	mask[3] = 3.0;
	
	if(mask.count(cnt) != 0) {
		return mask[cnt];
	}
	
	double res = 0.0;
	double all = 0.0;
	double sub = 0.0;
	
	vector<int> ring(cnt);
	vector<bool> flag;
	for(int i = 0; i < cnt; i++) {
		ring[i] = i;
	}
	
	do
	{
		double need = 0.0;
		bool sublevel = true;
		flag = vector<bool>(cnt,true);
		while(1)
		{
			bool have = false;
			int start;
			
			for(int i = 0; i < cnt; i++) {
				if(flag[i]) {
					have = true;
					start = i;
					break;
				}
			}
			
			if(!have) break;
			
			int next = start;
			int count = 0;
			while(1) {
				flag[next] = 0;
				next = ring[next];
				count ++;
				if(next == start) {
					break;
				}
			}
			if(cnt > count) need += calc(count);
			else {
				sublevel = false;
				need = 0.0;
				break;
			}
		}
		if(sublevel) {
			res += need;
			sub ++;
		}
		all++;
	}while(next_permutation(ring.begin(),ring.end()));
	
	res /= sub;
	
	res += all/sub;
	
	mask[cnt] = res;
	return res;
	
	for(int i = 1; i <= cnt/2; i++) {
		res += cnm(cnt,i)*(calc(cnt-i)+calc(i));
		all += cnm(cnt,i);
	}
	res /= all+1.0;
	
	res += 1.0*cnt/(cnt-1);
	
	mask[cnt] = res;
	return res;
}

void runCase()
{
	int n;
	scanf("%d",&n);
	
	int permu[CASE_MAX];
	int flag[CASE_MAX];
	for(int i = 1; i <= n; i++) {
		scanf("%d",&permu[i]);
		flag[i] = 1;
	}
	
	double res = 0.0;
	while(1)
	{
		bool have = false;
		int start;
		
		for(int i = 1; i <= n; i++) {
			if(flag[i]) {
				have = true;
				start = i;
				break;
			}
		}
		
		if(!have) break;
		
		int next = start;
		int count = 0;
		while(1) {
			flag[next] = 0;
			next = permu[next];
			count ++;
			if(next == start) {
				break;
			}
		}
		// res += calc(count);
		if(count != 1) res += count;
	}
	
	printf("%lf \n", res);
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

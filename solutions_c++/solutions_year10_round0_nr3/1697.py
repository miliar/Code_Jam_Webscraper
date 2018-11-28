#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
FILE* fin = fopen("C-large.in", "r");
FILE* fout = fopen("C-large.out", "w");
int main()
{
	__int64 g[1001], r, k, n, Case, t, i;
	vector<__int64> sum;
	vector<__int64> value;
	//scanf("%d", &Case);
	fscanf(fin,"%I64d", &Case);
	for(t = 1; t <= Case; t++){
	//	scanf("%d%d%d", &r, &k, &n);
		fscanf(fin, "%I64d%I64d%I64d", &r, &k, &n);
		sum.clear();
		value.clear();
		for(i = 0; i < n; i++)
			//scanf("%d", &g[i]);
			fscanf(fin, "%I64d", &g[i]);
		__int64 pre = 0, j, pre_sum = 0, ans;
		for(i = 0; i < r; i++){
			__int64 tmp = 0, num = 0;
			for(j = pre; tmp <= k && num <= n; j++){
				if(j == n) j = 0;
				tmp += g[j];
				num ++;
			}
			tmp -= g[j - 1];
			j--;
			if(j == -1)
				j = n - 1;
			
			bool f = false;
			__int64 kk;
			for(kk = 0; kk < value.size(); kk++)
				if(value[kk] == pre){
					f = true;
					break;
				}
			//f = false;
			if(!f){
				sum.push_back(pre_sum + tmp);
				pre_sum += tmp;
				value.push_back(pre);
			}
			else{		
				__int64 pre_sum = 0;
				ans = sum[kk] - tmp;
				__int64 rr  = r - kk;
				__int64 circle = i - kk;
				__int64 circle_sum = sum[i - 1] - sum[kk] + tmp;
				ans = ans + rr / circle * circle_sum;
				__int64 kkk = rr % circle;
				if(kkk != 0)
					ans = ans + sum[kk + kkk - 1] - sum[kk] + tmp;
				break;
			}
			pre = j;
		}
		if(i == r)
			ans = sum[r - 1];
	//	printf("Case #%d: %d\n", t, ans);
		fprintf(fout, "Case #%I64d: %I64d\n", t, ans);
	}
	return 0;
}
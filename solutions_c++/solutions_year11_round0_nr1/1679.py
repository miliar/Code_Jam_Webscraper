#include <cstdio>
#include <cstring>
#include <cmath>

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int pre[2];
	int curlast[2];
	int flag, curflag;
	int T, mcase = 1;
	int step, next;
	char str[2];
	int total;

	scanf("%d", &T);
	while(T--){
		pre[0] = pre[1] = 1;
		curlast[0] = curlast[1] = 0;
		total = 0;
		flag = 0;

		scanf("%d", &step);
		while (step--){
			scanf("%s%d", str, &next);
			if(strcmp(str, "O") == 0)
				curflag = 0;
			else
				curflag = 1;

			int temp = abs(next - pre[curflag]);
			if(flag == curflag){
				total = total + temp + 1;
				curlast[curflag] = curlast[curflag] + temp + 1;
			}
			else {
				if(temp <= curlast[flag]){
					total += 1;
					curlast[curflag] = 1;
					flag = curflag;
				}
				else {
					curlast[curflag] = temp - curlast[flag] + 1;
					total += curlast[curflag];
					flag = curflag;
				}
			}

			 pre[curflag] = next;
		}

		printf("Case #%d: %d\n", mcase, total);
		mcase ++;
	}
}
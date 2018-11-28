#include <cstdio>

int t, n, h, l, p[200];
bool flag;

int main(void)
{
	scanf("%d", &t);
	for(int cas=1; cas<=t; cas++){
		scanf("%d%d%d", &n, &l, &h);
		for(int i=0;i<n; i++){
			scanf("%d", &p[i]);
		}

		for(int test=l; test<=h; test++){
			flag = true;
			for(int i=0; i<n; i++){
				if((test%p[i])*(p[i]%test)){
					flag = false;
				}
			}
			if(flag){
				printf("Case #%d: %d\n", cas, test);
				break;
			}
		}

		if(!flag)
			printf("Case #%d: NO\n", cas);
	}

	return 0;
}

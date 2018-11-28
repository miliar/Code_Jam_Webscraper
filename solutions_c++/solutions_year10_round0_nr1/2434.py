#include <cstdio>
#include <cstring>

int arr[40];

void pre_done(){
	arr[1]=1;
	for(int i=2;i<31;i++)
		arr[i]=2*arr[i-1]+1;
}

int main()
{
	freopen("large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for(int ii=1;ii<=nca;ii++){
		int n, k, flag=0;
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", ii);
		for(int i=0;i<n;i++){
			if(!((k>>i)&1)){
				flag=1;
				break;
			}
		}
		if(flag)puts("OFF");
		else puts("ON");
	}
	return 0;
}
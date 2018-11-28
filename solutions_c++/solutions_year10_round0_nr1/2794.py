#include <stdio.h>

int main()
{
	int T,n,m,no = 0;
	freopen("E:\\A-large.in","r",stdin);
	freopen("E:\\A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		no++;
		scanf("%d%d",&n,&m);
		int tmp = (1<<n);
		m %= tmp;
		printf("Case #%d: ",no);
		if(m == tmp-1){
			printf("ON\n");
		}
		else printf("OFF\n");
	}
	return 0;
}
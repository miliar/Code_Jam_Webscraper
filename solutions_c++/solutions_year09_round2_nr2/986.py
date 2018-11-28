#include<stdio.h>
#include<string.h>
//#include<algorithm>
#include<stdlib.h>
using namespace std;

int main()
{
	int T, n, l, i, j, k;
	int a[30];
	char str[30];
	int TS = 0;
	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		
		scanf("%s",str);
		l = strlen(str);
		for( i = 0; i < l; i++)a[i] = str[i] - '0';
		
		i = 0;
		j = l-1;
		while(i < j){
			k = a[i];
			a[i] = a[j];
			a[j] = k;
			i++;
			j--;
		}
		
		TS++;
		printf("Case #%d: ",TS);
		
		for(i = 1; i < l; i++ ){
			if(a[i] < a[i-1])break;
		}
		
		if( i < l ){
			int flag = 0;
			for( i = 1; i < l; i++ ){
				for( j = 0; j < i; j++ ){
					if( a[i] < a[j] )
					{
						int t = a[i];
						a[i] = a[j];
						a[j] = t;
						
						
						int ii = 0;
						int jj = i-1;
						
						for(ii = 0; ii < i; ii++){
							for(jj=ii;jj<i;jj++){
								if(a[ii] < a[jj]){
									k = a[ii];
									a[ii] = a[jj];
									a[jj] = k;
								}
							}
						}
						
						flag = 1;
						break;
					}
				}
				if(flag)break;
			}
			
			for( i=l-1;i>=0;i--)printf("%d",a[i]);
			printf("\n");
			
		}else{
			k = 0;
			for(i = 0; i < l; i++)if(a[i]!=0){
				printf("%d",a[i]);
				k = i;
				break;
			}
			for(i = 0; i <= k; i++)printf("0");
			for(i = k+1; i < l; i++)printf("%d", a[i]);
			printf("\n");
		}
	}
	
	return 0;
}

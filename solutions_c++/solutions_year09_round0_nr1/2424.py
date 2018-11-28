#include <stdio.h>
#include <string.h>
	
	char dictionary[5010][16];
	char str[512],*ptr;
	int testcase[512][16][30];
	int count[512];
	int ans;

int main(){
	int l,d,n;
	int i,j,k,m;

	
	memset(count,0x00,sizeof(count));
	memset(testcase,0x00,sizeof(testcase));
	
	scanf("%d%d%d",&l,&d,&n);
	
	for(i = 0;i < d;i++){
		scanf("%s",&dictionary[i]);
		//puts(dictionary[i]);
	}
	
	for(i = 0;i < n;i++){
		scanf("%s",&str);
		//puts(str);
		k = 0;
		for(j = 0;str[j] != '\0';j++){
			if(str[j] == '('){
				for(m = j+1;str[m] != ')';m++){
					testcase[i][k][str[m]- 'a'] = 1;
					//printf("%d %d %c\n",i,k,str[m]);
				}
				j = m;
			}
			else{
				testcase[i][k][str[j]- 'a'] = 1;
				//printf("%d %d %c\n",i,k,str[j]);
			}
			k++;
		}
	}
		
	for(i = 0;i < n;i++){
		for(j = 0;j < d;j++){
			/*test dic[j] & testcase[i]*/
			ans = 1;
			for(k = 0;ans && k < l;k++){
				if(!testcase[i][k][dictionary[j][k]-'a'])
					ans = 0;
			}
			if(ans)
				count[i]++;
		}
	}
	
	for(i = 0;i < n;i++){
		printf("Case #%d: %d\n",i+1,count[i]);
	}
	
	
	return 0;
}
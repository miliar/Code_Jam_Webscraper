#include <stdio.h>
#include <string.h>

int next[64];

int main(){
	char str[64];
	int map[256];
	int t,cas;
	int i, j;
	int base;
	int sec;
	
	gets(str);
	sscanf(str,"%d",&t);
	
	for(i = 0;i < 64;i++)
		next[i] = i;
	next[0] = 1;
	next[1] = 0;
	
	
	for(cas = 1; cas <= t;cas++){
		gets(str);
		memset(map,0xFF,sizeof(map));
		base = 0;
		for(i = 0; str[i] != '\0';i++){
			if(map[str[i]] == -1){
				map[str[i]] = 1;
				base++;
			}
		}
		sec = 0;
		j = 0;

		if(base == 1)
			base = 2;
			
		memset(map,0xFF,sizeof(map));
		for(i = 0;str[i] != '\0';i++){
			sec *= base;
			if(map[str[i]] == -1){
				map[str[i]] = next[j];
				j++;
				sec += map[str[i]];
			}
			else{
				sec += map[str[i]];
			}
			//printf("%c %d\n",str[i],map[str[i]]);
		}
		
		printf("Case #%d: %d\n",cas,sec);
	}
	return 0;
}
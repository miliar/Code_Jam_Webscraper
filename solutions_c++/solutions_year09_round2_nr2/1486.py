#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char ori[16],str[16];
char pre[16],current[16];
int ans;
int digit;
int count[16],bound[16];


int cmp(const void *a,const void *b){
	char aa = *(char *)a;
	char bb = *(char *)b;
	
	return aa - bb;
}

int Compare(char * current){
	int v1,v2;
	
	//puts(current);
	v1 = strcmp(pre,ori);
	v2 = strcmp(current,ori);
	
	//printf("cur %s pre %s ori %s %d %d\n",current,pre,ori,v1,v2);
	if(v1 == 0 && v2 > 0){
		ans = 1;
		//printf("cur %s pre %s ori %s %d %d\n",current,pre,ori,v1,v2);
		return 1;
	}

	strcpy(pre,current);
	return 0;
}
void DFS(int d){
	int i;


		
	if(d == digit){
		current[digit] = '\0';
		if(Compare(current) == 1)
			return;
	}
	

	for(i = 0;!ans && i < 10;i++){
		//printf("i%d %d %d",i,count[i],bound[i]);
		if(count[i] < bound[i]){
			count[i]++;
			current[d] = i + '0';
			current[d+1] = '\0';
			//printf("now %s\n",current);
			DFS(d+1);
			count[i]--;
		}
	}	
}

void DFS2(int d){
	int i;

	
		
	if(d == digit){
		current[digit] = '\0';
		ans = 1;
			return;
	}
	

	for(i = 0;!ans && i < 10;i++){
		//printf("i%d %d %d",i,count[i],bound[i]);
		if(count[i] < bound[i]){
			count[i]++;
			current[d] = i + '0';
			//current[d+1] = '\0';
			//printf("now %s\n",current);
			DFS2(d+1);
			count[i]--;
		}
	}	
}
int main(){
	int t,cas;
	int i;
	
	gets(str);
	sscanf(str,"%d",&t);
	for(cas = 1;cas <= t;cas++){
		gets(str);

		strcpy(ori,str);
		pre[0] = '\0';
		digit = strlen(str);
		
		qsort(str,strlen(str),sizeof(char),cmp);
		
		memset(bound,0x00,sizeof(bound));
		

		for(i = 0; i < digit;i++){
			bound[ori[i] - '0']++;
		}
		
		memset(count,0x00,sizeof(count));
		ans = 0;
		DFS(0);
		//printf("Case #%d: %s\n",cas,current);
		if(!strcmp(current,ori)){
			
			memset(count,0x00,sizeof(count));
			bound[0]++;
			digit++;
			for(i = 1;i < 10;i++){
				if(bound[i] != 0){
					count[i]++;
					current[0] = i + '0'; 
					break;
				}
			}
			ans = 0;
			DFS2(1);
			
		}
		printf("Case #%d: %s\n",cas,current);
		
	}
	
	return 0;
}
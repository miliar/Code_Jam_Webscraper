#include<stdio.h>

#define MAXL 16
#define MAXD 8*1024

char dic[MAXD][MAXL];
char buf[1024];

int main(){
	int l,d,n,i,j,count,pos;
	char c1,c2;
	
	scanf("%d %d %d",&l,&d,&n);
	scanf(" ");
	
	for(i=0;i<d;i++)
			gets(dic[i]);
	
	int tot = n;		
	while(n--){
		gets(buf);

		count = 0;
		for(i=0;i<d;i++){
			pos = 0;
			for(j=0;j<l;j++){
				c1 = dic[i][j];
				
				if(buf[pos] == '('){
					c2 = -1;
					while(buf[pos] != ')'){
						pos++;
						if(c2 != -1) continue;
						if(buf[pos] == c1) c2 = c1; 
					}
					pos++;
				}else{
					c2 = buf[pos++];
				}
				if(c1 != c2) break;
			}
			if(j>=l) count++;
		}
		printf("Case #%d: %d\n",tot-n,count);
	}
	return 0;
}

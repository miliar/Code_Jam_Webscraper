#include <stdio.h>

int ok[20][26];
char dic[5005][20];
int l;

void process(char *s){
	int i,j;
	for (i=0; i<l; i++){
		for (j=0; j<26; j++) ok[i][j]=0;
		if (*s=='('){
			while((*(++s))!=')') ok[i][(*s)-'a']=1;
		}
		else ok[i][(*s)-'a']=1;
		s++;
	}
}

int main(){
	int ds,n,i,j,k;
	char s[30*20];
	
	scanf("%d%d%d",&l,&ds,&n);
	
	for (k=0; k<ds; k++)
		scanf("%s",dic[k]);
		//printf("d1=%d\n",ds);
	for (k=0; k<n; k++){
		//printf("d2=%d\n",ds);
		scanf("%s",s);
		process(s);
		int c=0;
		for (i=0; i<ds; i++){
			//printf("ds=%d\n",ds);
			//printf("%d\n",i);
			for (j=0; j<l; j++){
				if (!ok[j][dic[i][j]-'a']) break;
			}
			if (j==l) c++;
		}
		printf("Case #%d: %d\n",k+1,c);
	}
	return 0;
}



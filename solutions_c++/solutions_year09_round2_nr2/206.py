#include<stdio.h>
#include<algorithm>

int T=0,zer=0,r=0;
char s[111],l=0;

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int _=0;_<T;_++){
		scanf("%s",s);
//		printf("%s\n",s);
		l=strlen(s);
		if(!std::next_permutation(s,s+l)){
			zer=0;
			r=0;
			for(int i=0;i<l;i++) if(s[i]=='0'){
				zer++;
			}else s[r++]=s[i];
			zer++;
			s[r]=0;


			printf("Case #%d: %c",_+1,s[0]);
			for(int i=0;i<zer;i++) putchar('0');
			printf("%s\n",s+1);
		}else
			printf("Case #%d: %s\n",_+1,s);
	}
	return 0;
}

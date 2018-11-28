#include<stdio.h>

char str[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

//void init(){
//	char s1[110],s2[110];
//	gets(s1);
//	gets(s2);
//	for(int i=0;s1[i]!='\0';i++){
//		if(s1[i]!=' '){
//			str[s1[i]-'a']=s2[i];
//		}
//	}
//}


/*for(int i=0;i<26;i++){
		str[i]='0';
	}
	init();
	init();
	init();
	printf("\'%c\'",str[0]);
	for(int i=1;i<26;i++){
		printf(",\'%c\'",str[i]);
	}*/

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	getchar();
	for(int Case=1;Case<=T;Case++){
		char str1[110];
		char str2[110];
		gets(str1);
		int i=0;
		for(i=0;str1[i]!='\0';i++){
			if(str1[i]>='a'&&str1[i]<='z'){
				str2[i]=str[str1[i]-'a'];
			}
			else str2[i]=str1[i];
		}
		str2[i]='\0';
		printf("Case #%d: %s\n",Case,str2);
	}
	return 0;
}

	

#include<cstdio>
#include<cstring>
int link[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

//int link[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,-1,19,13,22,9,15,5,12,0,-1};
//16 25
char str[2000000];
int main(){
	int i,j,t;
	freopen("out.txt","w",stdout);
	scanf("%d",&t);getchar();
	for(i=1;i<=t;i++){
		gets(str);
		printf("Case #%d: ",i);
		for(j=0;str[j];j++){
			if(str[j]==' ')printf(" ");
			else printf("%c",link[str[j]-'a']+'a');
		}
		printf("\n");
	}
	return 0;
}

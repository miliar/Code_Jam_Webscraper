#include<stdio.h>
#include<string>
#include<map>
//#include<Windows.h>
using namespace std;
int main(){
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	char c1[136]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z";
	char c2[136]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q";
	int n,t=1;
	map<char,char>mp;
	for(int g=0;g<136;g++){
		mp[c1[g]]=c2[g];
	}
	char ss[105];
	scanf("%d\n",&n);
	while(n--){
		gets(ss);
		printf("Case #%d: ",t++);
		for(int i=0;i<strlen(ss);i++){
			char c=ss[i];
			if(c!=' '){
				c=mp[c];
			}
			printf("%c",c);
		}
		printf("\n");
	}
	//system("pause");
	return 0;
}
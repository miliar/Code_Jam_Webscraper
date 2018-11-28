#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
#include<math.h>
#include<set>
using namespace std;

char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
		'j','p','f','m','a','q'};
char str[220];
int main()
{
	int T,ri=1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	getchar();
	while(T--){
		gets(str);
		for(int i=0;str[i];i++){
			if(str[i]==' ')
				continue;
			str[i]=map[str[i]-'a'];
		}
		printf("Case #%d: ",ri++);
		puts(str);
	}

}

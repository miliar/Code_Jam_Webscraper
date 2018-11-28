#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<limits>
#include<set>

using namespace std;

int main()
{
	char map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char str[110];
	int N;
	scanf("%d\n",&N);
	for(int k=0;k<N;++k)
	{
		cin.getline(str,110);
		
		printf("Case #%d: ",k+1);
		for(int i=0;str[i];++i){
			if(str[i]>='a'&&str[i]<='z'){
				printf("%c",map[str[i]-'a']);
			}else if(str[i]>='A'&&str[i]<='Z'){
				printf("%c",map[str[i]-'A']-('a'-'A'));
			}else printf("%c",str[i]);
		}
		printf("\n");
		
	}
	return 0;
}


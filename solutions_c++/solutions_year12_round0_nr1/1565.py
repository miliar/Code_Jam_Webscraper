#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <string>
#include <sstream>
#include <map>
#include <set>

#define ll long long

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char to[]={"yhesocvxduiglbkrztnwjpfmaq"};
	int T=0;
	scanf("%d\n",&T);
	char str[102];
	for(int t=1;t<=T;++t) {
		gets(str);
		for(int i=strlen(str)-1;i>=0;--i)
			if (str[i]!=' ') str[i]=to[str[i]-'a'];
		printf("Case #%d: %s\n",t,str);
	}
	return 0;
}

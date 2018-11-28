#include <iostream>
#include <string.h>
using namespace std;
char mmap[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k'	,'r','z','t','n','w','j','p','f','m','a','q'};
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	char mm[200];
	int len;
	int cnt = 0;
	scanf("%d\n",&len);
	while(gets(mm))
	{
		++cnt;
		len = strlen(mm);
		for(int i=0 ;i<len ;++i)
		{
			if(mm[i] != ' ')
			{
				mm[i] = mmap[mm[i]-'a'];
			}
		}
		printf("Case #%d: %s\n",cnt,mm);
	}
}
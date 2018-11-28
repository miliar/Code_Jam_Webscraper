#include <algorithm>
#include <iostream>

using namespace std;

const char pattern[]=" welcome to code jam";
const int patternLen=20;

int main()
{
	int nTest;
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d ",&nTest);
	for(int test=1;test<=nTest;test++)
	{
		char buff;
		int mic[20]={1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
		scanf("%c",&buff);
		while(buff!='\n')
		{
			for(int q=patternLen-1;q>0;q--)
				if(buff==pattern[q])mic[q]=(mic[q]+mic[q-1])%10000;
			scanf("%c",&buff);
		}
		printf("Case #%d: ",test);
		if(mic[patternLen-1]<10)printf("0");
		if(mic[patternLen-1]<100)printf("0");
		if(mic[patternLen-1]<1000)printf("0");
		printf("%d\n",mic[patternLen-1]);
	}
	return 0;
}

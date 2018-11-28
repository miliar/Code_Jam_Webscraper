#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int N;
int main()
{
	const char base[]="welcome to code jam";//19
	scanf("%d",&N);
	string thme;
	getline(cin,thme);//dummy
	for (int kase=1;kase<=N;++kase)
	{
		string me;
		getline(cin,me);
		int M=me.length();
		vector< vector< int > > Cnt( M , vector<int>(20,0) );//len,init
		for (int q=0;q<M;q++) if (me[q]=='w') Cnt[q][0]=1;
		for (int q=1;q<19;q++)
		{
			int s=0;
			for (int w=0;w<M;w++)
			{
				if (me[w]==base[q]) Cnt[w][q]=s;
				(s+=Cnt[w][q-1])%=10000;
			}
		}
		int ret=0;
		for (int w=0;w<M;w++) (ret+=Cnt[w][18])%=10000;
		printf("Case #%d: %04d\n",kase,ret);
	}
	return 0;
}

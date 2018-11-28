#include <stdio.h>
#include <string>
#include <set>
using namespace std;

int n;
char s[600];
const char welcome[]="welcome to code jam";
const int K=19;
int kol[K];

int main()
{
	//death();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&n);
	gets(s);
	for(int i=0;i<n;i++)
	{
		gets(s);
		for(int i=0;i<K;i++)
			kol[i]=0;
		for(int i=0;s[i]!=0;i++)
			if(s[i]=='w')
				kol[0]++;
			else
				for(int j=1;j<K;j++)
					if(s[i]==welcome[j])
						kol[j]=(kol[j]+kol[j-1])%10000;
		printf("Case #%d: %04d\n",i+1,kol[K-1]);
	}
	//
	return 0;
}
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int T,Ti=0;;
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		int k;
		char s[1100];
		scanf("%d",&k);
		scanf("%s",s);
		int len=strlen(s);

		int key[10];
		for(int i=0;i<k;i++)
			key[i]=i;

		char t[1100];
		int minn=1<<30;
		while(1)
		{
			//for(int i=0;i<k;i++) printf("%d ",key[i]);puts("");
			for(int i=0;i<len;i++)
			{
				int starti=i/k;
				t[starti*k+key[i%k]]=s[i];
			}
			t[len]='$';
			t[len+1]=0;
			int count=0;
			for(int i=0;i<len;i++)
				if(t[i]!=t[i+1]) count++;
			minn=min(minn,count);
			//printf("%s\n",t);
			if(!next_permutation(key,key+k))
				break;
		}
		printf("Case #%d: %d\n",Ti,minn);

	}
}
#include <stdio.h>
#include <string.h>

int main()
{
	int t;
	scanf("%d",&t);
	int ti;
	for (ti=0;ti<t;ti++)
	{
		int n;
		char buf[41];
		int len[40];
		scanf("%d",&n);
		int ni;
		for (ni=0;ni<n;ni++)
		{
			scanf("%s",buf);
			int bi;
			for (bi=strlen(buf)-1;bi>=0;bi--)
				if (buf[bi]=='1') break;
			len[ni]=bi;
//			printf("%d\n",bi);
		}
		int li;
		int cnt=0;
		for (li=0;li<n;li++)
		{
			for (ni=li;ni<n;ni++)
				if (len[ni]<=li) break;
			int temp;
			for (ni--;ni>=li;ni--)
			{
				temp=len[ni];
				len[ni]=len[ni+1];
				len[ni+1]=temp;
				cnt++;
			}
//			for (ni=0;ni<n;ni++)
//				printf("%d ",len[ni]);
//			printf("%d\n",cnt);
		}
		printf("Case #%d: %d\n",ti+1,cnt);
	}
	return 0;
}

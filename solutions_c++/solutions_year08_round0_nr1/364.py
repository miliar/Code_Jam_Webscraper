#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
char buf[1000];
int N,N1,i,j,T;
vector<string> src;
vector<int> slots,slotnew;
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	int total;
	scanf("%d",&total);
	T=total;
	while (total--)
	{
		scanf("%d",&N);
		gets(buf);
		N1=N;
		slots.clear();
		src.clear();
		slotnew.clear();
		while (N--)
		{
			gets(buf);
			src.push_back(buf);
			slots.push_back(0);
		}
		scanf("%d",&N);
		gets(buf);
		while (N--)
		{
			slotnew.clear();
			gets(buf);
			for (i=0;i<N1;i++)
				if (src[i]==buf)
					{
						slotnew.push_back(10000000);
						for (j=0;j<N1;j++) if (j!=i)
							if (slots[j]+1<slotnew[i])
								slotnew[i]=slots[j]+1;
					}
				else
					slotnew.push_back(slots[i]);
			slots.swap(slotnew);
		}
		j=10000000;
		for (i=0;i<N1;i++)
			if (slots[i]<j)
				j=slots[i];
		printf("Case #%d: %d\n",T-total,j);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
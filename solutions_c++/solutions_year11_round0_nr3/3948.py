#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	freopen("test.in","r",stdin);
	int testn;
	scanf("%d",&testn);
	int tn=1;
	while(testn--)
	{
		int num;
		scanf("%d",&num);
		int array[1000];
		int t=0,s=0;
		for(int i=0;i<num;i++)
		{
			scanf("%d",&array[i]);
			t^=array[i];
			s+=array[i];
		}
		printf("Case #%d: ",tn++);
		if(t!=0)
			printf("NO\n");
		else
		{
			sort(array,array+num);
			printf("%d\n",s-array[0]);
		}
	}
}

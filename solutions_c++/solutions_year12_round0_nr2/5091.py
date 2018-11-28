#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int arr[1000];
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		int t,s,p;
		scanf("%d %d %d",&t,&s,&p);
		int j;
		int num1 = 3*p - 4;
		int num2 = 3*p - 3;
//		printf("num1 -> %d and num2 -> %d\n",num1,num2);
		int count = 0;
		int cnt = 0;
		for(j=0;j<t;j++)
		{
			scanf("%d",&arr[j]);	
			if(arr[j] > num2)
				count++;
			if(arr[j] == num1 || arr[j] == num2)
				cnt++;
		}
//		printf("cnt-> %d\n",cnt);
		cnt = min(cnt,s);
		if(num2 > s)
			count += cnt;
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}

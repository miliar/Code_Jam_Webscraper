#include <iostream>
using namespace std;
int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int A, B;
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d\n",&A,&B);
		int cnt=0;
		for(int i=A;i<=B;i++)
		{
			if(i<10) continue;
			int num=i;
			int mod=1;
			while(num>9)
			{
				num/=10;
				mod*=10;
			}
			num=i;
			while(1)
			{
				int next = (num%mod)*10+(num/mod);
				if(next==i) break;
				if(next>i&&next<=B) cnt++;
				num=next;
			}
		}
		printf("%d\n",cnt);
	}
}
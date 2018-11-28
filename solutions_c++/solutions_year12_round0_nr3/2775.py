#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>

using namespace std;

int f[2000001];

map <int , int> ma;

int get(int now,int l,int r)
{
	ma.clear();
	int shi=10;
	int orz=0,sro=1,sto=now;
	int ans=0;
	while (sto!=0)
	{
		orz++;
		sto/=10;
	}
	while (shi<now)
	{
		int last=now % shi;
		if (last / (shi / 10)!=0)
		{
			int first=now - last;
			int crf=1;
			for (int a=1;a<=orz-sro;a++)
				crf*=10;
			int newnum=crf*last+first/shi;
			if (newnum>l && newnum<=r) 
			{
				if (!ma[newnum]) ans++,ma[newnum]++;
			}
		}
		shi*=10;
		sro++;
	}
	return ans;
}

int main()
{
	int t;
	//f[9]=0;
	//for (int a=10;a<=2000000;a++)
	scanf("%d",&t);
	//for (int a=1;a<=t;a++)
	//{
	//	int l,r;
	//	scanf("%d%d",&l,&r);
	//	printf("Case #%d: %d\n",a,f[r]-f[l-1]);
	//}
	for (int a=1;a<=t;a++)
	{
		int l,r;
		scanf("%d%d",&l,&r);
		int ans=0;
		for (int b=l;b<=r;b++)
			ans+=get(b,b,r);//,printf("%d %d %d %d\n",b,l,r,get(b,b,r));
		printf("Case #%d: %d\n",a,ans);
	}

	return 0;
}

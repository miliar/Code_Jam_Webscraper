#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

#define pci pair<char, int>
pci* mas;
int* tms;

void test(int num)
{
	int o=1, b=1, ot=0, bt=0;
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
	{
		scanf(" %c %d",&mas[i].first, &mas[i].second);
	}
	tms[0]=0;
	for(int i=0; i<n; ++i)
	{
		if(mas[i].first=='O')
		{
			ot=tms[i+1]=max(tms[i],ot+abs(o-mas[i].second))+1;
			o=mas[i].second;
		}
		else
		{
			bt=tms[i+1]=max(tms[i],bt+abs(b-mas[i].second))+1;
			b=mas[i].second;
		}
	}
	printf("Case #%d: %d\n",num,tms[n]);
}

int main()
{
	mas=new pci[1000];
	tms=new int[1000];
	int t;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}
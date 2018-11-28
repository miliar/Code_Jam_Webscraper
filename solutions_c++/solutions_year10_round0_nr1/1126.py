#include<iostream>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int bi[31]={1,2};
	for(int i=2;i<31;i++)
		bi[i]=bi[i-1]*2;
	int T;
	int n,k;
	cin>>T;
	int sce=1;
	while(T--)
	{
		scanf("%d%d",&n,&k);
		int tmp=k%(bi[n]);
		printf("Case #%d: ",sce++);
		if(tmp==bi[n]-1)
			puts("ON");
		else
			puts("OFF");
	}
}
#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int num[1005];

int main()
{
	freopen("d://D-large.in","r",stdin);
	freopen("d://lowesy.txt","w",stdout);
	int _,cases=1,N;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%d",&num[i]);
		double res=0.0;
		for(int i=0;i<N;i++)
			if(num[i]!=i+1) res+=1.0;
		printf("Case #%d: %.8f\n",cases++,res);
	}
	return 0;
}
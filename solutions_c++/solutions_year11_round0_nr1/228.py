#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		int n;
		scanf("%d",&n);
		int PO=1,PB=1,LTO=0,LTB=0,S=0;
		for(int _n=1;_n<=n;_n++)
		{
			char c[5];int p;
			scanf("%s%d",c,&p);
			if(c[0]=='O')
			{
				int w=abs(PO-p);
				if(w>S-LTO)S=LTO+w;
				S++;LTO=S;PO=p;
			}else
			if(c[0]=='B')
			{
				int w=abs(PB-p);
				if(w>S-LTB)S=LTB+w;
				S++,LTB=S;PB=p;
			}
//			printf("%d %d %d %d %d\n",PO,PB,LTO,LTB,S);
		}
		printf("Case #%d: %d\n",__,S);
	}
	return 0;
}


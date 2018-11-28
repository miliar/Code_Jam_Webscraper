#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int nt,n,oc,bc,op,bp,el;

int main()
{
	scanf("%d",&nt);
	for(int i=1;i<=nt;i++)
	{
		bc=oc=0;
		bp=op=1;
		int ans=0;
		scanf("%d",&el);
		for(int j=0;j<el;j++)
		{
			char buff[3];
			int pos;
			scanf("%s%d",buff,&pos);
			if(buff[0]=='O')
			{
				int diff = abs(op-pos);
				if(diff < bc)
				{
					bc=0;
					ans+=1;
					oc++;
					op=pos;
				}
				else
				{
					op=pos;
					ans+= (abs(diff-bc)+1);
					oc += (abs(diff-bc)+1);
					bc=0;
				}
			}
			else
			{
				int diff=abs(bp-pos);
				if(diff < oc)
				{
					oc=0;
					ans+=1;
					bc++;
					bp=pos;
				}
				else
				{
					bp=pos;
					ans+=abs(diff-oc)+1;
					bc+=abs(diff-oc)+1;
					oc=0;
				}
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}

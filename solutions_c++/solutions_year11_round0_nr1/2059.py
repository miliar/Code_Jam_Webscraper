#include <stdio.h>
#include <vector>

using namespace std;

inline int abs(int a)
{
	return a>0?a:-a;
}

int main(void)
{
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;++j)
	{
		int n;
		int pos_o = 1,pos_b = 1;
		int delta_o = 0,delta_b = 0;;
		int pos[110],time = 0;;
		char rName[110][3];
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%s%d",rName[i],pos+i);
		}
		for(int i=0;i<n;++i)
		{
			if(rName[i][0]=='O')
			{
				if(abs(pos[i]-pos_o)>delta_o)
				{
					time += abs(pos[i]-pos_o)-delta_o;
					delta_b += abs(pos[i]-pos_o)-delta_o;
				}
				pos_o = pos[i];
				time ++;delta_b++;
				delta_o = 0;
			}
			else
			{
				if(abs(pos[i]-pos_b)>delta_b)
				{
					time += abs(pos[i]-pos_b)-delta_b;
					delta_o += abs(pos[i]-pos_b)-delta_b;
				}
				pos_b = pos[i];
				time ++;delta_o++;
				delta_b = 0;
			}
		//	if(j==10)printf("%d %d %d %d %d %d\n",pos[i],time,delta_o,delta_b,pos_o,pos_b);
		}
		printf("Case #%d: %d\n",j+1,time);
	}
	return 0;
}

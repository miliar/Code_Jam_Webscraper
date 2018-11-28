#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std ;

#define MAXN 105

bool canwithout[MAXN];
bool canwith[MAXN];
int arr[MAXN];
int n,S,p;

int main()
{
	FILE *in=fopen("dance.in","r");
	freopen("out.out","w",stdout);
	int c,c2,c3,c4;
	int tests;
	fscanf(in,"%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		memset(canwithout,0,sizeof(canwithout));
		memset(canwith,0,sizeof(canwith));
		fscanf(in,"%d%d%d",&n,&S,&p);
		for (c=0;c<n;c++)
			fscanf(in,"%d",&arr[c]);
		for (c=0;c<n;c++)
			for (c2=0;c2<=10;c2++)
				for (c3=0;c3<=10;c3++)
					for (c4=0;c4<=10;c4++)
					{
						if (c2<p && c3<p && c4<p)continue;
						if (c2+c3+c4!=arr[c])continue;
						if (abs(c2-c3)>2 || abs(c2-c4)>2 || abs(c3-c4)>2)continue;
						if (abs(c2-c3)<2 && abs(c2-c4)<2 && abs(c3-c4)<2)
							canwithout[c]=1;
						else canwith[c]=1;
					}
		int ret=0;
		int rem=S;
		for (c=0;c<n;c++)
		{
			if (canwithout[c])ret++;
			else if (canwith[c] && rem){
				ret++;
				rem--;
			}
		}
		printf("Case #%d: %d\n",test,ret);
	}
	
	return 0;
}

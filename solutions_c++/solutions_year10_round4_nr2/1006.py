#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#include <memory.h>

vector<int> m;
int p;
int res = 0;

int go1(int i)
{
	if(i >= (1<<p) -1)
		return m[i];
	return m[i] = max(go1(2*i+1), go1(2*i + 2));
}

int dec(int i,int level = p,int de = 0)
{
	if(level == 0) 
		return 0;
	if((m[i] - de) > 0)//== level || (m[2*+1] == m[2*i+2] && (m[2*i+2]-de > 0)))
	{
		res++;
		de++;
//		printf("inc %d\n",i);
	}
	dec(2*i+1,level-1,de);
	dec(2*i+2,level-1,de);		
	return 0;
}

int main()
{
	freopen("B-small-attempt4.in","r",stdin);
//	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int t;
	scanf("%d",&t);
	for(int ti = 0;ti < t;ti++)
	{
		scanf("%d",&p);
		res = 0;
		m.assign((1<<(p+1))-1,0);
		for(int i=0;i<(1<<p);i++)
		{
			scanf("%d",&m[(1 << p) - 1 + i]);
			m[(1 << p) - 1 + i] = p - m[(1 << p) - 1 + i];
		}
		for(int i=0;i<(1<<p) - 1;i++)
			scanf("%*d");
		

		go1(0);	
//		for(int i=0;i<m.size();i++) printf("%d  ",m[i]); puts("");
		dec(0,p,0);
		printf("Case #%d: %d\n",ti+1,res);
	}
	
	return 0;
}
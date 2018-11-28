#include<cstdio>
#include<cstring>
#include<iostream>
#include<sstream>
#include<map>
#include<cmath>
#include<vector>
#include<string>
#include<set>
#include<queue>
#include<algorithm>

using namespace std;
//const int MAXN = 102;

typedef long long int64;
typedef pair<int, int> pint;
int n,m;

/*
int betw(int a, int b, int c, int d, int val)
{
	if(val <=b && val >=a)
		return 1;

	if(val <=d && val >=c)
		return 2;

	if(c > b)
	{
		if(val > b && val < c || val < a)
			return 3;
		if(val > d)
			return 2;
	}
	if(d < a)
	{
		if(val > d && val<a || val > b)
			return 3;
		if()
	}
	else


}*/

int test(int ax, int bx, int ay, int by, int x, int y, int vx, int vy)
{
	
	
	
	
	if(ax > bx || ay > by)
		return 0;


	if(vx < ax)
		ax=vx;
	if(vx > bx)
		bx=vx;
	
	if(vy < ay)
		ay=vy;
	if(vy > by)
		by=vy;

	if(x <= bx && x >= ax && y>=ay && y<=by)
		return 1;
	else
		return 0;
/*
	if(y > by && x > bx)
	{
		if(vx >= x && vy >=y)
			return 1;
	}
	if(y > by && x < ax)
	{
		if(vy>=y && vx<=x)
			return 1;
	}
	if(y > by && x<=bx && x>=ax)
	{
		if(vy>=y)
			return 1;
	}
	if(y < ay && x > bx)
	{
		if(vy<=y && vx>=x)
			return 1;
	}
	if(y < ay && x < ax)
	{
		if(vy<=y && vx<=x)
			return 1;
	}
	if(y < ay && x<=bx && x>=ax)
	{
		if(vy <=y)
			return 1;
	}

	if(y>=ay && y<=by && x > bx)
	{
		if(vx>=x)
			return 1;
	}

	if(y>=ay && y<=by && x < ax)
	{
		if(vx<=x)
			return 1;
	}
*/
	return 0;
}




int main()
{
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);

	vector<pint> rec;
	for(int c=1; c<=numCase; c++)
	{
		rec.clear();
		printf("Case #%d:\n", c);
		scanf("%d", &n);
		int h, w;

		int bha=10000000, bhb=-1;
		int bwa=10000000, bwb=-1;
		int uha=10000000, uhb=-1;
		int uwa=10000000, uwb=-1;

		char buf[20];

		for(int i=0; i<n; i++)
		{
			scanf("%d%d%s", &h,&w,buf);
			if(strcmp(buf, "BIRD") == 0)
			{
				if(h<bha)
					bha=h;
				if(h>bhb)
					bhb=h;
				if(w<bwa)
					bwa=w;
				if(w>bwb)
					bwb=w;

			}
			else if(strcmp(buf, "NOT")==0)
			{
				gets(buf);
				rec.push_back(pint(h,w));
			}
			else
			{
				printf("=----------------");
				return -1;
			}
		}
			scanf("%d", &m);
			int stat=0;
			for(int i=0; i<m; i++)
			{
				scanf("%d%d", &h,&w);
			
				

				if(h >= bha && h <= bhb && w>=bwa && w<=bwb)
				{
					printf("BIRD\n");
					continue;
				}
				

				for(int j=0; j<rec.size(); j++)
				{
					if(test(bha, bhb, bwa, bwb, rec[j].first, rec[j].second, h, w)==1)
					{
						printf("NOT BIRD\n");
						goto end;
					}
				}
				printf("UNKNOWN\n");
end:;
			}
		}
		
	
	return 0 ;
}

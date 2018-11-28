#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T,N,x,y,z,ans,posb,poso,now;
vector<int> orange,blue;
vector<char> urut;
char code[2];

int main()
{
	scanf("%d",&T);
	for(z=1;z<=T;z++)
	{
		orange.clear();
		blue.clear();
		urut.clear();
		scanf("%d",&N);
		while(N--)
		{
			scanf("%s %d",code,&x);
			urut.pb(code[0]);
			switch(code[0])
			{
				case('O') : orange.pb(x);break;
				case('B') : blue.pb(x);break;
			}
		}
		
		poso=posb=1;
		x=y=ans=now=0;
		do
		{
			bool pencet=false;
			ans++;
			if(orange.size())
			{
				if(poso<orange[x]) poso++; else
				if(poso>orange[x]) poso--; else
				if((urut[now]=='O')&&(poso==orange[x]))
				{
					now++;
					if(x+1<orange.size()) x++;
					pencet=true;
				}
			}
			
			if(blue.size())
			{
				if(posb<blue[y]) posb++; else
				if(posb>blue[y]) posb--; else
				if((urut[now]=='B')&&(posb==blue[y])&&(!pencet))
				{
					now++;
					if(y+1<blue.size()) y++;
				}
			}
			
			//cout << ans << " " << poso << " " << posb << endl;
		}while(now<urut.size());
		
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}


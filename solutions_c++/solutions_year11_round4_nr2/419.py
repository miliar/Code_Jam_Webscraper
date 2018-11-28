#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;

int w[500][500];

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		
		int R,C,D;

		cin>>R>>C>>D;

		for(int i=0;i<R;i++)
		{
			string s;
			cin>>s;
			for(int j=0;j<C;j++)
				w[i][j] = D+s[j]-'0';
		}

		int ans = 0;

		for(int l=3;l<=max(R,C);l++)
		{
			for(int i=0;i<R;i++)
				for(int j=0;j<C;j++)
				{
					int top=i,bottom=i+l-1,left=j,right=j+l-1;
					if (bottom>=R||right>=C) continue;
					double midX = (top+bottom)/2.0, midY = (left+right)/2.0;
					double weightX = 0.0, weightY = 0.0;
					for(int x=top;x<=bottom;x++)
						for(int y=left;y<=right;y++)
						{
							if ((x==top||x==bottom)&&(y==left||y==right)) continue;
							weightX += w[x][y]*(x-midX);
							weightY += w[x][y]*(y-midY);
						}
					if (fabs(weightX)<1e-6&&fabs(weightY)<1e-6) ans = max(ans,l);
				}
		}

		if (ans==0) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}

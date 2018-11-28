#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <string>
using namespace std;

int main() {
//	freopen("B-small-attempt2.in", "r", stdin );
	freopen("B-large.in", "r", stdin );
	freopen("output.txt", "w", stdout );
	int cas;
	scanf("%d", &cas);
	for ( int cass=1; cass<=cas; ++cass)
	{
		char res[200];
		char c[200][200];
		char o[200][200];
		int cn,on,n,m;
		m=0;
		memset( c, -1, sizeof(c));
		memset( o, 0, sizeof(o));
		char str[200];
		scanf("%d", &cn);
		for (int i=0; i<cn; ++i)
		{
			scanf("%s", str);
			c[str[0]][str[1]] = str[2];
			c[str[1]][str[0]] = str[2];
		}
		scanf("%d", &on);
		for (int i=0; i<on; ++i)
		{
			scanf("%s", str);
			o[str[0]][str[1]] = 1;
			o[str[1]][str[0]] = 1;
		}
		scanf("%d",  &n);
		scanf("%s", str);
		for (int i=0; i<n; ++i)
		{
			res[m]='\0';
			//puts(res);
			if ( m > 0 )
			{
				if ( c[str[i]][res[m-1]] != -1 )
				{
					res[m-1] = c[str[i]][res[m-1]];
					continue;
				}
				bool b = false;
				for (int j=0; j<m; ++j)
				if ( o[str[i]][res[j]] == 1 )
				{
					m=0;
					b=true;
					break;
				}
				if ( b ) continue;

			}
			res[m++]=str[i];
		}


		printf("Case #%d: [", cass);
		if ( m>0) printf("%c", res[0]);
		for (int i=1; i<m; ++i )
			printf(", %c", res[i]);
		puts("]");
	}
	return 0;
}

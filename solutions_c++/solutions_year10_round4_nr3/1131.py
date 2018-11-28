#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

const int MaxN  = 105;

int main(int argc, char **argv)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int c;
	scanf("%d", &c); 
	for(int icase = 0; icase < c; icase++ )
	{
		bool cell[MaxN][MaxN] = {false};
		int r;
		int mx = 0, my = 0;
	
		//memset(cell, false, sizeof(cell));
		scanf("%d", &r);
		int ct = 0;
		for(int i = 0; i < r; i++ )
		{
			int x1, x2, y1, y2;
			scanf("%ld%ld%ld%ld", &x1, &y1, &x2, &y2);
			
			mx = (mx > x2)?mx:x2;
			my = (my > y2)?my:y2;

			for(int x = x1; x <= x2; x++)
				for(int y = y1; y <= y2; y++)
					if(!cell[x][y]){ cell[x][y]=true; ct++; }
		}
		
		int ans = 0;
		while(ct > 0)
		{
			for(int x = mx; x > 0; x--)
			{
				for(int y = my; y > 0; y--)
				{
					if(cell[x][y]){
						if(!cell[x-1][y] && !cell[x][y-1]){
							cell[x][y] =false;ct--;
						}
					}else{
						if(cell[x-1][y] && cell[x][y-1]){
							cell[x][y] =true;	ct++;
						}
					}
				}

			}
			ans++;

		}
		printf("Case #%d: %d\n", icase + 1, ans);

	}

	return 0;
}
#include <iostream>
#include <cmath>
using namespace std;

char ww[500][500];
int w[500][500];

int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		int R,C,D;
		cin >> R >> C >> D;
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				cin >> ww[i][j];
				w[i][j] = ww[i][j]-'0';
			}
		int minimum = R>C?C:R;
		for(int s = minimum; s>=3;s--)
		{
			for(int i=0;i<R+1-s;i++)
				for(int j=0;j<C+1-s;j++)
				{
					int vx=0,vy=0;
					int weight=0;
					for(int k=0;k<s;k++)
					{
						for(int l=0;l<s;l++)
						{
							if(l==0&&(k==0||k==s-1)||l==s-1&&(k==0||k==s-1)) continue;
							weight += (w[i+k][j+l]);
							vx += k * (w[i+k][j+l]);
							vy += l * (w[i+k][j+l]);
						}
					}
					if(((s-1)*weight)%2==0 && vx == (s-1)*weight/2 && vy == (s-1)*weight/2)
					{
						printf("Case #%d: %d\n",c,s);
						goto end;
					}
				}
		}
		printf("Case #%d: IMPOSSIBLE\n",c);
		end:;
	}
}

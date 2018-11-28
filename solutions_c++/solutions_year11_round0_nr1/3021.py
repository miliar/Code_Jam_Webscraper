#include<stdio.h>
#include<vector>

using namespace std;

vector<int> a, b;
vector<int> time1, time2;
int T;
int n;
char jiguna[111];

inline int _abs(int val)
{
	if(val < 0) return -val;
	return val;
}

inline int _min(int v1, int v2)
{
	if(v1 < v2) return v1;
	return v2;
}

int main(void)
{
	int l0, l1;
	int x, y, i, j;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		a.clear();
		b.clear();
		time1.clear();
		time2.clear();
		for(l1=0;l1<n;l1++)
		{
			int temp;

			scanf("%s",jiguna);
			scanf("%d",&temp);
			if(jiguna[0] == 'O')
			{
				a.push_back(temp);
				time1.push_back(l1);
			}
			else
			{
				b.push_back(temp);
				time2.push_back(l1);
			}
		}

		i = 0;
		j = 0;
		x = 1;
		y = 1;
		int ret = 0;
		while(i < a.size() || j < b.size())
		{
			if(i < a.size() && j < b.size())
			{
				int slice1 = _abs(a[i] - x);
				int slice2 = _abs(b[j] - y);

				if(time1[i] < time2[j])
				{
					ret += slice1;
					x = a[i];
					if(slice1 < slice2)
					{
						ret++;
						i++;
						if(y < b[j]) y += slice1 + 1;
						else y -= slice1 + 1;
					}
					else
					{
						y = b[j];
						ret++;
						i++;
					}
				}
				else
				{
					ret += slice2;
					y = b[j];
					if(slice1 > slice2)
					{
						ret++;
						j++;
						if(x < a[i]) x += slice2 + 1;
						else x -= slice2 + 1;
					}
					else
					{
						x = a[i];
						j++;
						ret++;
					}
				}
			}
			else if(i < a.size())
			{
				ret += _abs(a[i] - x);
				x = a[i];
				ret++;
				i++;
			}
			else if(j < b.size())
			{
				ret += _abs(b[j] - y);
				y = b[j];
				ret++;
				j++;
			}
		}
		printf("Case #%d: %d\n",l0,ret);
	}
	return 0;
}
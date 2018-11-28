#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
struct comando
{
	char robo;
	int pos;
};

int main()
{
	int t;
	comando vet[10000];
	scanf("%d",&t);
	int b, o;
	for(int i = 0; i < t; i++)
	{
		b = o = 1;
		int tempo = 0;
		scanf("%d",&n);
		for(int j = 0; j < n; j++)
		{
			scanf(" %c %d",&vet[j].robo, &vet[j].pos);
		}
		for(int j = 0; j < n; j++)
		{
			if(vet[j].robo == 'O')
			{
				tempo += abs(o-vet[j].pos)+1;
				for(int k = j+1; k < n; k++)
				{
					if(vet[k].robo == 'B')
					{
						if(vet[k].pos > b)
						{
							b = min(vet[k].pos, b + abs(o - vet[j].pos)+1);
						}
						else if(vet[k].pos < b)
						{
							b = max(vet[k].pos, b - (abs(o - vet[j].pos)+1));
						}
						break;
					}
				}
				o = vet[j].pos;
			}
			else if(vet[j].robo == 'B')
			{
				tempo += abs(b-vet[j].pos)+1;
				for(int k = j+1; k < n; k++)
				{
					if(vet[k].robo == 'O')
					{
						if(vet[k].pos > o)
						{
							o = min(vet[k].pos, o + abs(b - vet[j].pos)+1);
						}
						else if(vet[k].pos < o)
						{
							o = max(vet[k].pos, o - (abs(b - vet[j].pos)+1));
						}
						break;
					}
				}
				b = vet[j].pos;
			}
		}
		printf("Case #%d: %d\n",i+1,tempo);
	}
	return 0;
}

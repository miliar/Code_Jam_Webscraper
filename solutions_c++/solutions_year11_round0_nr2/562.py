#include <iostream>
#include <set>

using namespace std;

const int mask[8] = { 1, 2, 4, 8, 16, 32, 64, 128 };

int base(char c)
{
	switch(c)
	{
		case 'A': return 0;
		case 'S': return 1;
		case 'D': return 2;
		case 'F': return 3;
		case 'Q': return 4;
		case 'W': return 5;
		case 'E': return 6;
		case 'R': return 7;
		default: return -1;
	}
}

int main()
{
	//freopen("n:/input.txt", "rt", stdin);
	int T; scanf("%d", &T);

	char in[200];
	char out[200];
	
	for(int t=1; t<=T; t++)
	{
		int C,D,N;
		char tmp[5];

		char chan[256], del[256];

		for(int i=0; i<256; i++) chan[i] = del[i] = 0;

		scanf("%d", &C);
		for(int i=0; i<C; i++)
		{
			scanf("%s", tmp);
			int ii = mask[base(tmp[0])];
			int jj = mask[base(tmp[1])];
			chan[ii | jj] = tmp[2];
		}

		scanf("%d", &D);
		for(int i=0; i<D; i++)
		{
			scanf("%s", tmp);
			int ii = mask[base(tmp[0])];
			int jj = mask[base(tmp[1])];
			del[ii | jj] = 255;
		}

		scanf("%d", &N);
		scanf("%s", in);

		int j = 0;

		for(int i=0; i<N; i++)
		{
			out[j] = in[i];
			int jj = base(out[j]);
			
			if(j)
			{
				int ii = base(out[j-1]);

				if(jj!=-1)
				{
					char tt;
					if((ii!=-1) && (tt = chan[mask[ii] | mask[jj]]))
					{
						out[j-1] = tt;
						continue;
					}
					else
					{
						for(int z=0; z<j; z++)
						{
							int zz = base(out[z]);
							if((zz!=-1) && del[ mask[jj] | mask[zz] ])
							{
								j = -1;
								break;
							}
						}
					}
				}
			}

			j++;
		}

		printf("Case #%d: [", t);

		for(int i=0; i<j; i++)
		{
			if(i==j-1)printf("%c", out[i]);
			else printf("%c, ", out[i]);
		}
		printf("]\n");
	}

	return 0;
}
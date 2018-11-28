#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int P;
char W[200];
int Z[200];

int find_next_target(int index, char c)
{
	for(int i=index; i<P; i++)
	{
		if(W[i]==c)
			return Z[i];
	}
	return -1;
}

int main()
{
	freopen("input.txt", "rt", stdin);

	int num;
	scanf("%d", &num);
//printf("num=%d\n", num);

	for (int ii=0; ii<num; ii++)
	{
		int ans=0;
		int O_pos=1;
		int B_pos=1;
		int O_target=0;
		int B_target=0;

		scanf("%d ", &P);
//printf("P=%d\n", P);

		for(int i = 0; i < P; i++)
		{
			scanf(" %c %d", &W[i], &Z[i]);
//printf("%c %d\n", W[i],Z[i]);
		}

		int idx=0;
		char lead=W[idx];
		while(1)
		{
			bool found=0;
			if(idx == P)
				break;
			if(O_target==0)
			{
				O_target = find_next_target(idx,'O');
				if(O_target==-1)
					O_target=O_pos;
			}
			if(B_target==0)
			{
				B_target = find_next_target(idx,'B');
				if(B_target==-1)
					B_target=B_pos;
			}

			if(O_pos < O_target)
			{
				O_pos++;
//printf("O: move %d\n", O_pos);
			}
			else if(O_pos > O_target)
			{
				O_pos--;
//printf("O: move %d\n", O_pos);
			}
			else
			{
				if(lead!='O')
				{
//printf("O: STAY %d\n", O_pos);
				}
				else
				{
//printf("O: PUSH %d\n", O_pos);
					O_target=0;
					found=1;
				}
			}

			if(B_pos < B_target)
			{
				B_pos++;
//printf("B: move %d\n", B_pos);
			}
			else if(B_pos > B_target)
			{
				B_pos--;
//printf("B: move %d\n", B_pos);
			}
			else
			{
				if(lead!='B')
				{
//printf("B: STAY %d\n", B_pos);
				}
				else
				{
//printf("B: PUSH %d\n", B_pos);
					B_target=0;
					found=1;
				}
			}
			if(found)
			{
				idx++;
				lead=W[idx];
				found=0;
			}
			ans++;
		}

		printf("Case #%d: %d\n", ii+1, ans);
	}

	return 0;
}


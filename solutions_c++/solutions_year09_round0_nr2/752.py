#include<iostream>
#include<cstring>
using namespace std;

#define sz 100

int define (int index, int parent[sz*sz])
{
	if (parent[index] == index) return index;
	else parent[index] = define(parent[index], parent);
	return parent[index];
}

int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large-out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int dx[4] = {-1, 0, 0, 1};
	int dy[4] = {0, -1, 1, 0};
	for (int i = 0; i < t; i++)
	{
		int h, w;
		scanf("%d %d", &h, &w);
		int ele[100][100];
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				scanf("%d", &ele[j][k]);
		int parent[sz*sz];
		for (int j = 0; j < sz*sz; j++)
			parent[j] = j;
		int minimum;
		int temp_parent;
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
			{
				temp_parent = -1;
				minimum = ele[j][k];
				for (int dir = 0; dir < 4; dir++)
				{
					int curx = j+dx[dir];
					int cury = k+dy[dir];
					if (curx >= 0 && curx < h && cury >= 0 && cury < w)
						if (ele[curx][cury] < minimum)
						{
							minimum = ele[curx][cury];
							temp_parent = dir;
						}
				}
				if (temp_parent != -1)
					parent[j*sz+k] = (j+dx[temp_parent])*sz + k+dy[temp_parent];
			}
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
				define(j*sz+k, parent);
		int assign[sz*sz];
		memset(assign, -1, sizeof(assign));
		int count = 0;
		for (int j = 0; j < h; j++)
			for (int k = 0; k < w; k++)
			{
				if (assign[parent[j*sz+k]]==-1)
				{
					assign[parent[j*sz+k]] = count; 
					count++;
				}
				assign[j*sz+k] = assign[parent[j*sz+k]];
			}
		printf("Case #%d:\n", i+1);
		for (int j = 0; j < h; j++)
		{
			for (int k = 0; k < w; k++)
				printf("%c ", 'a'+assign[j*sz+k]);
			printf("\n");
		}
	}
	return 0;
}

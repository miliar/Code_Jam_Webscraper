#include <stdio.h>
#include <string.h>

#define INDEX(h,w) ((h)*W+(w))

char res[100][100];
int map[100][100];
int mark[100][100];
int temp[100][100][2];
char label[100 * 100];
int root[2];
int H, W, sum;

void Find(int h, int w)
{
	root[0] = h, root[1] = w;
	int temp_h, temp_w;
	while (temp[root[0]][root[1]][0] >= 0)
	{
		temp_h = temp[root[0]][root[1]][0];
		temp_w = temp[root[0]][root[1]][1];
		root[0] = temp_h;
		root[1] = temp_w;
	}
	while(temp[h][w][0] >= 0)
	{
		temp_h = temp[h][w][0];
		temp_w = temp[h][w][1];
		temp[h][w][0] = root[0];
		temp[h][w][1] = root[1];
		h = temp_h;
		w = temp_w;
	}
}

void Union(int h1, int w1, int h2, int w2)
{
	int sum, root_h1, root_h2, root_w1, root_w2;
	Find(h1, w1);
	root_h1 = root[0];
	root_w1 = root[1];
	Find(h2, w2);
	root_h2 = root[0];
	root_w2 = root[1];
	sum = temp[root_h1][root_w1][0] + temp[root_h2][root_w2][0];

	if(temp[root_h1][root_w1][0] > temp[root_h2][root_w2][0])
	{
		temp[root_h1][root_w1][0] = root_h2;
		temp[root_h1][root_w1][1] = root_w2;
		temp[root_h2][root_w2][0] = sum;
	}
	else
	{
		temp[root_h2][root_w2][0] = root_h1;
		temp[root_h2][root_w2][1] = root_w1;
		temp[root_h1][root_w1][0] = sum;
	}
}

void solve(int index)
{
	int h, w, i, cnt, dst_h, dst_w, dst_d;
	int flag;
	scanf("%d%d", &H, &W);
	for (h = 0; h < H; ++h)
	{
		for (w = 0; w < W; ++w)
		{
			scanf("%d", &(map[h][w]));
		}
	}
	for (h = 0; h < H; ++h)
	{
		for (w = 0; w < W; ++w)
		{
			temp[h][w][0] = -1;
			temp[h][w][1] = -1;
		}
	}
	for (h = 0; h < H; ++h)
	{
		for (w = 0; w < W; ++w)
		{
			mark[h][w] = 0;
		}
	}
	flag = 1;
	while (flag)
	{
		flag = 0;
		for (h = 0; h < H; ++h)
		{
			for (w = 0; w < W; ++w)
			{
				if (mark[h][w] == 1)
					continue;

				dst_h = -1; dst_w = -1; dst_d = map[h][w];
				if (h > 0 && dst_d > map[h - 1][w])
				{
					dst_h = h - 1;
					dst_w = w;
					dst_d = map[h - 1][w];
				}
				if (w > 0 && dst_d > map[h][w - 1])
				{
					dst_h = h;
					dst_w = w - 1;
					dst_d = map[h][w - 1];
				}
				if (w < W - 1 && dst_d > map[h][w + 1])
				{
					dst_h = h;
					dst_w = w + 1;
					dst_d = map[h][w + 1];
				}
				if (h < H - 1 && dst_d > map[h + 1][w])
				{
					dst_h = h + 1;
					dst_w = w;
					dst_d = map[h + 1][w];
				}
				if (dst_h != -1)
				{
					Union(h, w, dst_h, dst_w);
					mark[h][w] = 1;
					flag = 1;
				}
			}
		}
	}

	for (i = 0; i < H * W; ++i)
	{
		label[i] = ' ';
	}
	cnt = 0;
	for (h = 0; h < H; ++h)
	{
		for (w = 0; w < W; ++w)
		{
			Find(h, w);
			if (label[INDEX(root[0], root[1])] == ' ')
			{
				label[INDEX(root[0], root[1])] = 'a' + cnt;
				++cnt;
			}
			res[h][w] = label[INDEX(root[0], root[1])];
		}
	}
	printf("Case #%d:\n", index);
	for (h = 0; h < H; ++h)
	{
		for (w = 0; w < W; ++w)
		{
			printf("%c ", res[h][w]);
		}
		printf("\n");
	}

}

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i;
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
	{
		solve(i + 1);
	}
	return 0;
}

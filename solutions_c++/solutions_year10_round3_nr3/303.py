#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int,int> pii;

#define mp make_pair

char board_hex[515][515];
int R, C, board[515][515];

vector<pii> good_position[515];

int min(int a, int b)
{
	if(a < b) return a;
	return b;
}

// convert to bits and store in board[k][]
void convert(char row[], int k)
{
	int i;

	for(i = 0; i < C/4; ++i)
	{
		int val = 0;
		
		if(row[i] >= '0' && row[i] <= '9')
			val = row[i]-'0';
		else
			val = row[i]-'A'+10;

		int end = (i+1)*4, start = i*4;

		for(int j = end-1; j >= start; --j)
		{
			board[k][j] = val%2;
			val /= 2;
		}
	}
}

bool can_be_taken(int r, int c, int sz)
{
	if(r + sz - 1 >= R || c + sz - 1 >= C)
		return false;

	if(sz == 1) return true;
	
	int mask[2][515];

	for(int r0 = r; r0 <= r+1; ++r0)
	for(int i = c; i < c+sz; ++i)
	{
		mask[r0%2][i-c] = board[r0][i];
		
		if(i > c && mask[r0%2][i-c] == mask[r0%2][i-c-1]) 
			return false;		
	}
	
	int k;

	for(k = 0; k < sz; ++k)
		if(mask[0][k] == mask[1][k])
			return false;

	for(int j = r+2; j < r+sz; ++j)
	{
		for(k = c; k < c+sz; ++k)
		{
			if(mask[j%2][k-c] != board[j][k])
				return false;
		}
	}

	return true;
}

// for each cell calc the max size that can be taken
void pre_process()
{
	for(int r = 0; r < R; ++r)
	{
		for(int c = 0; c < C; ++c)
		{
			for(int sz = min(R,C); sz >= 1; --sz)
			{
				if(can_be_taken(r,c,sz))
				{
					good_position[sz].push_back(mp(r,c));
				}
			}
		}
	}
}

int count_size[515];

bool single_dim_intersects(int a, int b, int u, int v)
{
	return !(u > b || v < a);
}

bool intersects(int r1, int c1, int r2, int c2, int r3, int c3, int r4, int c4)
{
	return single_dim_intersects(r1,r2,r3,r4) && single_dim_intersects(c1,c2,c3,c4);
}

int calc_ans()
{
	int sz;
	for(sz = min(R,C); sz >= 1; --sz)
		sort(good_position[sz].begin(),good_position[sz].end());


	memset(count_size,0,sizeof(count_size));

	// take from the sorted list
	// type   (r, c, size)
	vector< pair<pii,int> > taken;

	for(sz = min(R,C); sz >= 1; --sz)
	{
		for(int i = 0; i < good_position[sz].size(); ++i)
		{
			int r = good_position[sz][i].first, c = good_position[sz][i].second;

			// if doesn't intersect with the prev. taken
			bool take = true;
			int k;
			for(k = 0; k < taken.size(); ++k)
			{
				int r1 = taken[k].first.first, c1 = taken[k].first.second;
				int sz1 = taken[k].second;

				if(intersects(r1,c1,r1+sz1-1,c1+sz1-1, r,c,r+sz-1,c+sz-1))
				{
					take = false;
					break;
				}
			}

			if(take)
			{
				taken.push_back(mp(mp(r,c),sz));
				count_size[sz]++;
			}
		}
	}

	int diff_sizes = 0;

	for(sz = min(R,C); sz >= 1; --sz)
		if(count_size[sz] > 0)
			++diff_sizes;

	return diff_sizes;
}

void initialize()
{
	for(int sz = min(R,C); sz >= 1; --sz)
		good_position[sz].clear();
}	

int main()
{
	freopen("CSmall.in","r",stdin);
	freopen("CSmall.out","w",stdout);

	int T; scanf("%d",&T);

	for(int t = 1; t <= T; ++t)
	{
		scanf("%d%d",&R,&C);

		initialize();

		int i;

		for(i = 0; i < R; ++i)
		{
			scanf("%s",board_hex[i]);
			
			convert(board_hex[i],i);
		}

		pre_process();

		int ans = calc_ans();

		printf("Case #%d: %d\n",t,ans);

		// rest of the answers..
		for(int sz = min(R,C); sz >= 1; --sz)
		{
			if(count_size[sz] > 0)
			{
				printf("%d %d\n",sz,count_size[sz]);
			}
		}
	}

	return 0;
}

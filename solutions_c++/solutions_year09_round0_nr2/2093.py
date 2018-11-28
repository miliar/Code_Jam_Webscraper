/*
 *  Google Code Jam 2009
 *  Qualification Round - Problem B - Watersheds
 */


#include <stdio.h>
#include <string.h>
#include <list>
#include <vector>

using namespace std;
list<pair<int, int> > Q;

#define INPUT_FILE    "input.txt"
#define OUTPUT_FILE   "output.txt"
#define INSIDE(l, c)  ((l) >= 1 && (l) <= H && (c) >= 1 && (c) <= W)
#define MAX(a, b)     ((a) > (b) ? (a) : (b))

int T, H, W;
int A[128][128];
int M[128][128];
char Col[128][128];
		/* N W E S */
int dl[4] = { -1, 0, 0, +1};
int dc[4] = { 0, -1, +1, 0};


/* returns a 4 bit integer with the bit 1 if the neighbour N W E S (1 2 4 8) can flow there */
int WhoCanFlowHere(int l, int c)
{
  int i, j, ret = 0;
  int nl, nc, nnl, nnc;
  int bOKN;

  for (i = 0; i < 4; i++)
    {
      nl = l + dl[i];
      nc = c + dc[i];

      if (!INSIDE(nl, nc))
	continue;

      if (A[nl][nc] > A[l][c])
      {
	bOKN = 1;

	for (j = 0; j < 4; j++)
	  {
	    nnl = nl + dl[j];
	    nnc = nc + dc[j];

	    if (nnl == l && nnc == c)
	      continue;

	    if (!INSIDE(nnl, nnc))
	      continue;

	    /* if the neighbour has another more deeper sink or same deep but 
		better direction (N W E S) */
		/*  direction to (nl, nc) of (l, c) and (nnl, nnc) */
		int dir1 = 3 - i;
		int dir2 = j;
	    if (A[nnl][nnc] < A[l][c] || (A[nnl][nnc] == A[l][c] && dir1 > dir2))
	      {
		bOKN = 0;
		break;
	      }
	  }

	if (bOKN)
	  {
	    ret |= 1 << i;
	  }
      };
    }

  return ret;
}

void Fill(int l, int c, int src, int dst)
{
	int i;

	if (!INSIDE(l, c))
		return;

	if (Col[l][c] == src)
	{
		Col[l][c] = dst;

		for (i = 0; i < 4; i++)
			Fill(l + dl[i], c + dc[i], src, dst);
	}
}

void Solve()
{
  char col = 'A';
  int i, j, k;
  int okSink;

  Q.clear();
  memset(Col, ' ', sizeof(Col));
  memset(M, 0, sizeof(M));

  for (i = 1; i <= H; i++)
    for (j = 1; j <= W; j++)
	{
		M[i][j] = WhoCanFlowHere(i, j);
	}

  /* find the sinks */
  for (i = 1; i <= H; i++)
    for (j = 1; j <= W; j++)
      {
		if (M[i][j] > 0)
		{
			okSink = 1;

			for (k = 0; k < 4; k++)
			{
				int nl = i + dl[k];
				int nc = j + dc[k];

				if (!INSIDE(nl, nc))
					continue;

				if (M[nl][nc] > 0 && A[nl][nc] < A[i][j])
				{
					okSink = 0;
					break;
				}
			}

			if (okSink)
			{
				/* no neighbours in which can also flow water -> sink */
				pair<int, int> sink;

				sink.first = i;
				sink.second = j;

				Q.push_back(sink);

				Col[i][j] = col++;
			}
		}
      }

	int colouring_level = Q.size();
	int l, c, nl, nc;
	/* now expand all these squares until we reach a colouring level of H * W */

	while (colouring_level < H * W && Q.size() > 0)
	{
		pair<int, int> p;

		p = Q.front();
		Q.pop_front();

		l = p.first;
		c = p.second;

		for (i = 0; i <= 3; i++)
		{
			if (M[l][c] & (1 << i))
			{
				nl = l + dl[i];
				nc = c + dc[i];

				if (Col[nl][nc] == ' ')
				{
					Col[nl][nc] = Col[l][c];
					pair<int, int> np;

					np.first = nl;
					np.second = nc;

					Q.push_back(np);
					colouring_level++;
				}
			}
		}
	}

	for (i = 1; i <= H; i++)
		for (j = 1; j <= W; j++)
		{
			if (Col[i][j] == ' ')
				Col[i][j] = col++;
		}

	/* reordering */
	col = 'a';
	for (i = 1; i <= H; i++)
		for (j = 1; j <= W; j++)
			if (Col[i][j] >= 'A' && Col[i][j] <= 'Z')
			{
				/* change all cells with col[i][j] with col*/
				Fill(i, j, Col[i][j], col);
				col++;
			};

	/* print */
	for (i = 1; i <= H; i++, printf("\n"))
		for (j = 1; j <= W; j++)
		{
			printf("%c ", Col[i][j]);
		}
}

int main()
{
  int i, j, k;

  freopen(INPUT_FILE, "rt", stdin);
  freopen(OUTPUT_FILE, "wt", stdout);

  scanf("%ld", &T);

  for (k = 0; k < T; k++)
    {
      scanf("%ld %ld", &H, &W);

      for (i = 1; i <= H; i++)
	for (j = 1; j <= W; j++)
	  {
	    scanf("%ld", &A[i][j]);
	  };
      
      printf("Case #%d: \n", k + 1);
      Solve();
    }

  fclose(stdout);
  fclose(stdin);

  return 0;
}

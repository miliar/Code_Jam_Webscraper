#include <cstdio>
#include <algorithm>
using namespace std;
#define NN 502
int col[NN][NN],row[NN][NN],map[NN][NN];
char map1[NN][NN];

void add(pair<int,int> &p, int d, int r, int c, int cr, int cc)
{
	p.first += (r-cr)*d;
	p.second += (c-cc)*d;
}

int main()
{
	int t,i,r,c,d,k,j,ii,jj,cr,cc,maxk;
	pair<int,int> p;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int cas=1; cas<=t; cas++)
	{
		scanf("%d%d%d",&r,&c,&d);
		for (i=0; i<r; i++) scanf("%s",map1[i]);
		for (i=0; i<r; i++) for (j=0; j<c; j++) map1[i][j]-='0';
		for (i=0; i<r*2; i++) for (j=0; j<c*2; j++)
		{
			if (i%2==0 && j%2==0) map[i][j]=map1[i/2][j/2];
			else map[i][j]=0;
		}
		maxk=2;
		for (i=0; i<r*2; i+=2) for (j=0; j<c*2; j+=2)
		{
			for (k=3; i+2*k<=2*r && j+2*k<=2*c; k++)
			{
				cr = i+k-1;
				cc = j+k-1;
				p.first=0; p.second=0;
				for (ii=i; ii<i+2*k; ii+=2) for (jj=j; jj<j+2*k; jj+=2)
				{
					if (ii==i && (jj==j || jj==j+2*k-2)) continue;
					if (ii==i+2*k-2 && (jj==j || jj==j+2*k-2)) continue;
					add(p,map[ii][jj]+d,ii,jj,cr,cc);
				}
//				if (i==2 && j==2 && k==5) printf("%d %d\n",p.first,p.second);
				if (p.first==0 && p.second==0 && maxk<k) maxk=k;
			}
		}
		if (maxk>=3) printf("Case #%d: %d\n",cas,maxk);
		else printf("Case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}

/*
		for (i=0; i<r; i++)
		{
			row[i][0]=map[i][0];
			for (j=1; j<c; j++) row[i][j]=map[i][j]+row[i][j-1];
		}
		for (i=0; i<c; i++)
		{
			col[i][0]=map[0][i];
			for (j=1; j<r; j++) col[i][j]=col[i][j-1]+map[j][i];
		}
		maxk=2;
		for (i=0; i<r; i++) for (j=0; j<c; j++)
		{
			up = down = left = right = 0;
			for (k=3; i+k<=r && j+k<=c; k++)
			{
				if (k%2==0)
				{
					ra = i+k/2-1;
					co = j+k/2-1;
					if (j>0) up += row[ra][j+k-1]-row[ra][j-1];
					else up += row[ra][j+k-1];
					up += col[j+k-1][ra-1]-col[j+k-1][i];
					up += map[i][j+k-2];
					down += row[i+k-1][j+k-2]-row[i+k-1][j];
					down += map[i+k-2][j]+map[i+k-2][j+k-2] + col[j+k-1][i+k-2]-col[j+k-1][ra];

					if (i>0) left += col[co][i+k-1] - col[co][i-1];
					else left += col[co][i+k-1];
					left += map[i+k-2][j] + row[i+k-1][co-1]-row[i+k-1][j];
					right += col[j+k-1][i+k-2]-col[j+k-1][i];
					right += map[i][j+k-2] + map[i+k-2][j+k-2];
					right += row[i+k-1][j+k-2] - row[i+k-1][co];
				} else {
					ra = i+k/2-1;
					co = j+k/2-1;
					up += col[j+k-1][ra] - col[j+k-1][i] + map[i][j+k-2];
					down += row[i+k-1][j+k-2]-row[i+k-1][j];
					down += map[i+k-2][j]+map[i+k-2][j+k-2] + col[j+k-1][i+k-2]-col[j+k-1][ra];
					if (j>0) down -= row[ra+1][j+k-1]-row[ra+1][j-1];
					else down -= row[ra+1][j+k-1];

					left += map[i+k-2][j] + row[i+k-1][co]-row[i+k-1][j];
					right += col[j+k-1][i+k-2]-col[j+k-1][i];
					right += map[i][j+k-2]+map[i+k-2][j+k-2]+row[i+k-1][j+k-2]-row[i+k-1][co];
					if (i>0) right -= col[co+1][i+k-1]-col[co+1][i-1];
					else right -= col[co+1][i+k-1];
				}
	//			if (i==1 && j==1 && k==5) printf("%d %d %d %d\n",up,down,left,right);
				if (up==down && left==right && maxk<k) maxk = k;
			}
		}
		*/
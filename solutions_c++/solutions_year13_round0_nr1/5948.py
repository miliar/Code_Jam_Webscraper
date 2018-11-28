#include <cstdio>

char c;
int lin[4][2];
int col[4][2];
int diag[2][2];
bool X,O,end;

int main()
{
	int n;
	scanf(" %d",&n);
	for(int i=1; i<=n; i++)
	{
		end = true;
		for(int j=0; j<2; j++)
			lin[0][j] = lin[1][j] = lin[2][j] = lin[3][j] = col[0][j] = col[1][j] = col[2][j] = col[3][j] = diag[0][j] = diag[1][j] = 0;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
			{
				scanf(" %c",&c);
				if(c=='.') {end = false;continue;}
				if(c=='O' || c=='T')
				{
					lin[j][0]++;
					col[k][0]++;
					if(k==j) diag[0][0]++;
					if(k+j==3) diag[1][0]++;
				}
				if(c=='X' || c=='T')
				{
					lin[j][1]++;
					col[k][1]++;
					if(k==j) diag[0][1]++;
					if(k+j==3) diag[1][1]++;
				}
			}
		X = (diag[0][1]==4) || (diag[1][1]==4);
		O = (diag[0][0]==4) || (diag[1][0]==4);
		for(int j=0; (!O) && (!X) && j<4; j++)
		{
			X = X || (lin[j][1]==4) || (col[j][1]==4);
			O = O || (lin[j][0]==4) || (col[j][0]==4);
		}
		printf("Case #%d: %s\n", i, X?"X won":(O?"O won":(end?"Draw":"Game has not completed")));
	}
	return 0;
}

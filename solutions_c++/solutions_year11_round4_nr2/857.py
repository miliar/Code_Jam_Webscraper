#include<cstdio>
#include<utility>
#include<algorithm>
using namespace std;

char dden[501][501];
long long int den[501][501];
//char den[501][501];
int sprawdz(int y, int x, int k)
{
	long long int px = 0;
	long long int py = 0;
	for (int i=y-k; i<=y+k; i++)
		for (int j=x-k; j<=x+k; j++)
		{
			py += (y-i)*den[i][j];
			px += (x-j)*den[i][j];
		}
	py -= k*den[y-k][x-k];
	py += k*den[y+k][x-k];
	py -= k*den[y-k][x+k];
	py += k*den[y+k][x+k];
	
	px -= k*den[y-k][x-k];
	px -= k*den[y+k][x-k];
	px += k*den[y-k][x+k];
	px += k*den[y+k][x+k];
	return ((px==0) && (py==0));
}
int sprawdz2(int y, int x, int k)
{
	long long int px = 0;
	long long int py = 0;
	for (int i=y-k; i<=y+k+1; i++)
		for (int j=x-k; j<=x+k+1; j++)
		{
			py += (2*y-2*i+1)*den[i][j];
			px += (2*x-2*j+1)*den[i][j];
		}
	py -= (2*k+1)*den[y-k][x-k];
	py += (2*k+1)*den[y+k+1][x-k];
	py -= (2*k+1)*den[y-k][x+k+1];
	py += (2*k+1)*den[y+k+1][x+k+1];
	
	px -= (2*k+1)*den[y-k][x-k];
	px -= (2*k+1)*den[y+k+1][x-k];
	px += (2*k+1)*den[y-k][x+k+1];
	px += (2*k+1)*den[y+k+1][x+k+1];
	return ((px==0) && (py==0));
}

int licz(int r, int c, int d)
{
	int wynik = 0;
        for (int i=1; i<r-1; i++)
                for (int j=1; j<c-1; j++)
		{
			int mlen = i;
			if (j < mlen)
				mlen = j;
			if (r-i-1 < mlen)
				mlen = r-i;
			if (c-j-1 < mlen)
				mlen = c-j;
			int ww = 0;
			for (int k=mlen; k>0; k--)
			{
				if (i+k+1<r && j+k+1 < c && sprawdz2(i,j,k))
				{
					ww = 2*k+2;
					break;
				}
				if (sprawdz(i,j,k))
				{
					ww = 2*k+1;
					break;
				}
			}	

        		if (ww > wynik)
				wynik = ww;      
  //                      if (wynik == r/2 || wynik == c/2)
//				return wynik;
                }
	return wynik;
}

int main()
{
        int tests;
        int wynik,r,c,d;
        scanf("%d",&tests);
        for (int tt=1; tt<=tests; tt++)
        {
                scanf("%d %d %d",&r,&c,&d);
                wynik = 0;
                for (int i=0; i<r; i++)
		{
                        scanf("%s",dden[i]);
			for (int j=0; j<c; j++)
				den[i][j] = dden[i][j] + d - '0';
		}

                wynik = licz(r,c,d);
		if (wynik >= 3)
	                printf("Case #%d: %d\n",tt,wynik);
		else
			printf("Case #%d: IMPOSSIBLE\n",tt);
        }

}

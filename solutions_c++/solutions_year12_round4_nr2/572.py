# include <stdio.h>
# include <stdlib.h>


typedef struct CIR{
	double r ;
	int num ;
}CIR ;


CIR cir[1010] ;
double x[1010], y[1010] ;
double xx[1010], yyy[1010] ;


int cmp(const void *a, const void *b)
{
	CIR *p = (CIR*)a, *q = (CIR*)b ;
	if (p->r > q->r) return -1 ;
	if (p->r < q->r) return 1 ;
	return 0 ;
}


int main ()
{
	int T, w, l, n , i ;
	int r ;
	int nCase = 1 ;
	freopen ("B-large.in", "r", stdin) ;
	freopen ("boutlarge.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%d%d%d", &n, &w, &l) ;
		for (i = 0 ; i < n ; i++)
		{
			scanf ("%d", &r) ;
			cir[i].r = r + 0.01 ;
			cir[i].num = i ;
		}
		qsort(cir, n, sizeof(cir[0]), cmp) ;
		
		int flag = 0 ;
		double ww = w ;
		double max_d = 0 ;
		double cc = 0, yy = 0 ;
		
		
		for (i = 0 ; i < n ; i++)
		{
			if (flag == 0){
				if (cc == 0 ){
					yy = 0 ;
					cc += cir[i].r;
				}
				else {
					yy = cc + cir[i].r ;
					cc += cir[i].r * 2 ;
				}
				x[i] = ww ;
				y[i] = yy ;
				ww -= cir[i].r ;
				flag = 1 ;
				max_d = cir[i].r*2 ;
			}
			else if (flag == 1)
			{
				if (ww >= cir[i].r*2)
				{
					x[i] = ww - cir[i].r ;
					y[i] = yy  ;
					ww -= cir[i].r*2 ;
					if (cir[i].r*2> max_d) max_d = cir[i].r*2 ;
				}
				else
				{
					if (ww >= cir[i].r)
					{
						x[i] = 0 ;
						y[i] = yy ;
						if (cir[i].r*2> max_d) max_d = cir[i].r*2 ;
						flag = 0 ;
						ww = w ;
					}
					else{
						flag = 0 ;
						i-- ;
						ww = w ;
					}
				}
			}
		}
		printf ("Case #%d: ", nCase++) ;
		for (i = 0 ; i < n ; i++){
			xx[cir[i].num] = x[i] ;
			yyy[cir[i].num] = y[i] ;
		}
		for (i = 0 ; i < n  ;i++)
			printf ("%lf %lf ", xx[i], yyy[i]) ;
		printf ("\n") ;
	}
	
	return 0 ;
}

#include <stdio.h>
#define debug(x) 
char table[105][105];
int win[105],lose[105];
double wp[105];
double owp[105];
double oowp[105];
double rpi[105];
double calcWp(int w,int l) { if (w+l) return double(w)/(w+l); return 0.; }
int main()
{
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int n;
		scanf("%d",&n);
		for (int q=0;q<n;++q)
			scanf("%s",table[q]);
		for (int q=0;q<n;++q)
		{
			win[q]=lose[q]=0;
			for (int e=0;e<n;++e)
			{
				if (table[q][e]=='1') win[q]++;
				else if (table[q][e]=='0')  lose[q]++;
			}
			wp[q] = calcWp(win[q],lose[q]);
		}
		for (int q=0;q<n;++q)
		{
			double avg = 0;
			int k = 0;
			for (int w=0;w<n;++w)
			{
				if (table[q][w]=='.') continue;
				int wc = win[w], lc = lose[w];
				if (table[w][q]=='1') wc--;
				if (table[w][q]=='0') lc--;
				avg += calcWp(wc,lc);
				k++;
			}
			if (k) avg /= k;
			owp[q] = avg;
		}
		for (int q=0;q<n;++q)
		{
			double avg = 0;
			int k =0;
			for (int w=0;w<n;++w)
			{
				if (table[q][w]=='.') continue;
				avg += owp[w];
				k++;
			}
			if (k) avg/=k;
			oowp[q] = avg;
		}
		printf("Case #%d:\n",kase);
		for (int q=0;q<n;++q) 
		{
			debug(printf("wp:%.4lf owp:%.4lf oowp:%.4lf\n",wp[q],owp[q],oowp[q]));
			printf("%.8lf\n",wp[q]/4. + owp[q]/2. + oowp[q]/4.);
			
		}
	}
	return 0;
}

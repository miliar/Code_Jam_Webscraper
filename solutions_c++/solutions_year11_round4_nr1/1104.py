#include<stdio.h>

double cc;
#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}

const int MAXN = 100000;

int T;
int n;
double len[MAXN], w[MAXN];
double gain[MAXN];
double ret = 0;

double X, walk, run, canrun;
double bonus;
double OKOK;

const double EPS = 1e-12;

void Go(void)
{
	int l1, l2;

	double curr;
	for(l1=0;l1<n;l1++)
	{
		for(l2=l1+1;l2<n;l2++)
		{
			if(gain[l1] < gain[l2])
			{
				Swap(len[l1], len[l2]);
				Swap(w[l1], w[l2]);
				Swap(gain[l1], gain[l2]);
			}
		}
	}

	canrun = OKOK;

	curr = 0;
	for(l1=0;l1<n;l1++)
	{
		double req = len[l1] / (run + w[l1]);

		if(canrun+EPS >= req)
		{
			curr += req;
			canrun -= req;
		}
		else
		{
			double other = len[l1] - canrun * (run + w[l1]);

			curr += canrun + other / (walk + w[l1]);
			canrun = 0;
		}
	}
	if(curr < ret) ret = curr;
}

int main(void)
{
	int l0, l1, l2, l3;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);
	

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%lf",&X);
		scanf("%lf",&walk);
		scanf("%lf",&run);
		scanf("%lf",&canrun);
		scanf("%d",&n);
		for(l1=0;l1<n;l1++)
		{
			double v1, v2;
			scanf("%lf %lf %lf",&v1,&v2,&w[l1]);
			len[l1] = v1 - v2;
			if(len[l1] < 0) len[l1] = -len[l1];
		}

		bonus = 0;
		for(l1=0;l1<n;l1++)
		{
			bonus += len[l1];
		}
		len[n] = X - bonus;
		w[n] = 0;
		n++;
		bonus = 0;

		ret = 1e100;

		OKOK = canrun;

		for(l1=0;l1<n;l1++) gain[l1] = len[l1] / (run+w[l1]) / (walk+w[l1]);
		Go();
		for(l1=0;l1<n;l1++) gain[l1] = 1 / (run+w[l1]) / (walk+w[l1]);
		Go();
		for(l1=0;l1<n;l1++) gain[l1] = w[l1];
		Go();
		for(l1=0;l1<n;l1++) gain[l1] = -len[l1] / (run+w[l1]) / (walk+w[l1]);
		Go();
		for(l1=0;l1<n;l1++) gain[l1] = -1 / (run+w[l1]) / (walk+w[l1]);
		Go();
		for(l1=0;l1<n;l1++) gain[l1] = -w[l1];
		Go();

		for(l1=0;l1<n;l1++) gain[l1] = -w[l1];
		Go();

		printf("Case #%d: %.10lf\n",l0,ret);

		// ret += (X - bonus) / walk;
		
	}
}
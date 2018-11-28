#include<stdio.h>
#include<stdlib.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
#define DSwap(Daa,Dbb) {Dcc=Daa;Daa=Dbb;Dbb=Dcc;}

int n;
double W, L;
double a[11111];
double Dcc;
int order[11111];
int T;
int cc;
int CASE;

int reversed;

const double EPS = 1e-12;

double retx[11111], rety[11111];
double showx[11111], showy[11111];

void Shuffle(void)
{
	int l1, t1, t2;

	if(rand() & 1)
	{
		reversed = 1 - reversed;
		DSwap(W,L);
	}

	for(l1=0;l1<n;l1++)
	{
		t1 = rand() % n;
		t2 = rand() % n;
		Swap(order[t1], order[t2]);
		DSwap(a[t1], a[t2]);
	}
}

int Go(void)
{
	int l1, l2, l3, l4;
	int iter = 0;

	for(l1=0;l1<n;l1++)
	{
		double curr = 0;
		curr = -a[l1];
		for(l2=l1;l2<n;l2++)
		{
			if(curr + a[l2] > W + EPS) break;
			if(iter & 1)
			{
				retx[l2] = curr + a[l2];
				rety[l2] = 0;
				curr += a[l2] + a[l2];
			}
			else
			{
				retx[l2] = W - curr - a[l2];
				rety[l2] = 0;
				curr += a[l2] + a[l2];
			}
		}
		iter++;

		for(l3=l1;l3<l2;l3++)
		{
			for(l4=0;l4<l3;l4++)
			{
				if(retx[l3] - a[l3] >= retx[l4] + a[l4] - EPS) continue;
				if(retx[l3] + a[l3] <= retx[l4] - a[l4] + EPS) continue;
				if(rety[l3] < rety[l4] + a[l3] + a[l4])
				{
					rety[l3] = rety[l4] + a[l3] + a[l4];
				}
				if(rety[l3] > L+EPS) return 0;
			}
		}
		l1 = l2 - 1;
	}
	for(l1=0;l1<n;l1++)
	{
		showx[order[l1]] = retx[l1];
		showy[order[l1]] = rety[l1];
	}
	printf("Case #%d: ",CASE);
	for(l1=0;l1<n;l1++)
	{
		if(reversed == 0)
		{
			printf("%.10lf %.10lf ",showx[l1],showy[l1]);
		}
		else
		{
			printf("%.10lf %.10lf ",showy[l1],showx[l1]);
		}
	}
	printf("\n");
	return 1;
}

int main(void)
{
	int l0, l1, l2, l3;

	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	scanf("%d",&T);

	for(l0=0;l0<T;l0++)
	{
		CASE = l0 + 1;
		fprintf(stderr,"%d %d\n",l0,T);
		scanf("%d",&n);
		scanf("%lf %lf",&W,&L);
		reversed = 0;

		for(l1=0;l1<n;l1++) scanf("%lf",&a[l1]);
		for(l1=0;l1<n;l1++) order[l1] = l1;

		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		for(l1=0;l1<n;l1++)
		{
			for(l2=l1+1;l2<n;l2++)
			{
				if(a[l1] < a[l2])
				{
					DSwap(a[l1], a[l2]);
					Swap(order[l1], order[l2]);
				}
			}
		}
		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		for(l1=0;l1<n;l1++)
		{
			for(l2=l1+1;l2<n;l2++)
			{
				if(a[l1] > a[l2])
				{
					DSwap(a[l1], a[l2]);
					Swap(order[l1], order[l2]);
				}
			}
		}
		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		if(Go()) continue;

		reversed = 1 - reversed;
		DSwap(W, L);

		while(1)
		{
			Shuffle();
			if(Go()) break;
		}
	}
}
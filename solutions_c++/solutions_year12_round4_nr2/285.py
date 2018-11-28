#include<stdio.h>
#include<algorithm>
#include<math.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int T,t;
int N;
double W,L;
struct Rad
{
	double x,y;
	int n;
	double r;
	bool operator()(Rad a,Rad b)
	{
		if(a.r!=b.r) return a.r>b.r;
		if(a.n!=b.n) return a.n<b.n;
	}
};
Rad R2[6001];
Rad Ans[6001];
double R[6001];
double Dis(double ax,double ay,double bx,double by)
{
	return sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by));
}
bool check(Rad a,Rad b)
{
	if(Dis(a.x,a.y,b.x,b.y)<a.r+b.r) return 0;
	return 1;
}
int main()
{
	fscanf(in,"%d",&T);
	int i,j,first;
	int pos;
	double Sx,Sy,Ex,Ey;
	double x,y;
	double Max;
	for(t=1;t<=T;t++)
	{
		fscanf(in,"%d %lf %lf",&N,&W,&L);
		for(i=1;i<=N;i++) fscanf(in,"%lf",&R2[i].r),R2[i].n=i;
		std::sort(R2+1,R2+1+N,Rad());
		for(i=1;i<=N;i++) R[i]=R2[i].r;
		x=y=pos=0;
		i=1;
		Sx=Sy=0; Ex=W; Ey=L;
		while(i<=N)
		{
			first=i;
			Max=0;
			for(;i<=N;i++)
			{
				if(i!=first) x+=R[i];
				if(Sx<=x&&x<=Ex&&Sy<=y&&y<=Ey)
				{
					if(Max<R[i]) Max=R[i];
					Ans[R2[i].n].x=x; Ans[R2[i].n].y=y; Ans[R2[i].n].r=R[i];
					x+=R[i];
				}
				else break;
			}
			if(i==N+1) break;
			Sy+=(Max+R[i]);
			x=0; y=Sy;
		}
		fprintf(out,"Case #%d: ",t);
		for(j=1;j<=N;j++)
		{
			fprintf(out,"%.3lf %.3lf ",Ans[j].x,Ans[j].y);
		}
		fprintf(out,"\n");
	}
}
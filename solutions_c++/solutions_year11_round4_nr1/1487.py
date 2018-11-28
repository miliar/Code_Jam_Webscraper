#include <iostream>
#include <cstdio>
using namespace std;
typedef struct osman
{
	int Bi,Ei,Wi;
}node;
int T,N,S,R,X;
double t;
node a[5002];
int main(void)
{
	int i,j,q,w;
	int Bi,Ei,Wi;
	int siradaki=0;
	long double result=0;
	int threshold=0;
	double val=0;
	int speed;
	double var;
	double sectorun;
	scanf(" %d",&T);
	for(i=1;i<=T;i++)
	{
		result=0;
		threshold=0;
		siradaki=2;
		val=0;
		scanf(" %d %d %d %lf %d",&X,&S,&R,&t,&N);
		scanf(" %d %d %d",&Bi,&Ei,&Wi);
		a[0].Bi=0;a[0].Ei=Bi;a[0].Wi=0;
		a[1].Bi=Bi;a[1].Ei=Ei;a[1].Wi=Wi;
		int oldei=Ei;
		for(j=2;j<N+1;j++)
		{
			scanf(" %d %d %d",&Bi,&Ei,&Wi);
			if(oldei!=-1 && oldei!=Bi)
			{
				a[siradaki].Bi=oldei;a[siradaki].Ei=Bi;a[siradaki].Wi=0;
				siradaki++;
			}
			a[siradaki].Bi=Bi;a[siradaki].Ei=Ei;a[siradaki].Wi=Wi;
			oldei=Ei;
			siradaki++;
		}
		
		a[siradaki].Bi=Ei;a[siradaki].Ei=X;a[siradaki].Wi=0;
		siradaki++;
		double eski=0;
		
		/*for(j=0;j<siradaki;j++)
		{
			cout<<a[j].Bi<<" "<<a[j].Ei<<" "<<a[j].Wi<<endl;
		}
		return 0;*/
		for(threshold=0;threshold<=1000;threshold++)
		{
			val=0;
			for(j=0;j<siradaki;j++)
			{
				if(a[j].Wi<=threshold) val=val+(a[j].Ei-a[j].Bi)/(long double)(a[j].Wi+R);
			}
			if(val>=t) 
			{
				sectorun=t-eski;
				break;
			}
			eski=val;
		}
		//cout<<"\n\n*********"<<threshold<<endl;
		for(j=0;j<siradaki;j++)
		{
			if(a[j].Wi<threshold) 
			{
				speed=a[j].Wi+R;
				//cout<<"Speed: "<<speed<<" Ei-Bi= "<<a[j].Ei-a[j].Bi<<endl;
				result=result+(double)((double)(a[j].Ei-a[j].Bi)/(long double)speed);
				t=t-((a[j].Ei-a[j].Bi)/(long double)speed);
			}
			if(a[j].Wi>threshold)
			{
				//if(j==2) cout<<"j=2! "<<result<<endl;
				speed=S+a[j].Wi;
				result=result+((a[j].Ei-a[j].Bi)/(long double)speed);
				//if(j==2) cout<<"j=2! "<<result<<endl;
			}
			if(a[j].Wi==threshold)
			{
				speed=a[j].Wi+R;
				var=sectorun*(double)speed+a[j].Bi;
				if(var>=a[j].Ei)
				{
					result=result+((a[j].Ei-a[j].Bi)/(long double)speed);
					sectorun=sectorun-((a[j].Ei-a[j].Bi)/(long double)speed);
				}
				else
				{
					//cout<<"ananzaaaaxdxd"<<endl;
					result=result+((var-a[j].Bi)/(long double)speed);
					sectorun=0;
					speed=S+a[j].Wi;
					result=result+((a[j].Ei-var)/(long double)speed);
				}
			}
			//cout<<"\n"<<"Result: "<<result<<" j: "<<j<<" threshold: "<<threshold<<" a begin,end: "<<a[j].Bi<<" "<<a[j].Ei<<" "<<a[j].Wi<<" t: "<<sectorun<<endl;
		}
		printf("Case #%d: %.15Lf\n",i,result);
	}
	return 0;
}

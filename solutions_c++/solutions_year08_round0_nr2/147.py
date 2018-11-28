#include <iostream>
#include <cmath>
using namespace std;

long casen,n,m,mi,h;
char c;
long i,j,t,na,nb,k;
struct trip
{
	long dir;
	long dep,arr;
	long father;
}tr[300];
bool suc;

int cmp(const void * xx,const void * yy)
{
	if (((trip *)xx)->dep<((trip *)yy)->dep) return -1;
	else if (((trip *)xx)->dep>((trip *)yy)->dep) return +1;
	else return 0;
}

int main()
{
	freopen("b2.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>casen;
	for (k=1;k<=casen;k++)
	{
		cin>>t;
		cin>>n>>m;
		for (i=0;i<n+m;i++)
		{
			cin>>h>>c>>mi;
			tr[i].dep=h*60+mi;
			cin>>h>>c>>mi;
			tr[i].arr=h*60+mi;
			tr[i].father=-1;
			if (i<n) tr[i].dir=1;
			else tr[i].dir=-1;
		}
		qsort(tr,n+m,sizeof(trip),cmp);
		for (i=0;i<n+m-1;i++)
		{
			j=i+1;
			suc=false;
			while (j<n+m && suc==false)
			{
				if (tr[i].dir*tr[j].dir==-1 && tr[i].arr+t<=tr[j].dep && tr[j].father==-1)
				{
					tr[j].father=i;
					suc=true;
				}
				j++;
			}
		}
		na=0;nb=0;
		for (i=0;i<n+m;i++) if (tr[i].father==-1)
		{
			if (tr[i].dir==1) na++;
			else nb++;
		}
		cout<<"Case #"<<k<<": "<<na<<' '<<nb<<endl;
	}
	return 0;
}





			
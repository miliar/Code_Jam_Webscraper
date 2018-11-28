#include<iostream>
#include<algorithm>
using namespace std;
#define num 21
int na,nb,t,ans1,ans2;
struct time
{
	int h,m;
};

time astart[num],astop[num],bstart[num],bstop[num];

bool cmp(const time &a,const time &b)
{
	if(a.h<b.h)  return true;
	if(a.h>b.h) return false;
	if(a.m<=b.m)  return true;
	return false;
}

int main()
{
	int i,j,n,cases;
	cin>>n;
	for(cases=1;cases<=n;cases++)
	{
		cin>>t;
		cin>>na>>nb;
		for(i=1;i<=na;i++)
		{
			cin>>astart[i].h;
			getchar();
			cin>>astart[i].m;

			cin>>astop[i].h;
			getchar();
			cin>>astop[i].m;
			
			astop[i].m+=t;
			if(astop[i].m>=60)
			{
				astop[i].h++;
				astop[i].m%=60;
			}
		}

		for(i=1;i<=nb;i++)
		{
			cin>>bstart[i].h;
			getchar();
			cin>>bstart[i].m;

			cin>>bstop[i].h;
			getchar();
			cin>>bstop[i].m;

			bstop[i].m+=t;
			if(bstop[i].m>=60)
			{
				bstop[i].h++;
				bstop[i].m%=60;
			}
		}

		sort(astart+1,astart+na+1,cmp);
		sort(astop+1,astop+na+1,cmp);
		sort(bstart+1,bstart+nb+1,cmp);
		sort(bstop+1,bstop+nb+1,cmp);

		ans1=ans2=0;
		for(i=1,j=1;i<=na;i++)
		{
			if(j>nb)
			{
				ans1++;
				continue;
			}
			if( cmp(bstop[j],astart[i]) )
			{
				j++;
			}
			else
			{
				ans1++;
			}
		}

		for(i=1,j=1;i<=nb;i++)
		{
			if(j>na)
			{
				ans2++;
				continue;
			}
			if( cmp(astop[j],bstart[i]) )
			{
				j++;
			}
			else
			{
				ans2++;
			}
		}
		cout<<"Case #"<<cases<<": "<<ans1<<' '<<ans2<<endl;
	}
	system("pause");
	return 0;
}
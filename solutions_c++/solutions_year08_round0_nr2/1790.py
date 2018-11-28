#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int a[100][2],b[100][2],na,nb,t;

void drive(char ch,int i,int j)
{
	int k;

	if (i==na) {b[j][0]=-1;return;}
	if (j==nb) {a[i][0]=-1;return;}
	if (ch=='a')
	{
		for (k=0;k<na;k++)
		{
			if (b[j][1]+t<=a[k][0]&&a[k][0]!=-1)
			{
				b[j][0]=-1;
				drive('b',k,j);
				break;
			}
		}
		b[j][0]=-1;
	}
	else
	{
		for (k=0;k<nb;k++)
		{
			if (a[i][1]+t<=b[k][0]&&b[k][0]!=-1)
			{
				a[i][0]=-1;
				drive('a',i,k);
				break;
			}
		}
		a[i][0]=-1;
	}
	return;
}

void driving(int i,int j)
{
	int k;

	while (a[i][0]==-1) i++;
	while (b[j][0]==-1) j++;
	if (i==na) {b[j][0]=-1;return;}
	if (j==nb) {a[i][0]=-1;return;}
	if (a[i][0]<=b[j][0])
	{
		for (k=0;k<nb;k++)
		{
			if (a[i][1]+t<=b[k][0]&&b[k][0]!=-1)
			{
				a[i][0]=-1;
				drive('b',i,k);
				break;
			}
		}
		a[i][0]=-1;
	}
	else
	{
		for (k=0;k<na;k++)
		{
			if (b[j][1]+t<=a[k][0]&&a[k][0]!=-1)
			{
				b[j][0]=-1;
				drive('a',k,j);
				break;
			}
		}
		b[j][0]=-1;
	}
}



int compare(const void *p1,const void *p2 )
{
	int i;
	for (i=0;i<2;i++)
	{
		if (*((int *)p1+i)!=*((int *)p2+i)) return *((int *)p1+i)-*((int *)p2+i);
	}
	return 0;
}

int main()
{
	int n,i,j,k=1,ka,kb;
	string str;

	for (cin>>n;n>0;n--)
	{
		ka=kb=0;
		for (i=0;i<100;i++) a[i][0]=a[i][1]=b[i][0]=b[i][1]=0;
		cin>>t;
		cin>>na>>nb;
		for (i=0;i<na;i++)
		{
			cin>>str;
			a[i][0]=((str[0]-'0')*10+str[1]-'0')*60+(str[3]-'0')*10+str[4]-'0';
			cin>>str;
			a[i][1]=((str[0]-'0')*10+str[1]-'0')*60+(str[3]-'0')*10+str[4]-'0';
		}
		for (i=0;i<nb;i++)
		{
			cin>>str;
			b[i][0]=((str[0]-'0')*10+str[1]-'0')*60+(str[3]-'0')*10+str[4]-'0';
			cin>>str;
			b[i][1]=((str[0]-'0')*10+str[1]-'0')*60+(str[3]-'0')*10+str[4]-'0';
		}
		if (na==0||nb==0) {cout<<"Case #"<<k++<<": "<<na<<' '<<nb<<endl;continue;}
		qsort(a,na,sizeof(int)*2,compare);
		qsort(b,nb,sizeof(int)*2,compare);
		i=j=0;
		while (!(i==na&&j==nb))
		{
			if ((a[i][0]<=b[j][0]&&i!=na)||j==nb) ka++;
			else kb++;
			driving(i,j);
			while (a[i][0]==-1) i++;
			while (b[j][0]==-1) j++;
		}
		cout<<"Case #"<<k++<<": "<<ka<<' '<<kb<<endl;
	}
	return 0;
}
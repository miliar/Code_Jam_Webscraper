#include<iostream>
#include<cstdio>
#include<map>
#include<string>
#include<deque>
#include<cmath>
#include<map>
using namespace std;
int cek(deque<int> d,deque<int> d2);
deque<int> ubah(int a);
int main()
{
	int n,i,j,k,a,w,jum=0;
	deque<int> d[1001];
	map<int,int> m[1001];
	//getline(cin,c);
	for(j=1;j<=1000;j++)
			d[j]=ubah(j);
	for(j=0;j<=1000;j++)
	{
		for(k=0;k<=1000;k++)
			m[j][k]=-1;
	}
	cin>>n;
	for(i=0;i<n;i++)
	{
		jum=0;
		//printf("Case #%d: %d",i+1,jum);
		scanf("%d",&a);scanf("%d",&w);
		//for(j=10;j<1000;j++)
		//	d[j]=ubah(j);
		for(j=a;j<=w;j++)
		{
			for(k=j+1;k<=w;k++)
			{
				if(m[j][k]==-1)
					m[j][k]=cek(d[j],d[k]);
				jum=jum+m[j][k];
			}
		}
		printf("Case #%d: %d\n",i+1,jum);
	}
	return 0;
}
int cek(deque<int> d,deque<int> d2)
{
	//deque<int> d,d2;
	int i,j,l,c=0;
	/*while(a!=0)
	{
		i=a%10;
		//j=b%10;
		d.push_front(i);
		//d2.push_front(j);
		a=a/10;
		//b=b/10;
	}*/
	l=d.size();
	for(i=0;i<l-1;i++)
	{
		d2.push_back(d2[0]);
		d2.pop_front();
		for(j=0;j<l;j++)
		{
			if(d[j]!=d2[j])
				break;
		}
		if(j==l)
		{
			return 1;
			break;
		}
		
	}
	return 0;
}
deque<int> ubah(int a)
{
	deque<int> d;
	int i;
	while(a!=0)
	{
		i=a%10;
		d.push_front(i);
		a=a/10;
	}
	return d;
}
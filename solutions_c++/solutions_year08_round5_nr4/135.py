#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");

long long vals[15000];

void mkvals(void)
{
	int a = 1;
	int i,j,k;
	vals[0]=1;
	for(i=1; i<10007; i++)
	{
		vals[i]=(i*vals[i-1])%10007;
	}
	return;
}

pair<int,int> getfact(int x)
{
	
	pair<int,int> ans;
	ans.first=ans.second=0;
	ans.first=1;
	if(x==0)
	{
		return ans;
	}
	int i,j,k;
	i=x/10007;
	pair<int,int> partans;
	partans=getfact(i);
	ans.second+=i;
	ans.second+=partans.second;
	ans.first*=partans.first;
	ans.first%=10007;
	if(i%2==1)
	{
		ans.first=(10007-partans.first)%10007;
	}
	ans.first*=vals[x%10007];
	ans.first%=10007;
	return ans;
}

int getinv(int x)
{
	int curr=x%10007;
	int ans = 1;
	for(int i=0; i<20; i++)
	{
		if(((1<<i)&(10005))>0)
		{
			
			ans*=curr;
			ans%=10007;
			//cout << i << " " << ans << endl;
		}
		curr*=curr;
		curr%=10007;
	}
	return ans;
}

int getchoose(int x, int a)
{
	pair<int,int> num1;
	pair<int,int> denom1;
	pair<int,int> denom2;
	num1=getfact(x);
	//cout << x << " " << num1.first << " " << num1.second << endl;
	denom1=getfact(a);
	denom2=getfact(x-a);
	denom1.first=(denom1.first*denom2.first)%10007;
	denom1.second+=denom2.second;
	
	if(denom1.second<num1.second)
	{
		return 0;
	}
	else
	{
		return (num1.first*getinv(denom1.first))%10007;
	}
}

/*
int main(void)
{
	mkvals();
	int i,j,k;
	pair<int,int> x;
	cin >> i >> j;
	x=getfact(i);
	//cout << x.first << " " << x.s
	return 0;
}
*/

int numways(int x1, int x2, int y1, int y2)
{
	if(x1==x2 && y1==y2)
	{
		return 1;
	}
	if(x1>=x2 || y1>=y2)
	{
		return 0;
	}
	int i,j,k,l;
	int d1,d2;
	d1=x2-x1;
	d2=y2-y1;
	if(d1<d2)
	{
		k=d2;
		d2=d1;
		d1=k;
	}
	if(d1>2*d2)
	{
		return 0;
	}
	if((d1+d2)%3!=0)
	{
		return 0;
	}
	j=(d1+d2)/3;
	k=d2-j;
	//cout << x1 << " " << x2 << " " << y1 << " " << y2 << " " << j << " " << k << " " << getchoose(j,k) << endl;
	return getchoose(j,k);
}

int dists[12][12];
int px[12];
int py[12];
int sx[10];
int sy[10];

bool cmp(pair<int,int> a, pair<int,int> b)
{
	return (a.first<b.first);
}

int main(void)
{
	mkvals();
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k,l;
		int m,a,b,c;
		px[0]=py[0]=1;
		int r;
		int h,w;
		cin >> h >> w >> r;
		px[r+1]=h;
		py[r+1]=w;
		vector <pair<int,int> > rlis;
		pair<int,int> myrock;
		for(i=0; i<r; i++)
		{
			cin >> sx[i] >> sy[i];
			rlis.push_back(make_pair(sx[i],sy[i]));
		}
		sort(rlis.begin(),rlis.end(),cmp);
		for(i=0; i<r; i++)
		{
			px[i+1]=rlis[i].first;
			py[i+1]=rlis[i].second;
		}
		
		int ans = 0;
		int tot=0;
		int curr;
		for(j=0; j<(1<<r); j++)
		{
			curr=0;
			tot=0;
			k=1;
			for(i=0; i<r; i++)
			{
				if(j&(1<<i))
				{
					k*=numways(px[curr],px[i+1],py[curr],py[i+1]);
					k%=10007;
					//cout << i << " " << k << endl;
					curr=i+1;
					tot++;
				}
			}
			k*=numways(px[curr],px[r+1],py[curr],py[r+1]);
			k%=10007;
			//cout << j << " " << k << endl;
			if(tot%2==0)
			{
				ans+=k;
			}
			else
			{
				ans+=(10007-k);
			}
			ans%=10007;
		}
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
	}

	
	return 0;
}


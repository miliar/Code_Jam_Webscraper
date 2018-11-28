#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <iomanip>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <sstream>
#include <strstream>
#include <ctime>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

struct zibil
{
	int tiv;
	int num;
};

bool operator < (zibil a,zibil b)
{
	if (a.tiv < b.tiv || (a.tiv == b.tiv && a.num < b.num))
		return true;
	return false;
}

bool mej(long long c,long long a,long long b)
{
	if (c>=a && c<=b)
		return true;
	if (c>=b && c<=a)
		return true;
	return false;
}
int sgn(long long a)
{	
	if (a == 0)
		return 0;
	if (a<0)
		return -1;
	return 1;	
}
bool hatum(long long  x1,long long  y1,long long  x2,long long  y2,long long  xx1,long long yy1,long long xx2, long long yy2)
{
	long long  a1,b1,c1,a2,b2,c2;	
	a1=y1-y2;
	b1=x2-x1;
	c1=y2*x1-x2*y1;
	a2=yy1-yy2;
	b2=xx2-xx1;
	c2=yy2*xx1-xx2*yy1;
	if ((sgn(a1*xx1+b1*yy1+c1)==0 && sgn(a1*xx2+b1*yy2+c1)==0) ||
		(sgn(a2*x1+b2*y1+c2)==0  && sgn(a2*x2+b2*y2+c2)==0))
	{
		if ((mej(xx1,x1,x2) && mej(yy1,y1,y2)) ||			
			(mej(x1,xx1,xx2) && mej(y1,yy1,yy2)) ||			
			(mej(xx2,x1,x2) && mej(yy2,y1,y2)) ||			
			(mej(x2,xx1,xx2) && mej(y2,yy1,yy2)))			
			return true;
		else
			return false;
	}
		else
	{
		if ((sgn(a1*xx1+b1*yy1+c1)*sgn(a1*xx2+b1*yy2+c1)<=0) &&
			(sgn(a2*x1+b2*y1+c2)*sgn(a2*x2+b2*y2+c2)<=0))
			return true;
		else
			return false;
	}
}

int n,k;

int price[110][110];
int a[110][110];

zibil g[110];

vector <int> tik;

bool b[110];

bool good(int k)
{
	int i;
	for (i=0;i<tik.size();i++)
		if (a[g[tik[i]].num][g[k].num] == 1)
			return false;
	return true;
}

int guyn[110];

bool sork(int k)
{
	int i,j;
	for (i=0;i<n;i++)
		guyn[i] = rand()%k;

	int qanak = 0;
	bool f;
	while (qanak < 500000)
	{		
		f = false;
		for (i=0;i<n;i++)
			for (j=0;j<n;j++)
				if (i!=j)
					if (a[i][j] == 1 && guyn[i] == guyn[j])
					{
						qanak++;
						guyn[j] = rand()%k;
						f = true;
					}
		if (!f)
			return true;
	}
	return false;
}

int solve()
{
	int i;
	for (i=1;i<=n;i++)
		if (sork(i))
			return i;
	return n;
}

int main()
{

	srand(time(0));
	int i,j,test,t,r,w;

	in >> test;

	for (t=1;t<=test;t++)
	{
		in >> n >> k;

		for (i=0;i<n;i++)
			for (j=0;j<k;j++)
				in >> price[i][j];

		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
			{
				bool f = true;
				for (r=0;r<k-1 && f;r++)
				{
					w = r;
					if (hatum(r,price[i][r],r+1,price[i][r+1],w,price[j][w],w+1,price[j][w+1]))						
							f = false;						
					if (r>0)
					{
						w = r - 1;
						if (hatum(r,price[i][r],r+1,price[i][r+1],w,price[j][w],w+1,price[j][w+1]))						
							f = false;
					}
				}
				if (!f)
					a[i][j] = 1;
				else
					a[i][j] = 0;
			}
		}

		/*for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
				cout << a[i][j] << " ";
			cout << endl;
		}*/

		/*for (i=0;i<n;i++)
		{
			g[i].tiv = price[i][0];
			g[i].num =  i;
			b[i] = true;
		}

		sort(g,g+n);

		int answer = 0,ii;

		while (1)
		{
			tik.clear();
			for (i=0;i<n;i++)	
			{				
				if (b[i])
				{
					tik.push_back(i);
					break;
				}		
			}
			if (tik.empty())
				break;
			for (j=tik[tik.size()-1];j<n;j++)
				if (good(j))
					tik.push_back(j);
			for (i=0;i<tik.size();i++)
			{
				b[tik[i]] = false;
				//cout << g[tik[i]].num << " ";
			}
			//cout << endl;
			answer++;			
		}

		int ans1 = 0;
			for (i=0;i<n;i++)
			{
				k = 0;
				for (j=0;j<n;j++)
					if (i!=j)
						k+=a[i][j];
				if (k>ans1)
					ans1 = k;
			}*/

		int answer = solve();

		out << "Case #" << t << ": " << answer << endl;
	}

	return 0;
}

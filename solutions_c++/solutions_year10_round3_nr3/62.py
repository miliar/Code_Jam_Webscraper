#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

const int MAX= 512;
const int INF= MAX+1;

struct T 
{
	int i;
	int j;
	int s;
};

bool mat[MAX+1][MAX+1];
bool used[MAX+1][MAX+1];
int go[MAX+1][MAX+1];
int res[MAX+1];
int resc;


const int tohex(const char c)
{
	if (c>='0' && c<='9')
		return c-'0';
	else
		return 10+c-'A';
}

const bool cmp(const T &a, const T &b)
{
	return (a.s>b.s) ||
		(a.s==b.s && 
		(a.i<b.i || (a.i==b.i && a.j<b.j))); 
}

const bool space(const int i, const int j, const int s)
{
	int ii, jj;
	for(ii=i; ii<i+s; ++ii)
		for(jj=j; jj<j+s; ++jj)
			if (used[ii][jj])
				return false;
	return true;
}


void fill(const int i, const int j, const int s)
{
	int ii, jj;
	for(ii=i; ii<i+s; ++ii)
		for(jj=j; jj<j+s; ++jj)
			used[ii][jj]= true;
}


int main()
{
	int i, j, k, h, t, n, m, r, p, size, rsize;
	char c;
	vector<T> mas;
	T tmp;
 	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >>t;
	for(k=1; k<=t; ++k)
	{
		mas.resize(0);
		cin >>m >>n;
		for(i=1; i<=m; ++i)
			for(j=1; j<=n; j+=4)
			{
				cin >>c;
				r= tohex(c);
				mat[i][j+0]= r & 8;
				mat[i][j+1]= r & 4;
				mat[i][j+2]= r & 2;
				mat[i][j+3]= r & 1;
			}
		for(i=1; i<=m; ++i)
			for(j=1; j<=n; ++j)
				used[i][j]= false;
		for(i=1; i<=min(n, m); ++i)
			res[i]= 0;
		resc=0;
		for(i=1; i<=m; ++i)
		{
			p= n;
			go[i][n]= 1;
			for(j=n-1; j>=1; --j)
				if (mat[i][j]!=mat[i][j+1])
				{
					go[i][j]=p-j+1;
				}
				else 
				{
					go[i][j]= 1;
					p=j;
				}
		}
		/*
		
		for(i=1; i<=m; ++i)
		{
			cout << endl;
			for(j=1; j<=n; ++j)
				cout <<go[i][j] << ' ';
		}
*/

		for(i=1; i<=m; ++i)
			for(j=1; j<=n; ++j)
			{
				size= min(go[i][j], m-i+1);
				rsize= 1;
				for(h=i+1; h<=m; ++h)
				{
					if (size<(h-i+1))
						break;
					if (mat[h-1][j]==mat[h][j])
					{
						size= min(size, h-i);
						break;
					}
					size= min(size, go[h][j]);
					rsize= max(min(size, h-i+1), rsize);
				}
				tmp.i= i;
				tmp.j= j;
				for(h=1; h<=rsize; ++h)
				{
					tmp.s= h;
					mas.push_back(tmp);
				}
			}
		sort(mas.begin(), mas.end(), cmp);
		for(i=0; i<mas.size(); ++i)
			if (space(mas[i].i, mas[i].j, mas[i].s))
			{
				res[mas[i].s]++;
				if (res[mas[i].s]==1)
					resc++;
				fill(mas[i].i, mas[i].j, mas[i].s);
			}
		cout <<"Case #" <<k <<": " <<resc <<endl;
		for(i=min(n, m); i>=1; --i)
			if (res[i]!=0)
				cout <<i <<' ' <<res[i] << endl;
	}
	return 0;
}
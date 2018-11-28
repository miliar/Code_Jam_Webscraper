#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

typedef long long ll ;

struct T {
	ll cost;
	ll to;
};

void gen_link(const ll n,
			  const ll k,
			  const vector<ll> &mas,
			  vector<T> &link)
{
	int i, j; 

	ll sm(0);
	for(i=0; i<n; ++i)
		sm+= mas[i];
	
	if (k>=sm)
	{
		link.resize(n);
		for(i=0; i<n; ++i)
		{
			link[i].cost= sm;
			link[i].to= i;
		}
	}
	else
	{
		link.resize(n);
		for(i=0; i<n; ++i)
		{
			if (mas[i]>k)
			{
				link[i].cost= 0;
				link[i].to= i;
			}
			else
			{
				sm= mas[i];
				for(j=i+1; sm+mas[j%n]<=k; ++j)
					sm+= mas[j%n];
				link[i].cost= sm;
				link[i].to= j%n;
			}
		}
	}
}

const ll solve(const ll r,
			   const ll n,
			   const vector<T> &link)
{
	int i;
	ll res(0);
	int p=0;
	for(i=1; i<=r; ++i)
	{
		res+= link[p].cost;
		p= link[p].to;
	}
	return res;
}


int main()
{
	int i, j, t;
	ll r, n, k;
	vector<ll> mas;
	vector<T> link;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >>t;
	for(i=1; i<=t; ++i)
	{
		cin >>r >>k >>n;
		mas.resize(n);
		for(j=0; j<n; ++j)
			cin >>mas[j];
		gen_link(n, k, mas, link);
		cout <<"Case #" <<i <<": " <<solve(r, n, link) <<endl;
	}
	return 0;
}

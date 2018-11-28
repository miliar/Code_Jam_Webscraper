#include<iostream>
#include<set>
#include <vector>
#include<algorithm>
#include<cmath>
using namespace std;

const int maxn = 1050000;
int prime[100000] , hash[maxn]={0} , k;
void lineprime()//线性素数筛选
{
	int  i , j;
	k = 0;
	for (i = 2 ; i < maxn ; i++)
	{
		if (!hash[i])
			prime[k++] = i;
		for (j = 0 ; j < k && prime[j]*i < maxn  ; j++)
		{
			hash[i*prime[j]] = 1;
			if (0 == i % prime[j]) break;//精华
		}
	}
}
vector<int> st[1000050];
int mk[1000050];
int ok(int a , int b)
{
	int l = 0 , r = 0;
	while(l<st[a].size() && r < st[b].size())
	{
		if (st[a][l]==st[b][r]) return 1;
		if (st[a][l] < st[b][r] ) l++;
		else
			r++;
	}
	return 0;
}
void mmerge(int a, int b)
{
	vector<int> nw;
	int l = 0 , i,r = 0;
	st[a].push_back(10000);
	st[b].push_back(10000);
	for (i = 0 ; i < st[a].size() + st[b].size() - 2; i++)
	{
		if (st[a][l]<st[b][r])
		{
			nw.push_back(st[a][l]);
			l++;
		}
		else
		{
			nw.push_back(st[b][r]);
			r++;
		}
	}
	mk[b] = 1;
	st[a] = nw;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,a,b,p,l,r,ca,ans,i,j;
	lineprime();
	cin>>T;
	for (ca = 1 ; ca <= T ; ca++)
	{
		cin>>a>>b>>p;
		l = lower_bound(prime,prime+k,p)-prime;
		r = upper_bound(prime,prime+k,b)-prime;
		for (i = a ; i <= b ; i++)
		{
			st[i-a].clear();
			mk[i-a] = 0;
			for (j = l ; j < r ; j++)
			{
				if (i%prime[j]==0)
					st[i-a].push_back(j);
			}
		}
		while(1)
		{
			for (i = a ; i <= b ; i++)
			{
				if (mk[i-a]) continue;
				for (j = i+1 ; j <= b ;j++)
				{
					if (mk[j-a]) continue;
					if (ok(i-a,j-a))
					{
						mmerge(i-a,j-a);
						break;
					}
				}
				if (j <= b) break;
			}
			if (i > b ) break;
		}
		ans = 0;
		for (i = a ; i <= b ; i++)
		{
			if (mk[i-a]==0) ans++;
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1000

struct POINT
{
	int left;
	int right;
};

int n;
POINT ps[MAXN];

bool cmp(POINT p1, POINT p2)
{
	return p1.left < p2.left;
}


int solve()
{
	int i, j, res;
	sort(ps, ps+n, cmp);
	res = 0;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < i; j++)
		{
			if(ps[j].right > ps[i].right)
				res++;
		}
	}
	
	return res;
}

int main()
{
	int i, case_num, t;
	int a, b;
	cin>>t;
	for(case_num = 1; case_num <= t; case_num++)
	{
		cin>>n;
		for(i = 0; i < n; i++)
		{
			cin>>ps[i].left>>ps[i].right;
			ps[i].left -= 1;
			ps[i].right -= 1;
		}
		
		cout<<"Case #"<<case_num<<": "<<solve()<<endl;

	}
	return 0;
}
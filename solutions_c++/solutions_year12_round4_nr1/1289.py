#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<functional>
#include<queue>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;
typedef map<string,string>::iterator sm;
#define mp(a, b) make_pair(a, b)

struct dd
{
	int d, l;
};

int nowright;
int nowd;
int ww[10001];

struct ddd
{
	int pos, right;
};
queue <ddd> q;
int main()
{
	int t, c=1, n, m, target, i;
	cin >> t;
	while(t--)
	{
		vector <dd> x;
		cin >> n;
		for(i=0; i<n; i++)
		{
			dd q;
			scanf("%d%d", &q.d, &q.l);
			x.push_back(q);

			ww[i] = 0;
		}
		scanf("%d", &target);
		printf("Case #%d: ", c++);
		while(!q.empty())
			q.pop();
		ddd qq = {0, 2*x[0].d};
		q.push(qq);
		bool ck=0;
		while(!ck && !q.empty())
		{
			qq = q.front();
			q.pop();
			if(qq.right >= target)
				ck = 1;
			int d = x[qq.pos].d, right;
			for(int i=qq.pos+1; i<n && !ck; i++)
			{
				if(qq.right < x[i].d)
					break;
				ddd ins = {i, x[i].d+min(x[i].d-d, x[i].l)};
				if(ins.right >= target)
					ck = 1;
				if(ins.right <= ww[ins.pos])
					continue;
				ww[ins.pos] = ins.right;
				q.push(ins);
			}
		}
		if(ck)
			puts("YES");
		else
			puts("NO");
	}
}

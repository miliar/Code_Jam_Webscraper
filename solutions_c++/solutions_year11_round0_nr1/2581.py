#include <cstdio>
#include <vector>

using namespace std;

vector<pair<int,int> > ovec;
vector<pair<int,int> > bvec;
int res;

void Input()
{
	int n;
	scanf("%d", &n);
	ovec.clear();
	bvec.clear();
	for (int i=0; i<n; i++)
	{
		char c[20];
		int a;
		scanf("%s%d", &c, &a);
		if (c[0]=='B')
			bvec.push_back(make_pair(a,i));
		else
			ovec.push_back(make_pair(a,i));
	}
}

int moveBpos(int pos, int index)
{
	if (pos < bvec[index].first)
	{
		pos++;
		return pos;
	}
	if (pos > bvec[index].first)
	{
		pos--;
	}
	return pos;
}
int moveOpos(int pos, int index)
{
	if (pos < ovec[index].first)
	{
		pos++;
		return pos;
	}
	if (pos > ovec[index].first)
	{
		pos--;
	}
	return pos;
}

void Solve()
{
	int oindex = 0;
	int bindex = 0;
	int opos = 1;
	int bpos = 1;

	res = 0;
	while (oindex != ovec.size() || bindex != bvec.size())
	{
		res++;
		if (oindex == ovec.size())
		{
			if (bpos == bvec[bindex].first)
			{
				bindex++;
				continue;
			}
			bpos = moveBpos(bpos,bindex);
			continue;
		}
		if (bindex == bvec.size())
		{
			if (opos == ovec[oindex].first)
			{
				oindex++;
				continue;
			}
			opos = moveOpos(opos,oindex);
			continue;
		}
		if (bvec[bindex].second < ovec[oindex].second)
		{
			if (bpos == bvec[bindex].first)
			{
				bindex++;
			}
			else
			{
				bpos = moveBpos(bpos,bindex);
			}
			opos = moveOpos(opos,oindex);
		}
		else
		{
			if (opos == ovec[oindex].first)
			{
				oindex++;
			}
			else
			{
				opos = moveOpos(opos,oindex);
			}
			bpos = moveBpos(bpos,bindex);
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		Input();
		Solve();
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
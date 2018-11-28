#pragma warning(disable:4786)
#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<assert.h>
using namespace std;

const int MAX_N = 1005;


int R,K,N;
int g[MAX_N];
int gc[MAX_N];


struct Node
{	
	vector<int> v;
	int pos;
};

const int HS_N = 1777;
Node hs[HS_N];

int GetKey(const vector<int>& v)
{
	int key = 0;
	for(int i = 0; i < (int)v.size(); ++i)
	{
		key = (key + v[i]) % HS_N;
	}
	return key;
}

void Init(Node *hs, int n)
{
	for(int i = 0 ;i < n; ++i)
	{
		hs[i].pos = -1;
	}
}

bool Cmp(const vector<int> &a, const vector<int> &b)
{
	if(a.size() != b.size())
	{
		return false;
	}
	for(int i = 0 ; i < (int)a.size(); ++i)
	{
		if(a[i] != b[i])
		{
			return false;
		}
	}
	return true;
}

void Insert(vector<int>& v, int pos)
{
	int key = GetKey(v);
	while(hs[key].pos >= 0 && !Cmp(v, hs[key].v))
	{
		key = (key + 1 < HS_N ? key + 1: 0);
	}
	if(hs[key].pos < 0)
	{
		hs[key].pos = pos;
		hs[key].v = v;
	}
}

Node* Find(const vector<int> &v)
{
	int key = GetKey(v);
	while(hs[key].pos >= 0 && !Cmp(v, hs[key].v))
	{
		key = (key + 1 < HS_N ? key + 1: 0);
	}
	return (hs[key].pos < 0 ? NULL: &hs[key]);
}


void Input()
{
	scanf("%d%d%d",&R,&K,&N);
	for(int i = 0 ;i < N; ++i)
	{
		scanf("%d",&g[i]);
	}
	return;
}


void LShift(vector<int> &v, int n)
{
	reverse(v.begin(), v.begin() + n);
	reverse(v.begin() + n, v.end());
	reverse(v.begin(), v.end());
}


void Solve(int caseId)
{
	int i,j;

	Init(hs, HS_N);	

	vector<int> a(g, g + N);

	int pos = -1;
	int period = -1;
	for(i = 0; ; ++i)
	{
		Node* res = Find(a);
		if(!res)
		{
			Insert(a, i);
			int tot = 0;
			for(j = 0; j < N && tot + a[j] <= K; ++j)
			{
				tot += a[j];
			}
			gc[i] = tot;
			LShift(a, j);
		}
		else
		{
			pos = res->pos;
			period = i - pos;
			break;
		}
	}

	assert( pos >= 0 && period >= 1);

	__int64 res = 0;
	for(i = 0; i < pos; ++i)
	{
		res += gc[i];
	}
	R -= pos;

	__int64 t = 0;
	for(i = pos; i < pos + period; ++i)
	{
		t += gc[i];
	}
	res += R / period * t;

	R %= period;
	for(i = pos; i < pos + R; ++i)
	{		
		res += gc[i];
	}


	printf("Case #%d: %I64d\n", caseId, res);
	return;
}


int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tcNum;
	scanf("%d",&tcNum);
	int i;
	for(i = 1; i <= tcNum; ++i)
	{
		Input();
		Solve(i);
	}
	return 0;
}

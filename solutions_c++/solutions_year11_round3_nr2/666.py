#include<cstdio>
#include<vector>
#include<iostream>

using namespace std;

int CASOS, L, t, N, C, Dist[1001];

void leerEntrada()
{
	scanf("%d %d %d %d ", &L, &t, &N, &C);
	for (int x = 0; x < C; x++)
		scanf("%d", Dist+x);
	scanf("\n");
}

void dbg(vector<int> v)
{
	cout << "[";
	for (int x=0; x<v.size(); x++)
		cout << v[x] << " ";
	cout << "]" << endl;
	return;
}

int go()
{
	vector<int> v;
	for (int x = 0; x < N; x++)
		v.push_back(2 * Dist[x % C]);

	int rem = t;
	reverse(v.begin(), v.end());
	int tot =0;
	while (v.size() > 0 && rem > 0)
	{
		if (v.back() <= rem)
		{
			rem -= v.back();
			tot += v.back();
			v.pop_back();
		}
		else
		{
			int b = v.back();
			tot += rem;
			v.pop_back();
			v.push_back(b-rem);
			rem = 0;
		}
	}
	
	if (v.size() == 0)
		return tot;
	
	sort(v.begin(), v.end());
	while (v.size() > 0)
	{
		int b = v.back();
		if (L > 0)
			tot += b/2;
		else
			tot += b;
		L--;
		v.pop_back();
	}

	return tot;
	/*
	dbg(v);
	int z;
	z = v.back();
	cout << z << endl;
	v.pop_back();
	dbg(v);
	z = v.back();
	cout << z << endl;
	v.pop_back();
	dbg(v);
	reverse(v.begin(), v.end());
	dbg(v);
	sort(v.begin(), v.end());
	dbg(v);
	*/
}

int main(void)
{
	scanf("%d\n", &CASOS);
	for (int caso=1; caso<=CASOS; caso++)
	{
		leerEntrada();
		int ret = go();
		printf("Case #%d: %d\n", caso, ret);
	}	
}

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

struct Polygon
{
	int n;
	int pts[10];
};

int wall[10][2];
Polygon polyQue[1000];
Polygon polys[100];
int N, M;
int polysCt;

void swap(int &a, int &b)
{
	int t = a;
	a = b; b = t;
}

bool CutIt(Polygon &curP, int a, int b, Polygon &p1, Polygon &p2)
{
	if(a>b) swap(a, b);

	int i, j, k;
	for(i=1; i<=curP.n; i++) if(curP.pts[i]==a)
	{
		for(j=i+2; j<=curP.n; j++) if(curP.pts[j]==b && !(i==1 && j==curP.n))
		{
			int pos;

			pos = 1;
			//p1.n = j-i+1;
			for(k=i; k<=j; k++) p1.pts[pos++] = curP.pts[k];
			p1.n = pos-1;
			
			//p2.n = curP.n-j+2;
			pos = 1;
			for(k=1; k<=i; k++) p2.pts[pos++] = curP.pts[k];
			for(k=j; k<=curP.n; k++) p2.pts[pos++] = curP.pts[k];
			p2.n = pos - 1;

			return true;
		}
	}

	return false;
}

void CutPoly()
{
	int i;
	int f = 0, r = 1;
	polyQue[0].n = N;
	for(i=1; i<=N; i++) polyQue[0].pts[i] = i;

	while(f<r)
	{
		Polygon curP = polyQue[f++];
		Polygon p1, p2;
		for(i=0; i<M; i++) if(CutIt(curP, wall[i][0], wall[i][1], p1, p2))
		{
			polyQue[r++] = p1;
			polyQue[r++] = p2;
			break;
		}

		if(i>=M) polys[polysCt++] = curP;
	}
}

int colors[100];

bool Search(int curPos, int tot)
{
	if(curPos>N)
	{
		bool flag = true;
		for(int i=0; i<polysCt; i++)
		{
			int st = 0;
			int ct = 0;
			for(int j=1; j<=polys[i].n; j++)
			{
				int pt = polys[i].pts[j];
				if(st & (1<<colors[pt])) continue;
				ct++;
				st = (st | (1<<colors[pt]));
			}
			if(ct<tot)
			{
				flag = false;
				break;
			}
		}
		return flag;
	}
	for(int i=1; i<=tot; i++)
	{
		colors[curPos] = i;
		if(Search(curPos+1, tot)) return true;
	}
	return false;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		cin>>N>>M;
		
		int i;
		for(i=0; i<M; i++) cin>>wall[i][0];
		for(i=0; i<M; i++) cin>>wall[i][1];

		polysCt = 0;
		CutPoly();

		//for(i=0; i<polysCt; i++)
		//{
		//	cout << "polygon " << i+1 << ": ";
		//	for(int j=1; j<=polys[i].n; j++) cout << polys[i].pts[j] << " ";
		//	cout << endl;
		//}

		int maxN = N;
		for(i=0; i<polysCt; i++) if(polys[i].n < maxN)
			maxN = polys[i].n; 

		//cout <<"maxN= "<< maxN << endl;

		int ans = -1;
		for(i=maxN; i>=1; i--)
		{
			ans = i;
			bool flag = Search(1, ans);
			if(flag) break;
		}
		cout << "Case #" << cas++ << ": ";
		cout << ans << endl;
		for(i=1; i<N; i++) cout << colors[i] << " ";
		cout << colors[i] << endl;
	}
	return 0;
}
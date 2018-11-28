#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 103;
const int x0[] = {1,-1,1,-1,0,1,0,-1,0};
const int y0[] = {1,-1,-1,1,1,0,-1,0,0};

struct el{
	char name;
	int button;
};

struct qq{
	int i,j,k;
};

int m[nmax][nmax][nmax],d[nmax][nmax][nmax];
qq q[nmax * nmax * nmax],p[nmax][nmax][nmax];
el a[nmax];


bool belong(int i,int j)
{
	return (i >= 1 && j >= 1 && i <= 100 && j <= 100);
}

int path(int n)
{
	memset(m,0,sizeof(m));
	memset(d,0,sizeof(d));
	m[1][1][1] = 1;
	d[1][1][1] = 0;

	int top = 1;
	int tail = 1;

	q[1].i = q[1].j = q[1].k = 1;

	while (top <= tail)
	{
		qq cur = q[top];
		++top;

		if (cur.k > n)
		{
			/*while (!(cur.i == 1 && cur.j == 1 && cur.k == 1))
			{
				cout << cur.i << " " << cur.j << " " << cur.k << endl;
				cur = p[cur.i][cur.j][cur.k];
			}
			cout << endl;*/

			return d[cur.i][cur.j][cur.k];
		}

		
		for (int i = 0;i < 9; ++i)
		{
			qq next;
			next.i = cur.i + x0[i];
			next.j = cur.j + y0[i];
			next.k = cur.k;

			if (x0[i] == 0 && cur.i == a[cur.k].button && a[cur.k].name == 'O') next.k++;
			if (y0[i] == 0 && cur.j == a[cur.k].button && a[cur.k].name == 'B') next.k++;

			if (belong(next.i,next.j) && m[next.i][next.j][next.k] == 0)
			{
				m[next.i][next.j][next.k] = 1;
				d[next.i][next.j][next.k] = d[cur.i][cur.j][cur.k]+1;
				p[next.i][next.j][next.k] = cur;
				++tail;
				q[tail] = next;					
			}
		}
		
	}
	
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;

	for (int test = 1;test <= nn; ++test){
		int n;

		cin >> n;

		for (int i = 1;i <= n; ++i) cin >> a[i].name >> a[i].button;		
		
		printf("Case #%i: %i\n",test,path(n));		
	}
	
	return 0;
}
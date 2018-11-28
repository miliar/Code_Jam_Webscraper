#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

#define MAXN 10

int p[] = {0,1,2,3,4,5,6,7,8,9};
int T, N, W, L;
int r[MAXN];
int x[MAXN], y[MAXN];
bool solved;	
	
void place(int si, int sx, int sy)
{
	if (si==N)
	{
		solved = true;
		return;
	}
	
	if (sx+r[p[si]]<=W && sy+r[p[si]]<=L)
	{
		x[p[si]] = sx+r[p[si]];
		y[p[si]] = sy+r[p[si]];
	//	cout<<r[p[si]]<<" "<<x[p[si]]<<" "<<y[p[si]]<<endl;
		place( si+1, x[p[si]]+r[p[si]], max(sy,-r[p[si+1]]) );
		place( si+1, max(sx,-r[p[si+1]]) , y[p[si]]+r[p[si]] );
	}
}

int main()
{
	cin>>T;
	for (int t=1; t<=T; t++)
	{
		cin>>N>>W>>L;
		for (int i=0; i<N; i++)
			cin>>r[i];
		solved = false;
		sort (p,p+MAXN);

		do
		{
			place(0,-r[p[0]],-r[p[0]]);
			next_permutation(p,p+N);
			//break;
		} while (!solved);
		
		cout<<"Case #"<<t<<":";
		for (int i=0; i<N; i++)
			cout<<" "<<x[i]<<" "<<y[i];
		cout<<endl;
	}
	return 0;
}


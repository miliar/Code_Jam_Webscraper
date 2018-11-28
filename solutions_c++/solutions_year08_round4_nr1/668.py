#include <iostream>
#include <vector>

#define inf 10000000

using namespace std;

int M;
bool v;
vector <bool> lt;
vector <bool> cb;

int calc(int a)
{
	if (a>=(M/2))
	{
		if (lt[a]==v)
			return 0;
		return inf;
	}
	int hi=calc(a*2+1);
	int hd=calc(a*2+2);
	if (not cb[a])
	{
		if (lt[a]==v)
		{
			return min(hi,hd);
		}
		return hi+hd;
	}
	if (lt[a]==v)
	{
		return min(hi,hd);
	}
	return min(hi+1,min(hd+1,hi+hd));
}

int main()
{
	int N;
	cin >> N;
	for (int caso=1;caso<=N;caso++)
	{
		int V;
		cin >> M >> V;
		v=(V==1);
		lt=vector <bool>  (M);
		cb=vector <bool> (M,false);
		for (int i=0;i<M/2;i++)
		{
			int a,b;
			cin >> a >> b;
			lt[i]=(a==0);
			cb[i]=(b==1);
		}
		for (int i=M/2;i<M;i++)
		{
			int a;
			cin >> a;
			lt[i]=(a==1);
		}
		int tot=calc(0);
		cout << "Case #" << caso << ": ";
		if (tot>=inf)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << tot << endl;
	}
}

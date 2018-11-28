#include <iostream>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;
typedef long long LL;

#define NMAX 1011

int N, W, L,
	X[NMAX], Y[NMAX], R[NMAX];

inline bool between(int a, int x, int b)
{
	return (a<x && x<b) || (a>x && x>b);
}

inline long long sqr(long long l) { return l*l; }

// wepchnij ko³o #i tak, by lewa krawêdŸ otaczaj¹cego prostok¹ta zaczyna³a siê na pozycji x; zwraca prawa krawêdŸ
int Wedge(int i, int lx)
{
	int r = R[i], y = -r, rx = lx+r+r;
	for(int j=0; j<i;++j)
	{
		if(between(lx, X[j]-R[j], rx) || between(X[j]-R[j], lx, X[j]+R[j]))
		{
			y = max(y, Y[j]+R[j]);
		}
	}
	X[i] = lx+r;
	Y[i] = y+r;
	return rx;
}

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		cin>>N>>W>>L;
		for(int i=0; i<N; ++i)
		{
			cin>>R[i];
		}
		//sort(R, R+N, greater<int>());

		int x = -R[0];
		for(int i=0; i<N; ++i)
		{
			if(x+R[i]>W) 
				x = -R[i];
			x = Wedge(i, x);
		}

		cout<<"Case #"<<test<<":";
		for(int i=0; i<N; ++i)
		{
			cout<<" "<<X[i]<<" "<<Y[i];
			if(X[i]<0 || Y[i]<0 || X[i]>W || Y[i]>L) cerr << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
		}
		for(int i=0; i<N; ++i) for(int j=i+1; j<N; ++j)
		{
			if((sqr(X[i]-X[j])+sqr(Y[i]-Y[j]))<(sqr(R[i])+sqr(R[j])))
			{
				cerr<<" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ";
				cerr<<X[i]<<","<<Y[i]<<","<<R[i];
				cerr<<" <--> ";
				cerr<<X[j]<<","<<Y[j]<<","<<R[j];
				cerr<<" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ";
			}

		}


		cout<<endl;
	}
	
	return 0;
}

/**
22
2 6 6
1 1
3 320 2
4 3 2
3 2 320
4 3 2
*/
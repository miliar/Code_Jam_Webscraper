#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 1000100

struct SW
{
	int skad;
	int dokad;
	int speed;

	bool operator<(const SW& S)
	{
		return skad<S.skad;
	}
	SW() {}
	SW(int skad, int dokad, int speed) : skad(skad),dokad(dokad),speed(speed) {}
};

using namespace std;
typedef vector<SW> VP;
typedef long double LD;

bool cmp(const SW& a, const SW& b)
{
	if (a.speed!=b.speed) return a.speed<b.speed;
	return a.skad<b.skad;
}

bool pomin[MAX];

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int X,S,R,t,N;
		cin>>X>>S>>R>>t>>N;

		for (int i=0; i<=X; ++i) pomin[i]=false;

		VP V(N);
		for (int i=0; i<N; ++i) cin>>V[i].skad>>V[i].dokad>>V[i].speed;
		sort(V.begin(),V.end());

		if (V.front().skad>0) V.push_back(SW(0,V.front().skad,0));
		for (int i=1; i<N; ++i)
		{
			if (V[i].skad>V[i-1].dokad) V.push_back(SW(V[i-1].dokad,V[i].skad,0));
		}
		if (V[N-1].dokad<X) V.push_back(SW(V[N-1].dokad,X,0));
		sort(V.begin(),V.end());
		N=(int)V.size();

		VP W=V;
		sort(W.begin(),W.end(),cmp);
		LD time=0;
		for (int i=0; i<N; ++i)
		{
			LD dist=W[i].dokad-W[i].skad;
			LD speed=R+W[i].speed;
			if (time+dist/speed<=t) time+=dist/speed;
			else
			{
				LD czasSzybko=t-time;
				LD drogaSzybko=czasSzybko*speed;
				speed=S+W[i].speed;
				LD drogaReszta=dist-drogaSzybko;
				LD czasReszta=drogaReszta/speed;

				time=t+czasReszta;
			}
			pomin[W[i].skad]=true;
			if (time>=t) break;
		}

		for (int i=0; i<N; ++i)
		{
			if (pomin[V[i].skad]) continue;
			LD dist=V[i].dokad-V[i].skad;
			LD speed=S+V[i].speed;
			time+=dist/speed;
		}

		cout.precision(10);
		cout<<"Case #"<<test<<": "<<time<<endl;
	}

	return 0;
}

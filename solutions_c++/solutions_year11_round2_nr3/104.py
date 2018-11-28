#include <vector>
#include <iostream>

using namespace std;

template <class T>ostream &operator<<(ostream &o,const vector<T>&v)
{o<<"{";for(int i=0;i<(int)v.size();i++)o<<(i>0?", ":"")<<v[i];o<<"}";return o;}

int N,M;
vector<vector<bool> > R;

int ansc;
vector<int> ansv;
vector<int> V;

void BT(int p,int c)
{
	if ( p == N )
	{
		if ( c <= ansc )
			return;

		for ( int i=0; i<(int)R.size(); i++ )
		{
			vector<bool> f(c,false);

			for ( int j=0; j<N; j++ )
			if ( R[i][j] )
				f[V[j]] = true;

			for ( int i=0; i<c; i++ )
				if ( ! f[i] )
					return;
		}

		ansv = V;
		ansc = c;

		return;
	}

	for ( V[p]=0; V[p]<c; V[p]++ )
		BT(p+1,c);
	V[p] = c;
	BT(p+1,c+1);
}

int main()
{
	int T;
	cin >> T;

	for ( int t=1; t<=T; t++ )
	{
		cin>>N>>M;
		vector<int> U(M),V(M);
		for ( int i=0; i<M; i++ ) cin>>U[i];
		for ( int i=0; i<M; i++ ) cin>>V[i];

		vector<vector<bool> > R(1,vector<bool>(N,true));

		for ( int i=0; i<M; i++ )
		{
			int u = U[i]-1;
			int v = V[i]-1;
			if ( u>v) swap(u,v);

			for ( int j=0; j<(int)R.size(); j++ )
			if ( R[j][u] && R[j][v] )
			{
				vector<bool> t(N,false);
				for ( int k=u; k<=v; k++ )
					if (R[j][k])
						t[k] = true;
				R.push_back(t);
				for ( int k=u+1; k<=v-1; k++ )
					R[j][k] = false;
				break;
			}
		}

		::R = R;

		ansc = 0;
		::V = vector<int>(N);

		BT(0,0);


		cout << "Case #"<<t<<": "<<ansc<<endl;
		for ( int i=0; i<N; i++ )
			cout << (i>0?" ":"") << ansv[i]+1;
		cout << endl;

		//cout << R << endl;
	}
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <numeric>
#include <map>
#include <queue>
using namespace std;

//BEGIN_CODETEMPLATE
#define DISPV(v) { for(typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++) cout<<*it<<" "; cout<<endl; }
//END_CODETEMPLATE

bool isGood(vector<int> &V)
{
	for(int i=0 ; i<V.size() ; i++)
		if(V[i] > i)
			return false;
	return true;
}

int hash(vector<int> V)
{
	
}

int get(vector<int> V)
{
	queue< vector<int> > Q;
	queue<int> C;
	map< vector<int>, bool > cache;

	Q.push(V);
	C.push(0);

	cache[V] = true;

	int cnt;

	while(!Q.empty())
	{
		vector<int> P = Q.front();

		cnt = C.front();

		if(isGood(P))
			break;

		//DISPV(P);

		for(int i=0 ; i<P.size()-1 ; i++)
		{
			if(P[i]>P[i+1])
			{
				swap(P[i], P[i+1]);
				if(!cache.count(P))
				{
					Q.push(P);
					C.push(cnt+1);
					cache[P] = true;
				}
				swap(P[i], P[i+1]);
			}
		}

		Q.pop();
		C.pop();
	}

	return cnt;
}

int main()
{
	int T;
	cin >> T;

	for(int t=1 ; t<=T ; t++)
	{
		vector<int> V;

		int N;
		cin >> N;

		for(int i=0 ; i<N ; i++)
		{
			string s;
			cin >> s;

			int l;
			for(l=s.size()-1 ; l>=0 ; l--)
				if(s[l] == '1')
					break;

			l = max(l, 0);

			V.push_back(l);
		}

		int cnt = get(V);

		cout << "Case #" << t << ": " << cnt << endl;
	}

	return 0;
}

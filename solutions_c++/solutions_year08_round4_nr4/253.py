#include <iostream>
#include <vector>
#include <string>

using namespace std;
#define pb push_back
#define LL long long

int main()
{
	int T;
	scanf("%d",&T);
	int c=0;
	while(T--)
	{
		int K;
		scanf("%d", &K);
		string S;
		cin>>S;
		vector<int> v(K);
		for(int i=0;i<K;i++) v[i] = i;
		int ret = S.length();
		do
		{
			string S1;
			S1 = S;
			for(int i=0;i<S.length();i++)
				S1[i] = S[K*(i/K) + v[i%K] ];
			S1.erase( unique(S1.begin(),S1.end()), S1.end());
			ret <?= S1.length();

		}
		while( next_permutation( v.begin(), v.end() ));
		cout<<"Case #"<<++c<<": "<<ret<<"\n";
	}
	return 0;
}

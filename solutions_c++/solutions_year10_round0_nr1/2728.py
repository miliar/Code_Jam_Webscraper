#include <vector>
#include <bitset>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define vecStack(TO,FROM) TO.assign( FROM.begin() , FROM.end() )
#define vecSubst(TO,FROM) TO.clear(); TO.assign( FROM.begin() , FROM.end() )
#define vecAll(V) V.begin() , V.end()
#define vecForEach(V,I) for(int I=0; I<V.size() ; I++ )
#define vecFor(V,I,P) for(int I=0; I<V.size() ; I+=P )
#define vecFind(V,N) (find(V.begin(),V.end(),N)!=V.end())
#define vecPrint(V,I) for(int I=0 ; I<V.size() ; I++ )cout<<V[I];cout<<endl

#define long long int llint

int
main()
{
	int testcase;
	cin >> testcase;

	for( int cases=1 ; cases<=testcase ; cases++ )
	{
		int N , K;
		cin >> N >> K;
		bitset<100> bits(K);

		string result = "ON";
		for( int i=0 ; i<N ; i++ )
		{
			if( bits.at(i) == false ){
				result = "OFF";
			}
		}

		cout << "Case \#" << cases << ": " << result << endl;
	}

	return 0;
}
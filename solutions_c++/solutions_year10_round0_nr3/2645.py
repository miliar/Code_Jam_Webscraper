#include <vector>
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


int solverFunc( int time , int rideMax , int group , vector<int> gset )
{
	int euro=0;

	for( int i=0 ; i<time ; i++ )
	{
		int roop=rideMax;
		int g = group;

		while( roop-gset.front() >=0 && g-->0 ){
			euro += gset.front();
			roop -= gset.front();

			rotate( gset.begin() , gset.begin()+1 , gset.end() );
		}
	}
	return euro;
}
int
main()
{
	int testcase;
	cin >> testcase;

	int cases=1;
	while( cases <= testcase )
	{
		int ridetime , maximamRide , group;

		cin >> ridetime >> maximamRide >> group;
		
		vector<int> groupSet(group);
		for( int i=0 ; i<group ; i++ )
		{
			cin >> groupSet[i];
		}

		int result = solverFunc( ridetime , maximamRide , group , groupSet );
		
		cout << "Case \#" << cases << ": " << result << endl;
		cases++;
	}

	return 0;
}
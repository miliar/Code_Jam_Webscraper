#include <stdio.h>
#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
int main(int argc, char *argv[])
{
	printf("Hello, world\n");
	ifstream input;
	input.open( "C-small-attempt2.in" );
	ofstream output;
	output.open( "C-small2.out" );

	long long R,k,N;
	long long g[1000];
	long long euro = 0,currentLoad =0, maxLoad=0;
	int cur=0;
	int T = 0;
	input>>T;
	for( int i=1; i<=T; i++ )
	{
		input>>R>>k>>N;
		maxLoad = 0;
		for( int j=0; j<N;j++ )
		{
			input>>g[j];
			maxLoad += g[j];
		}
		if( maxLoad <= k )
		{
			output<<"Case #"<<i<<": "<<maxLoad*R<<"\n";
			continue;
		}

		cur = 0;
		euro = 0;
		for( long long m=1; m<=R; m++ )
		{
			currentLoad = 0;
			while( currentLoad + g[cur]<= k )
			{
				currentLoad += g[cur];
				cur++;
				if( cur == N )
					cur=0;
			}
			euro += currentLoad;
			//cout<<euro<<","<<currentLoad<<"\n";

			if( cur ==0 )  //as good as start
			{	
				long long quickM,quickEuro; 
				quickM = m;
				quickEuro = euro;
				while( quickM+m < R )
				{
					quickM += m;
					quickEuro +=euro;
				}
				m = quickM;
				euro = quickEuro;
			}
		}
		output<<"Case #"<<i<<": "<<euro<<"\n";
		//cout  <<"Case #"<<i<<": "<<euro<<"\n";
	}
	input.close();
	output.close();
	return 0;
}

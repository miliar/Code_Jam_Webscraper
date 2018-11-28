#include<iostream>
#include<string>

using namespace std;

typedef unsigned long long int uint;

char combinations[256][256];
uint counts[256];
bool oppositions[256][256];

void clear()
{
	for( int i = 0 ; i < 256 ; i++ )
	{
		counts[i] = 0;
		for( int j = 0 ; j < 256 ; j++ )
			combinations[i][j] = oppositions[i][j] = 0;
	}
}

string magicka( char* seq, uint length )
{
	char q[length+1];
	int j = 0;

	for( uint i = 0 ; i <= length ; i++ ) q[i] = '\0';

	if( length > 0 ) 
		q[0] = seq[0];

	for( uint i = 1 ; i < length ; i++ )
	{
		char combination = combinations[q[j]][seq[i]];
		if( combination )
			q[j] = combination;
		else
		{
			bool opposition = false;
			for( uint k = 0 ; k <= j; k++ )
				if( oppositions[q[k]][seq[i]] )
				{
					i++;
					j=0;
					q[j] = seq[i];
					opposition = true;
				}
			if( !opposition )
			{
				j++;
				q[j] = seq[i];
				counts[q[j]]++;
			}
		}
	}
	
	string output = "[";

	uint i=0;
	while( i < j )
	{
		output += q[i];
		output += ", ";
		i++;
	}
	if( q[i] != 0 ) output += q[i];
	output += ']';

	return output;
}

int main()
{
	uint T;
	cin >> T;

	for( int c = 0 ; c < T ; c++ )
	{
		int C,D,N;

		clear();

		cin >> C;
		for( int i = 0 ; i < C ; i++ )
		{
			char comb[3];
			cin >> comb;
			combinations[comb[0]][comb[1]]=comb[2];
			combinations[comb[1]][comb[0]]=comb[2];
		}

		cin >> D;
		for( int i = 0 ; i < D ; i++ )
		{
			char opp[2];
			cin >> opp;
			oppositions[opp[0]][opp[1]]=true;
			oppositions[opp[1]][opp[0]]=true;
		}

		cin >> N;

		char seq[N];
		cin >> seq;

		cout << "Case #" << c+1 << ": " << magicka( seq, N ) << endl;
	}

	return 0;
}


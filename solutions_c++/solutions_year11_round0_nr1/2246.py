#include<iostream>

using namespace std;

typedef unsigned long long int uint;

struct Position
{
	char bot;
	uint button;
};

uint botTrust( Position* seq, uint length )
{
	uint orange=1, blue=1;
	uint orange_i = 0, blue_i = 0;
	uint time = 0;

	while( orange_i < length || blue_i < length )
	{
		
		// busco la próxima instrucción para el orange
		while( seq[orange_i].bot != 'O' && orange_i < length ) orange_i++;

		// busco la próxima instrucción para el blue
		while( seq[blue_i].bot != 'B' && blue_i < length ) blue_i++;
		
		// si no llegó a destino orange, se mueve 
		if( orange != seq[orange_i].button )
			orange += (orange < seq[orange_i].button?1:-1);
		else if( orange_i < blue_i )
			orange_i++;

		// si no llegó a destino blue, se mueve 
		if( blue != seq[blue_i].button )
			blue += (blue < seq[blue_i].button?1:-1);
		else if( blue_i < orange_i )
			blue_i++;

		time++;

	}

	return time;

}

int main()
{
	int T;
	Position* seq = NULL;

	cin >> T;

	for( int c = 0 ; c < T ; c++ )
	{
		int N;
		cin >> N;
		seq = new Position[N];

		for( int i = 0 ; i < N ; i++ )
			cin >> seq[i].bot >> seq[i].button;

		cout << "Case #" << c+1 << ": " << botTrust( seq, N ) << endl;

		delete[] seq;
	}

	return 0;
}


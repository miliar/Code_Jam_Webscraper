#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
using namespace std;

int main(int _argc, char* _argv)
{
	ifstream infile;
	ofstream outfile;
	string line;

	infile.open("A.in");
	outfile.open("A.out");

	int cases = 0;
	infile >> cases;

	for( int i = 1; i <= cases; i++ ){
		int N;
		infile >> N;
		int sol = 0;
		int O=1, B=1;
		queue<int> routeO, routeB;
		queue<char> orders;

		for( int j = 0; j < N; j++ ){
			char player;
			int stepto;

			infile >> player >> stepto;

			if( player == 'O') routeO.push(stepto);
			else routeB.push(stepto);

			orders.push(player);
		}

		for( sol = 0; !orders.empty(); sol++ ){
			char order = orders.front();

			// move 
			if( !routeO.empty() && O != routeO.front() )
			{
				O += (routeO.front()-O)/abs(routeO.front()-O);
				//cout << "Move to Button " << O;
			}
			else
			{
				if ( order == 'O' ) 
				{
					//cout << "Push Button " << O;

					routeO.pop();
					orders.pop();
				}
					//cout << "Stay at Button " << O;
			}

			//cout << "  |  ";

			if( !routeB.empty() && B != routeB.front() )
			{
				B += (routeB.front()-B)/abs(routeB.front()-B);
				//cout << "Move to Button " << B;
			}
			else
			{
				if( order == 'B' && B == routeB.front() ){
					//cout << "Push Button " << B;

					routeB.pop();
					orders.pop();
				}
					//cout << "Stay at Button " << B;
			}

			//cout << endl;
		}
		outfile << "Case #" << i << ": " << sol << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}
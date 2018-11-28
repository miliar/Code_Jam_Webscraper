#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	for ( int i = 1 ; i <= n ; i++ ) {
		int moves;
		cin >> moves;
		
		char c;
		int button;
		
		int time = 0;
		int timeA = 0;
		int timeB = 0;
		int butA = 1;
		int butB = 1;
		
		for ( int k = 1 ; k <= moves ; k++ ) {
			cin >> c;
			cin >> button;
			if ( c == 'O' ) {
				if (( abs(button - butA) ) > ( time - timeA ) ) {
					time += (abs(button - butA) + 1) - ( time -timeA );
				} else {
					time += 1;
				}
				
				timeA = time;
				butA = button;
			} else {
				if (( abs(button - butB) ) > ( time - timeB ) ) {
					time += (abs(button - butB) + 1) - ( time -timeB );
				} else {
					time += 1;
				}
				timeB = time;
				butB = button;
			}
		}
		cout << "Case #"<<i<<": "<< time << endl;
	}
	return 0;
}

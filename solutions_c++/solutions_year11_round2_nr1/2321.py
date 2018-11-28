#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{

	int T; cin >> T;
	for( int t = 0 ; t < T ; t++ ) {
		vector<string> V; V.clear();
		int N; cin >> N;
		double *WP = new double[N];
		int *played = new int[N];
		for( char c = cin.get() ; c != '\n' ; c = cin.get() );
		for( int i = 0 ; i < N ; i++ ) {
			string str = "";
			getline(cin,str);
			V.push_back(str);
			int won = 0; 
			played[i] = 0;
			for( int j = 0 ; j < N ; j++ ) {
				if( V[i][j] != '.' ) played[i]++;
				if( (i != j) && (V[i][j] == '1') ) won++;
			}

			if( played[i] > 0 )
				WP[i] = double(won) / double(played[i]);
			else WP[i] = 0;

			// cout <<"WP[" << i << "] " << WP[i] << endl;
		}
		
		double *OWP = new double[N];

		for( int i = 0 ; i <  N ; i++ ) {
			double sum = 0.0;
			for( int j = 0 ; j < N ; j++ ) {
				if ( j != i ) {
				if( V[j][i] == '1' ) {
					if( (played[j] - 1) > 0 )
						sum += ((WP[j]*played[j] - 1) / double(played[j]-1));
					else
						sum += 0.0;
				} else if ( V[j][i] == '0' ) {
					sum += ( (WP[j]*played[j]) / double(played[j]-1) )  ;
				} else {
					sum += 0.0;
				}
				}
			}
			
			if( (played[i]) > 0 ) 
				OWP[i] = sum / double(played[i]);
			else
				OWP[i] = 0.0;
	

			// cout << "OWP[" << i << "] " << OWP[i] << endl;
	
		}


		double *OOWP = new double[N];

		for( int i = 0 ; i < N ; i++ ) {
			double sum = 0.0;
			for( int j = 0 ; j <  N ; j++ ) {
				if( (j != i) && (V[i][j] != '.') ) {
					sum += OWP[j];
				}
			}

			if( played[i] > 0 ) 
				OOWP[i] = sum / double(played[i]);
			else
				OOWP[i] =0.0; 


			// cout << "OOWP[" << i << "] " << OOWP[i] << endl;

		}


		cout << "Case #" << (t+1) << ":" << endl;
		for( int i = 0 ; i < N ; i++ ) {
			cout << ( 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] ) << endl;
		}

	}


	return 0;
}




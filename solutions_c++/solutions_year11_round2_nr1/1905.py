
#include <iostream>
#include <vector>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;

double calculateOWP( vector<char> &games, vector<double> &OWP, int excluded){
	double total = 0;
	int n = 0;
	for ( int i=0; i<games.size(); i++){
		if ( i!= excluded && games[i]!='.'){
			n++;
			if ( games[i] == '1') total ++;
		}
	}

	total = total/n;
	return total;
}

double mod( double a){
	return (a >= 0 ) ? a:-a;
}

int main(){

	int T;
	cin>>T;

	for ( int t=0; t<T; t++){
		int Teams;
		cin>>Teams;

		vector<vector<char> > scores( Teams, vector<char> ( Teams, ' '));
		for ( int i=0; i<Teams; i++){
			for ( int j=0; j<Teams; j++){
				char tmp;
				cin>>tmp;
				scores[i][j] = tmp;
			}
		}

		vector<vector<double> > OOWP( Teams, vector<double> ( Teams, 0));


		for ( int i=0; i<Teams; i++){
			for ( int j=0; j<Teams; j++){
				OOWP[i][j] =  calculateOWP(scores[i], OOWP[i], j);
			}
		}

		/*for ( int i=0; i<Teams; i++){
			for ( int j=0; j<Teams; j++){
				cout<<OOWP[i][j]<<" ";
			}
			cout<<endl;
		}*/

		cout<<"Case #"<<t+1<<":"<<endl;

		cout.precision(12);
		//cout.setf(std::ios::fixed,std::ios::floatfield);

		for ( int i=0; i<Teams; i++){
			double averageWP = 0;
			double averageOWP = 0;
			int n=0;
			for ( int j=0; j<Teams; j++){
				if ( scores[i][j]!='.'){
					n++;
					averageWP += OOWP[j][i];

					int np=0;
					double av= 0;
					for ( int k=0; k<Teams; k++){
						if ( scores[j][k]!='.'){
							np++;
							av += OOWP[k][j];
						}
					}
					averageOWP +=av/np;

				}
			}

			cout<<(n*OOWP[i][i]/4+averageWP/2+averageOWP/4)/n<<endl;

		}




	}


	return 0;
}


#include <iostream>
#include <vector>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;


int main(){

	int N;
	cin>>N;

	int nElements = 'Z'-'A'+ 1;

	for ( int n=1; n<=N; n++){
		vector<vector<char> > mixer ( nElements, vector<char>( nElements, 'A'-1) );
		vector<vector<bool> > opposite ( nElements, vector<bool>( nElements, false) );

		int C; //combinaciones
		cin>>C;
		for ( int c=0; c<C; c++) {
			string comb;
			cin>>comb;
			mixer[comb[0]-'A'][comb[1]-'A'] = comb[2];
			mixer[comb[1]-'A'][comb[0]-'A'] = comb[2];
		}

		int D; //opuestos
		cin>>D;
		for ( int d=0; d<D; d++){
			string dest;
			cin>>dest;
			opposite[dest[0]-'A'][dest[1]-'A'] = true;
			opposite[dest[1]-'A'][dest[0]-'A'] = true;
		}

		string elementList;
		vector<int>  elementNumber( nElements, 0);

		string sequence;
		int length ;
		cin>>length;
		cin>>sequence;

		for ( int i=0; i<sequence.size(); i++){
			int candidate = sequence[i]-'A';
			//destroys?
			bool destroys = false;

			int currentLast = elementList[elementList.size()-1]-'A';
			if ( mixer[candidate][currentLast] == 'A'-1 ){
				for ( int j=0; j<nElements; j++){
					if ( opposite[candidate][j] && elementNumber[j]>0){
						destroys = true;
						break;
					}
				}
			}
			if ( destroys ){
				elementList.clear();
				elementNumber = vector<int>( nElements, 0);
			} else {
				elementList.push_back( sequence[i] );
				elementNumber[candidate]++;

				if ( elementList.size() >= 2){
					int beforeLast = elementList[elementList.size()-2]-'A';
					if ( mixer[candidate][beforeLast] != 'A'-1 ) {
						elementList.resize( elementList.size() - 2 );
						elementList.push_back( mixer[candidate][beforeLast] );

						elementNumber[candidate]--;
						elementNumber[beforeLast]--;
						elementNumber[mixer[candidate][beforeLast]-'A']++;
					}
				}


			}
		}
		cout<<"Case #"<<n<<": [";
		for ( int i=0; i<elementList.size(); i++){
			cout<<elementList[i];
			if ( i != elementList.size()-1)
				cout<<", ";
		}
		cout<<"]"<<endl;
	}



	return 0;
}

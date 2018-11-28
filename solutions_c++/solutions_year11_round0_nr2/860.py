#include <iostream>
#include <vector>
#include <cstring>

using namespace std ;

vector <char> element_list ;
char comb[128][128], oppo[128][128] ;

int main(void){

	int T ;
	cin >> T ;
	
	for( int i_case=1 ; i_case <= T ; i_case++ ){
		memset( comb, 0, sizeof(comb) ) ;
		memset( oppo, 0, sizeof(oppo) ) ;
		
		int C, D, N ;
		string buffer ;
		
		cin >> C ;
		while( C-- ){
			cin >> buffer ;
			comb[buffer[0]][buffer[1]] = buffer[2] ;
			comb[buffer[1]][buffer[0]] = buffer[2] ;
		}
		
		cin >> D ;
		while( D-- ){
			cin >> buffer ;
			oppo[buffer[0]][buffer[1]] = 1 ;
			oppo[buffer[1]][buffer[0]] = 1 ;
		}
		
		cin >> N ;
		cin >> buffer ;
		element_list.clear() ;
		for( int i=0 ; i<N ; i++ ){
			element_list.push_back( buffer[i] ) ;
			
			while( element_list.size() >= 2 ){
				char p = element_list[element_list.size()-1] ;
				char q = element_list[element_list.size()-2] ;
				
				if( comb[p][q] ){
					element_list.resize( element_list.size()-2 ) ;
					element_list.push_back( comb[p][q] ) ;
					continue ;
				}
				
				for( int j=0 ; j < element_list.size() ; j++ ){
					if( oppo[p][element_list[j]] )
						element_list.clear() ;
				}
				
				break ;
			}
		}
		
		cout << "Case #" << i_case << ": [" ;
		if( element_list.size() ){
			cout << element_list[0] ;
			for( int i=1 ; i<element_list.size() ; i++ )
				cout << ", " << element_list[i] ;
		}
		cout << "]" << endl ;
	}

	return 0 ;
}

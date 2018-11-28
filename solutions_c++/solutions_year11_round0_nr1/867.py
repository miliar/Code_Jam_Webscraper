#include <iostream>

using namespace std ;

struct robot{
	int loc ;
	int time ;
	
	robot(){
		loc = 1 ;
		time = 0 ;
	}
	
	int update(int pending, int button){
		int move = button - loc ;
		if( move < 0 )
			move = -move ;
			
		if( move <= pending - time )
			time = pending + 1 ;
		else
			time += move + 1 ;
		
		loc = button ;
		return time ;
	}
} ;

int main(void){
	int T, N ;
	
	cin >> T ;
	for( int i_case=1 ; i_case <= T ; i_case++ ){
		int ans = 0 ;
		robot last_O, last_B ;
	
		string R ;
		int loc ;
		cin >> N ;
		while( N-- ){
			cin >> R ;
			cin >> loc ;
			
			if( R[0] == 'O' )
				ans = last_O.update( last_B.time, loc ) ;
			else
				ans = last_B.update( last_O.time, loc ) ;
		}
		
		cout << "Case #" << i_case << ": " << ans << endl ;
	}

	return 0 ;
}

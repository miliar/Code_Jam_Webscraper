#include<iostream>
using namespace std;


int main () {
  int tt_c;
  cin >> tt_c;

  int i = 0;
  for( ; i < tt_c; i++) {
    int tt_snp = 0;
    int tt_t = 0;
    cin >> tt_snp >> tt_t ;
    
    bool status = false;
   
    int dived = tt_t ;
    int j = 0;
    for( ; j < tt_snp; j++) {
      if( (dived % 2) == 1 ) {
	dived = ( dived / 2 );
      } else
	break ;
    }
    
    if ( j == tt_snp )
      status = true;

    if( status == false )
      cout << "Case #" << i+1 << ": " << "OFF" << endl;
    else
      cout << "Case #" << i+1 << ": " << "ON" << endl;
  }
  
  return 0;
}

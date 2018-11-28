#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int cases, i;
	int a, b, c;
	int cont = 0;
	int googlers, surprising, min;
	int sorpresas = 0;
	int result = 0;
	int scores[100];
	cin >> cases;
	while ( cont < cases ){
		result = 0;
		cin >> googlers;
		cin >> surprising;
		cin >> min;
		for( i=0; i<googlers; i++ ){
			cin >> scores[i];
			switch( scores[i] % 3 ){
				case 0:
					if ( scores[i] / 3 >= min ){
						result++;
					}else{
						if( surprising > 0 && scores[i] / 3 > 0 && (scores[i] / 3) + 1 >= min ){            
							result++;
							surprising--;
						}            
					}         
				break;
				case 1:
					if ( scores[i] / 3 >= min || (scores[i] / 3) + 1 >= min ){
						result++;
					}else{
						if( surprising > 0 && (scores[i] / 3) + 1 >= min ){            
							result++;
							surprising--;
						}            
					}     
				break;
				case 2:
					if ( scores[i] / 3 >= min || (scores[i] / 3) + 1 >= min ){
						result++;
					}else{
						if( surprising > 0 && (scores[i] / 3) + 2 >= min ){            
							result++;
							surprising--;
						}            
					}    
				break;
			}
		}
		cout << "Case #" << cont+1 << ": "<< result << endl;
		cont++;	
	}	
	return 0;
}

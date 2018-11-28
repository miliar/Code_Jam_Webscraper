#include<iostream>
using namespace std;

int main()
{
	unsigned int tests;
	short int googlers, surprising, best;
	short int total[100];
	short int score[3];
	
	cin >> tests;
	
		for(int i = 1; i <= tests; i++)
		{
			
			cin >> googlers >> surprising >> best;
			
			for(int a=0; a < googlers; a++)
				cin >> total[a];
				
			int number = 0;	
			
			for(int a=0; a < googlers; a++)
			{
				//googler a
				//surprising left
				bool found = false;
				bool possible = false;
				
				for(int first = best; first <= total[a] && !found; first++){
				for(int second=best-1; second <= first && !found; second++){
				for(int third=best-1; third <= first && !found; third++){
				
					if(first + second + third == total[a]){
						possible = true;
						found = true;				
					}
				}				
				}
				}
					
				if((!found) && (surprising != 0))
				{
					for(int first = best; first <= total[a]; first++){
					for(int second=best-2; second <= first; second++){
					for(int third=best-2; third <= first; third++){
					
						if(first + second + third == total[a]){
							surprising--;
							possible = true;
							
						}
					
					}
					}
					}
					
				}
				
				if(possible)
						number++;		
			}	
			
	
			
			cout << "Case #" << i << ": ";
			cout << number;
			
				if(i < tests)
					cout << endl;
		}
	
	return 0;	
}

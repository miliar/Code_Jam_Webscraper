#include <iostream>
#include <fstream>

using namespace std;

int main(){

	ifstream fcin("a.in");
	ofstream fcout("a.txt");
	
	int cases;
	fcin >> cases;
	
	for(int i=1 ; i<= cases ; i++)
	{

		int googlers, surprises, p, cont=0;
		fcin >> googlers >> surprises >> p;
		int vec[googlers];
				
		while(googlers--)
		{
			int num;
			fcin >> num;
	
			if(num/3 >= p-2)
			{			
				if(num <= 1 && p >= 1){
					continue;
				}

		
				if(num/3 >= p-1){
					
					if(num%3 > 0 || num/3 >= p){
						cont++;
						continue;
					} else if(surprises > 0){
						cont++;
						surprises--;
					}
				}

				
				if(num%3 <= 1 ){
					continue;
				} else if(surprises > 0){
					cont++;
					surprises--;
					
				}
			
			}
		}
		
		fcout << "Case #" << i << ": " << cont << endl;
		cout << cont << endl;
	}
}


#include <iostream>
#include <math.h>
#include <set>

using namespace std;


int main()
{
	int T;
	int i;
	
	cin >> T;
	
	for( i = 1; i<=T; i++)
	{
		unsigned int A,B,C, tot = 0, digits = 0;
		
		cin >> A >> B;
		
		C = A;
		
		while(C != 0 )
		{
			C /= 10;
			digits++;
		}
		
		for(C = A; C < B; C++)
		{
			unsigned int currentNum;
			unsigned int lastDigit; 			
			int j;
			set<unsigned int> found;

			 
			currentNum = C;
			
			for(j=0; j < digits; j++)
			{
				lastDigit = currentNum % 10;
				
				currentNum = (pow(10, digits - 1) * lastDigit) + (currentNum /10);
				
				if((currentNum > C) and (currentNum <= B))
				{					
					if(found.find(currentNum) == found.end())
					{
						found.insert(currentNum);
						tot++;
// 						cout << "pair " << tot << ": (" << C << ", " << currentNum << ")" << endl;
					}
				}
			}
			
			
		}
		
		cout << "Case #" << i << ": " << tot << endl;
	}
	
}


/*Best result p or more:

If unsurprising, lowest possible score = 3p - 2
                 maximum possible score = 30

Best result p or more:

If surprising, maximum possible score = 28
               minimum possible score = 3p - 4


S = 2
p = 8

22-30 U        19-30 U
20-28 S        17-28 S

20, 8, 18, 18, 21


Are 3p-3, 3p-4 actual scores? 
If so, is S positive? 

Everything more than 3p - 2 is admissible
3p - 3 and 3p - 4, as many as possible are admissible. 
*/

#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;

int main(){
	int T;
	cin >> T;

	for(int i=0; i<T; i++){
		int N;
		cin >> N;

		int S;
		cin >> S;
		
		int p;
		cin >> p;

		int sur_count = 0;
		int reg_count = 0;
		for(int j=0; j<N; j++){
			int t;
			cin >> t;

			if (t >= 3*p - 2) reg_count++;
			else if(p==1) ; //do nothing because t = 0
			else if((t==3*p-3)||(t==3*p-4)) sur_count++;			
		}
		
		int solution = reg_count + ((sur_count > S)?S:sur_count);
		cout << "Case #" << i+1 <<": " << solution << endl;				
	}	
}


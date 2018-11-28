#include <iostream>
#include   <iomanip> 
#include <fstream>

using namespace std;





struct Pos{
	char col;
	int button;
};

int calculate(Pos *, int);

int main(){

	ifstream input("G:\\interview\\A-large.in");
	ofstream output("G:\\interview\\output.txt");
	int test_num;
	input>>test_num;

	if(test_num < 1 || test_num  >100)
		return 1;

	Pos *arry;
	for(int index = 0; index < test_num; index ++){
		
		int n;
		input>>n;
		if(n < 1 || n  > 100)
			return 1;
		arry = new Pos[n];
		for(int i = 0; i< n; i++){
			input>>arry[i].col;
			if('O' != arry[i].col && 'B' != arry[i].col )
				return 1;
			input>>arry[i].button;
			if(arry[i].button < 1 || arry[i].button > 100)
				return 1;
		}
		cout<<"Case #"<<(index + 1)<<": "<<calculate(arry, n)<<endl;
		output<<"Case #"<<(index + 1)<<": "<<calculate(arry, n)<<endl;
		delete[]arry;
	}
	input.close();
	output.close();
	return 0;
}

int calculate(Pos *arry, int n){

	int b_pos = 1, o_pos = 1;
	int minval = 0;
	int cur = 0, last_inc = 0, inc;
	int btoal = 0, otoal = 0;

	bool bcol = false;
	while(cur < n){
		if('O' == arry[cur].col){				
			inc = abs(arry[cur].button - o_pos) + 1; 
			o_pos = arry[cur].button;	
			
			if(bcol){
				if(inc <= btoal){	
					last_inc = 1;
				}else{
					last_inc = inc - btoal ;
				}
				otoal = last_inc;
			}else{					
				last_inc = inc;
				otoal += inc;
			}
			bcol = false;
		}else{	
			inc = abs(arry[cur].button - b_pos) + 1;

			b_pos = arry[cur].button;
			
			if(!bcol){				
				if(inc <= otoal){	
					last_inc = 1;
				}else{
					last_inc = inc - otoal ;
				}
				btoal = last_inc;
			}else{
				last_inc = inc;
				btoal += inc;
			}
			bcol = true;
		}
		minval += last_inc;
		cur ++;
	}
	return minval;
}


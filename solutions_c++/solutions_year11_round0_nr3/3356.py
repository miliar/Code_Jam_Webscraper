#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

template <typename T> T Max(T a,T b){
	if(a>b)return a;
	return b;
}

int power(int base,int exponent){
	if(exponent==0)return 1;
	return base*power(base,exponent-1);
}

void next_state(int* combination,int N){
	int carry = 0;
	int next_carry = 0;
	int add = 1;
	for(int i=0;i<N;i++){
		if(combination[i]+carry+add>1)next_carry=1;
		else next_carry = 0;
		combination[i] = (combination[i]+add+carry)%2;
		carry = next_carry;
		add = 0;
	}
}

void solve(int case_number,ofstream* output,int* candy,int N)
{
	int max = 0;
	int test = 0;
	int pile1;
	int pile2;
	int pile1_value;
	int pile2_value;
	int combination[N];
	
	for(int i=0;i<N;i++){
		test = (test^candy[i]);
	}
	
	if(test){
		*output << "Case #" << case_number <<": " << "NO" << endl;
		return;
	}else{
		
		for(int i=0;i<N;i++){
			combination[i] = 0;
		}

		for(int i=0;i<power(2,N);i++){	
	
			pile1 = 0;
			pile2 = 0;
			pile1_value = 0;
			pile2_value = 0;
			test = 0;
			
			next_state(&combination[0],N);
			for(int i=0;i<N;i++){
				test += combination[i];
			}
			
			if(test==0 || test==N)continue;
			
			for(int j=0;j<N;j++){
				if(combination[j]){
					pile1 = (pile1^candy[j]);
					pile1_value += candy[j];
				}else{
					pile2 = (pile2^candy[j]);
					pile2_value += candy[j];
				}
			}
		
			if ( (pile1==pile2) && (Max(pile1_value,pile2_value)>max)){
				max = (Max(pile1_value,pile2_value));
			}
		}
		*output << "Case #" << case_number <<": " << max << endl;
	}
}

int main()
{

	int T;
	int N;
	ifstream input("C-small-attempt1.IN");
	ofstream output("output.txt");
	
	input >> T;

	for(int i=0;i<T;i++)
	{
		input >> N;
		int candy[N];
		
		for(int j=0;j<N;j++){ input >> candy[j];}
		solve(i+1,&output,&candy[0],N);
	}
	
	return 0;
}

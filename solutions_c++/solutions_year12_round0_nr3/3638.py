#include<iostream.h>
#include<fstream>
#include<math.h>
#include<map>
using namespace std;


int numCycle(int n, int B ,map<int,int> cyclepair){
	int cur;
	int bit = log10(n);
	//cout<<n<<" "<<bit<<endl;
	int tmp;
	int count  =0;
	//map<int,int> cyclepair;	
	for ( int i = 1; i<= bit; i++){
		tmp = n/pow(10,i);
		cur = (n-tmp * pow(10,i) )*pow(10,(bit-i+1)) + tmp;
		//cout<<i<<" "<<cur<<"*"<<endl;
		if(cur > n && cur <= B){
			if(cyclepair[n] == cur)
				continue;
			//cout<<n<<" "<<cur<<endl;
			count ++;
			cyclepair[n] = cur;
		}
	}
	return count;
}
					
int main(){
	int T;
	int n, m;
	int A,B;
	bool tag;
	ifstream in("C-small-attempt1.in");
	ofstream out("output3.txt");
	in>> T;
	int count ;
	for( int i = 1; i<= T; i++){
		map<int,int> cyclepair;
		count = 0;
		in>> A>>B;
		if( B - A < 9){
			out<<"Case #"<<i<<":  0"<<endl;
			continue;
		}
	
		for( int j = A; j<=B; j++){
			count += numCycle(j,B,cyclepair);
		}
		out<<"Case #"<<i<<":  "<<count<<endl;
	}
}
		
			

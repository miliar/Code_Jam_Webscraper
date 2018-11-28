#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;

#define N 10

vector<unsigned long> factorial(N+1);
vector<unsigned long> subFactorial(N+1);
vector<vector<float> > derangementsP(N+1, vector<float> (N+1, 0));
vector<float> expectation(N+1, 0);

void populateFactorial(){
	factorial[0] = 1;
	factorial[1] = 1;
	for ( int i = 2; i<=N; i++){
		factorial[i] = factorial[i-1]*i;
	}
}

void populateSubFactorial(){
	subFactorial[0] = 1;
	for ( int i = 1; i<=N; i++){
		subFactorial[i] = i*subFactorial[i-1] + ( (i%2)? -1:1);
	}

}

void popualteDearangementsP(){
	for ( int i=0; i<=N; i++){
		derangementsP[i][0] = 1/float(factorial[i]);
	}

	for ( int i=2; i<=N; i++){
		for ( int j=2; j<=i; j++){
			derangementsP[i][j] = subFactorial[j]/float(factorial[j]*factorial[i-j]);
		}
	}
}

float mod( float a){
	return (a >= 0 ) ? a:-a;
}

void populateExpectation(){

	float delta = 1;
	int it = 0;
	while( delta > 1e-12 ){
		delta = 0;

		for ( int i = 1; i<=N; i++){
			float oldExp = expectation[i];

			float newExp = 0;
			for ( int j=0; j<=N; j++){
				newExp += (expectation[j]+1)*derangementsP[i][j];
			}

			delta = std::max( delta, mod( oldExp-newExp) );
			expectation[i] = newExp;
		}

		//cout<<it++<<endl;
	}

}

int nDerangements( const vector<int> & data){
	int derr = 0;
	for ( int i=0; i<data.size(); i++){
		if ( data[i] != i+1)
			derr++;
	}
	return derr;
}


int main(){

	populateFactorial();
	populateSubFactorial();
	popualteDearangementsP();
	populateExpectation();

	int T; //testcase
	cin>>T;

	for ( int t=1; t<= T; t++){
		int D;
		cin>>D;

		vector<int> data;
		for ( int n=0; n<D; n++){
			int tmp;
			cin>>tmp;
			data.push_back( tmp );
		}

		int der = nDerangements( data );

		float Exp = expectation[der];

		cout<<"Case #"<<t<<": "<<Exp<<endl;

	}


	return 0;
}

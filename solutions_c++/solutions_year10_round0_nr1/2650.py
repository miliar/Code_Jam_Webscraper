
#include <iostream>
#include<fstream>
using namespace std;

//#define  MYDEBUG

static int* results = NULL;
static unsigned long T = 0;


inline
void output(){
	///output
	ofstream f1("e:\\A-large.out");
	if( !f1 ) return;
	
	for (int i = 0; i != T; i++)
	{
		if ( results[i] == 0 )
			f1 << "Case #" << i+1 << ": OFF" << endl;
		else
			f1 << "Case #" << i+1 << ": ON" << endl;
		
	}

}

inline
void pushRet(int i, unsigned long n){
	if ( results != NULL ){
		results[n] = i;
	}
}

int main(){
	///get input T
	ifstream fin("e:\\A-large.in");
	fin >> T;

	/// malloc out result
	if ( T >= 0 ){
		results = (int *)malloc(T * sizeof(int));
	}


	unsigned long counter = T;
	unsigned long outCount = 0;
	///
	while( counter != 0){
		unsigned long N = 0;
		unsigned long K = 0;
		
		///get input

#ifdef MYDEBUG
		N = 4;
		K = 47;
#else
		fin >> N;
		fin >> K;
#endif
		unsigned long picker = 1;
		for (unsigned long i = 0; i != N ; i++){
			picker *= 2;
		}
		picker -= 1;

		K = K - picker;
		if ( K < 0 ){
			pushRet(0, outCount);
		}
		else{
			if( K%(picker+1) == 0 ){
				pushRet(1,outCount);
			}
			else{
				pushRet(0,outCount);
			}
		}

		counter--;
		outCount++;
	}
	output();

	///free results
	if(results != NULL )
		free(results);

	return 0;

}
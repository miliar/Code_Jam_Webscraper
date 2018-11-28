#include <iostream>

using namespace std;

const int maxN = 100;
const int maxL = 1000;

struct Letter{
	int code,freq;
};

int compare( const void *arg1, const void *arg2 );

int main()
{
	int N,P,K,L;
	Letter C[maxL];
	long long res;

	cin >> N;
	for(int i=1; i<=N; i++){
		/************************************
			Input Data
		*************************************/
		cin >> P >> K >> L;
		for(int j=0; j<L; j++){
			cin >> C[j].freq ;
			C[j].code =j;
		}
		/************************************
			Solve the Problem
		*************************************/
		qsort(C, L, sizeof(Letter), compare);
		res=0;
		for(int j=0;j<L;j++){
			res+=C[j].freq * (j/K+1);
		}
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}

int compare( const void *arg1, const void *arg2 )
{
	int r = - (*(Letter*) arg1).freq + (*(Letter*) arg2).freq;
   return r;
}

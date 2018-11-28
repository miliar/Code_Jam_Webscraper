#include <iostream>
#include <istream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <map>

#define min(a, b) (((a) < (b)) ? (a) : (b))

using namespace std;


int solver(int N, int S, int P, int scores[]){
	
	int higher = 0;
	int possible = 0;
	
	
	for(int i=0; i< N; i++){
		double avg = double(scores[i])/3;
		int intpart = (int)avg;
		double decpart = avg - intpart;
		
		if(decpart == 0){
			if(intpart >= P) higher++;
			if(intpart == P-1 && intpart > 0 && intpart < 10) possible++;
		}else if (decpart < 0.5){ //decpart = 0.3333
			if(intpart >= P-1)higher++;
		}else{ //decpart = 0.6666
			if(intpart >= P-1)higher++;
			if(intpart == P-2 && intpart < 9)possible++;
		}
	}
	
	return higher + min(S,possible);
}


int main(void){
	
	int n_cases;
	int N, S, P;
	scanf("%d",&n_cases);

	for (int testCase = 1; testCase <= n_cases; testCase++) {
		printf("Case #%d: ",testCase);
		scanf("%d",&N);
		scanf("%d",&S);
		scanf("%d",&P);
		int scores[N];
		for(int i=0;i<N;i++){
			scanf("%d",&scores[i]);
		}
		
		cout << solver(N,S,P,scores) << endl;

	}
	return 0;
}



#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int getAbove(int  scores[100], int n, int s, int p){
	int res = 0;
	for ( int i = 0 ; i < n ; i++ ){
		int score = scores[i];
		switch (score % 3) {
			case 0:
				if ( score / 3 >= p) 
					res++;
					else if ( (score /3 +1 >= p) && (s > 0) && (score/3-1 >=0)){
						res++;
						s--;
					}
				break;
			case 1:
				if ( score /3 + 1 >= p)
					res ++ ;
				break;
			case 2:
				if ( score /3 + 1 >= p )
					res ++;
				else if (( score /3 + 2 >=p ) && (s >0)){
					res++;
					s--;
				}
				break;
			default:
				break;
		}
	}
	return res;
}

int main(int argv, char** args){
	ifstream in;
	in.open("large.in");
	ofstream out;
	out.open("large.out");
	int T,S,N,p;
	in >> T;
	int score[100] = {};
	
	for ( int i = 0; i < T ; i++){
		
		in >> N >> S >> p;
		for ( int j = 0; j <  N; j++){
			in>> score[j];
		//	out << score[j] << " " ;
		}
		//out << endl;
		int res = getAbove(score, N,S,p);
		out << "Case #" << i +1 << ": "<< res << endl;
	}
}
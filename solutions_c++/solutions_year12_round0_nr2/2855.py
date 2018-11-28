#include<iostream>
#include<string>
#include<fstream>

using namespace std;

char answer(char a){
	
	
}

int main(){

	ifstream in_str("1.txt");
	ofstream out_str("2.txt");
	
	int numOfCases = 0;
	in_str >> numOfCases;
	for(int i = 0; i < numOfCases; i++){
		int numOfGoogle,sRemaining,limit;
		in_str >> numOfGoogle >> sRemaining >> limit;
		int score = 0;
		int result = 0;
		for(int j = 0; j < numOfGoogle; j++){
			in_str >> score;
			if(limit > 1){
				if(score >= (limit*3-2)){
					result++;
				}
				else if (score >= (limit*3-4) && (sRemaining > 0)){
					result++;
					sRemaining--;
				}
			}
			else{
				if(score >= limit){
					result++;
				}
			}
		}
		out_str << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}
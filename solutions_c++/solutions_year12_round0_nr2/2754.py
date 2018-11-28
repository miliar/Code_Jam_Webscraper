#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main(){
	string temp;
	int numCases=0, N=0, S=0, p=0, num=0;
	int t[3];
	int triplet[3];
	int answers[3];
	bool bad = true;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
	outFile.open("output.out");
	if(!inFile){
                cerr << "Unable to open file Dictionary";
	}
	inFile >> numCases;
	cout << numCases << "\n";
	for(int i=0; i<numCases; i++){
		answers[0] = 0;
		answers[1] = 0;
		answers[2] = 0;
		bad = true;
		inFile >> N;
		cout << N << " ";
		inFile >> S;
		cout << S << " ";
		inFile >> p;
		cout << p << " ";
		for(int j=0; j<N; j++){
			inFile >> t[j];
			cout << t[j] << " ";
		}
		cout << "\n";
		for(int k=0; k<N; k++){
			triplet[0] = (t[k]/3);
			triplet[1] = (t[k]/3);
			triplet[2] = (t[k]/3);
			if(t[k]%3 == 1){
				triplet[0]++;
			}
			else if(t[k]%3 == 2){
				triplet[0]++;
				triplet[1]++;
			}
			cout << "Triplet: " << k << " is " << triplet[0] << " " << triplet[1] << " " << triplet[2] << "\n";

			// Check without suprising results
			if(triplet[0] >= p){
				answers[k] = 2;
				cout << "answers[k] is 2\n";
			}

			if(triplet[1] == triplet[2] && !(triplet[0]>triplet[1]) && triplet[2]!=0){
				triplet[2]--;
				triplet[0]++;
				bad = false;
			}
			else if(triplet[0] == triplet[1] && triplet[2]!=0){
				triplet[1]--;
				triplet[0]++;
				bad = false;
			}
			cout << "Triplet after adjustment is: " << k << " is " << triplet[0] << " " << triplet[1] << " " << triplet[2] << "\n";
			if(triplet[0] >= p && answers[k]!=2 && !bad){
				answers[k] = 1;
				cout << "answers[k] is 1\n";
			}
			else if(answers[k]!=2){
				answers[k] = 0;
				cout << "answers[k] is 0\n";
			}
		}

		//Calculate num
		num=0;
		for(int q=0; q<3; q++){
        	        if(answers[q] == 2){
				num++;
				cout << "adding 1 for answers 2\n";
			}
			else if(answers[q] == 1 && S>0){
				num++;
				S--;
				cout << "adding 1 for suprising result\n";
			}
        	}
        		cout << "Case #" << (i+1) << ": " << num << "\n";
			outFile << "Case #" << (i+1) << ": " << num << "\n";
	}
	return 1;
}

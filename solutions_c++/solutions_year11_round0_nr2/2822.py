#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solveEachCase();

void main(){
	int caseNum;
	cin >> caseNum;
	for (int i = 0; i < caseNum; i++){
		string caseResult = solveEachCase();
		cout << "Case #" << i+1<<": " <<caseResult;
		if(i < caseNum - 1)
			cout <<endl;
	}

}

string solveEachCase(){
	int c, d, n;
	
	cin >> c;
	char* comb1 = (char*) malloc(c*sizeof(char));
	char* comb2 = (char*) malloc(c*sizeof(char));
	char* comb3 = (char*) malloc(c*sizeof(char));

	for(int i=0; i<c;i++){
		string temp;
		cin >> temp;
		const char* temp2 = temp.c_str();
		comb1[i] = temp2[0];
		comb2[i] = temp2[1];
		comb3[i] = temp2[2];
	}

	cin >> d;
	char* oppose1 = (char*) malloc(c*sizeof(char));
	char* oppose2 = (char*) malloc(c*sizeof(char));

	for(int i = 0; i< d;i++){
		string temp;
		cin >> temp;
		const char* temp2 = temp.c_str();
		oppose1[i] = temp2[0];
		oppose2[i] = temp2[1];
	}

	cin >> n;
	string input;
	cin >> input;
	const char* charList = input.c_str();
	if(n != input.length()){
		cout << "inconsistant input" <<endl;
		exit(1);
	}

	vector<char> output;
	for(int i = 0; i < n; i++){
		char freshChar = charList[i];
		if(output.size()==0){
			output.push_back(freshChar);
			continue;
		}
		char lastChar = output.back();
		//try to match combine
		bool matched = false;
		for(int j = 0; j < c;j++){

			if(freshChar==comb1[j]&&lastChar==comb2[j]){
				output.pop_back();
				output.push_back(comb3[j]);
				matched = true;
				break;
			}
			if(freshChar==comb2[j]&&lastChar==comb1[j]){
				output.pop_back();
				output.push_back(comb3[j]);
				matched = true;
			}

		}
		if(matched == true)
			continue;

		//try to match opposition
		matched = false;
		for(int j=0; j<d;j++){
			if(oppose1[j] == freshChar){
				for(int k = output.size()-1;k>=0;k--){
					if(output[k]==oppose2[j]){
						matched = true;
						break;
					}
				}
				if(matched){
					output.clear();
					break;
				}
			}

			if(oppose2[j] == freshChar){
				for(int k=output.size()-1;k>=0;k--){
					if(output[k]==oppose1[j]){
						matched=true;
						break;
					}
				}
				if(matched){
					output.clear();
					break;
				}
			}
		}

		if(matched==true)
			continue;
		output.push_back(freshChar);
	}
	
	string resultList = "[";
	for(int i = 0; i< output.size();i++){
		resultList.push_back(output[i]);
		if( i <output.size()-1)
			resultList.append(", ");
	}
	resultList.append("]");

	return resultList;
}
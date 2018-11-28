#include <iostream>
#include <vector>
#include <string>


using namespace std;
vector<string> combineList, opposedList;

int isInCombineList(char result_last, char word_first){
	if(!combineList.empty()){
		for(int k=0; k<combineList.size(); k++){
			if( (result_last == combineList[k][0] && word_first == combineList[k][1]) || 
				(word_first == combineList[k][0] && result_last == combineList[k][1])){
					return k;
			}
		}
	}
	return -1;
};

int isInOpposedList(string result, char word_first){
	if(!opposedList.empty()){
		for(int k=0; k<opposedList.size(); k++){
			for(int l=0;l<result.length();l++){
				if( (result[l] == opposedList[k][0] && word_first == opposedList[k][1]) || 
					(result[l] == opposedList[k][1] && word_first == opposedList[k][0])){
						return k;
				}
			}
		}
	} 
	return -1;
};

int main(){
	int cases;
	cin >> cases;
	for(int i=0;i<cases;i++){
		int C, D, N;
		string word;
		string result;
		combineList.clear();
		opposedList.clear();
		
		cin >> C;
		for(int j=0;j<C; j++){
			string combine;
			cin >> combine;
			combineList.push_back(combine);
		}
		
		cin >> D;
		for(int j=0;j<D; j++){
			string opposed;
			cin >> opposed;
			opposedList.push_back(opposed);
		}
		
		cin >> N;
		cin >> word;
		result="";
		
		while(word.length()>0){
			if(result.length()==0) {
				result.push_back(word[0]);
				word.erase(0,1);
			}else{
				int index;
				if((index=isInCombineList(result[result.length()-1], word[0])) >= 0){
					result[result.length()-1] = combineList[index][2];
					word.erase(0,1);
				}
				else if(isInOpposedList(result, word[0]) >= 0){
					result.clear();
					word.erase(0,1);
				}
				else{
					result.append(1,word[0]);
					word.erase(0,1);
				}
			}
		}
		
		cout << "Case #" << i+1 << ": [";
		for(int j=0; j<result.length();j++){
			cout <<	result[j];
			if(j< result.length()-1) cout<<", ";
		}
		cout << "]" << endl;
	}
	
	
	
	return 0;
}

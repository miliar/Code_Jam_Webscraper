#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

vector<string> getPatternAsVector(string pattern){
	vector<string> ans;
	int pos = 0;
//	printf("Converting #%s#\n",(char*)pattern.c_str());	

	while(pos<pattern.size()){
		if(pattern[pos]=='('){
			string token = "";
			pos++;
			while(pattern[pos]!=')'){
				token += pattern[pos];
				pos++;
			}			
			ans.push_back(token);
//			printf("Tok %s\n",(char*)token.c_str());
		}
		else{
			string prox = "";
			prox+= pattern[pos];
			ans.push_back(prox);
//			printf("Tokc %s\n",(char*)prox.c_str());
		}
		pos++;
	}
//	printf("Vector\n");
/*	for(int i=0;i<ans.size();i++){
		printf("%s\n",(char*)ans[i].c_str());
	}*/
	return ans;
}

bool compare(string word,vector<string> patternAsVec){
	bool ans = true;
//	printf("comparing %s\n",(char*) word.c_str());
	int correctNumber = 0;
	for(int i=0;i<word.size();i++){
		for(int j=0;j<patternAsVec[i].size();j++){
//			printf("Comparing letters %c %c\n",patternAsVec[i][j],word[i]);
			if(patternAsVec[i][j]==word[i]){
//				printf("Correct %c %c\n",patternAsVec[i][j],word[i]);
				correctNumber++;
				break;
			}
		}
	}
	return correctNumber==word.size();
}

int main(){
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	vector<string> dictionary;
	for(int i=0;i<D;i++){
		char temp[2000];
		scanf("%s\n",temp);
		dictionary.push_back(string(temp));		
	}

	for(int i=0;i<N;i++){
		char pattern[2000];
		scanf("%s\n",pattern);//fgets(pattern,1900,stdin);//
//		printf("Read pattern %s\n",pattern);
		int count = 0;
		vector<string> patternAsVec =	getPatternAsVector(string(pattern));
		for(int j=0;j<D;j++){
			if( compare(dictionary[j], patternAsVec ))
				count++;
		}
		printf("Case #%d: %d\n",i+1,count);
		
	}
	
}

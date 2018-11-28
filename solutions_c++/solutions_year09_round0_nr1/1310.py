//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream cin("A-large.in");
ofstream cout("A-Large.out");


bool matches (string &dictword, int pos[20][26]){
	bool retval = true;
	for(int i=0;i<dictword.size();i++)
		if(pos[i][dictword[i]-'a']==0) retval = false;
	return retval;
}
void fillarray(string &word, int pos[20][26]){
	for(int i=0;i<20;i++)
		for(int j=0;j<26;j++)
			pos[i][j]=0;
	
	char curmd = 'a';
	int j=-1;
	for(int i=0;i<word.size();i++){
		if(word[i]=='('){
			curmd = 'b';
			j=j+1;			
		}
		else if (word[i]==')'){
			curmd = 'a';			
		}
		else if (curmd == 'a'){
			j=j+1;
			pos[j][word[i]-'a'] = 1;
		}
		else if (curmd == 'b'){
			pos[j][word[i]-'a'] = 1;
		}
	}
}


int getCount(vector <string> &dict, string &word){
	int pos[20][26];
	fillarray(word,pos);
	int retval=0;
	for(int i=0;i<dict.size();i++)
		if(matches(dict[i],pos)) retval++;
	return retval;	
}

int main(){
	int L,D,N;
	cin >> L >> D >> N;
	vector <string> dict;
	vector <string> words;
	for(int i=0;i<D;i++){
		string s;
		cin >> s;
		dict.push_back(s);
	}
	for(int j=0;j<N;j++){
		string s;
		cin >> s;
		words.push_back(s);
	}
	for(int i=0;i<words.size();i++){
		int n = getCount(dict,words[i]);
		cout << "Case #" << i + 1 << ": " << n << endl; 
	}
	return 0;
}
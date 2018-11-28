#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

int main(){

	ifstream ifs;
	ifs.open("A-small-attempt0.in");

	ofstream ofs;
	ofs.open("A-small-attempt0.out");

	int wordLength,NofWord,tc;
	vector<string> known;
	vector<string> words;
	set<char> ch;
	ifs>>wordLength>>NofWord>>tc;
	
	string getStr;
	for(int i = 0 ; i < NofWord ; i++){
		ifs>>getStr;	
		known.push_back(getStr);
	}

	for(int caseCnt = 1 ; caseCnt <= tc ; caseCnt++){
		words.clear();
		words = known;
		ifs>>getStr;
		int i = 0;
		int lenCnt = 0;
		while(i<(int)getStr.size()){
			ch.clear();
			if(getStr.at(i) == '('){
				while(getStr.at(i) != ')'){
					ch.insert(getStr.at(i));
					i++;
				}
			}
			else ch.insert(getStr.at(i));

			int j = 0;
			while(j < (int)words.size()){
				if(ch.find(words[j].at(lenCnt)) == ch.end()) words.erase(words.begin()+j);
				else j++;
			}
			lenCnt++;
			i++;
		}
		cout<<"Case #"<<caseCnt<<": "<<(int)words.size()<<endl;
		ofs<<"Case #"<<caseCnt<<": "<<(int)words.size()<<endl;
	}
	ifs.close();
	ofs.close();
	return 0;
}
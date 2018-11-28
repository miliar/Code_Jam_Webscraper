#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main(){

	int L,D,N;
	cin>>L>>D>>N;

	string buf;

	vector<string> dictionary;
	for(int i=0;i<D;i++){
		cin>>buf;
		dictionary.push_back(buf);
	}

	string word;
	vector<string> letters;
	string::size_type index;
	int ans=0;

	ofstream cou("gjamA.txt");

	for(int i=1;i<=N;i++){
		cin>>word;
		for(int c=0;c<L;c++){
			index = word.find("(");
			if(index == string::npos){
				for(int size=0;size<word.size();size++){
					letters.push_back(word.substr(size,1));
				}
				break;
			}
			else{
				if(index>0){
					letters.push_back(word.substr(0,1));
					word = word.substr(1);
					continue;
				}
				index = word.find(")");
				letters.push_back(word.substr(1,index-1));
				word = word.substr(index+1);
			}
		}

		/*for(int j=0;j<letters.size();j++){
			cou<<letters[j]<<" ";
		}
		cou<<"\n";*/

		for(int d=0;d<D;d++){
			for(int c=0;c<L;c++){
				if(letters[c].find(dictionary[d][c]) != string::npos){
					if(c==L-1) ans+=1;
					else continue;
				}
				else break;
			}
		}

		cou<<"Case #"<<i<<": "<<ans<<"\n";
		ans=0;
		letters.clear();
	}

	return 0;
}
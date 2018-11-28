#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin ("alien.in");
ofstream fout ("alien.out");

int main(){
	int L, D, N;
	fin >> L >> D >> N;
	vector<string> words;
	for (int i=0; i<D; i++){
		string w;
		fin >> w;
		words.push_back(w);
	}
	for (int i=0; i<N; i++){
		string pattern;
		fin >> pattern;
		vector<string> poss;
		vector<string> matches;
		string word="";
		for (int j=0; j<L; j++)
			word+=' ';
		int k=0;
		for (int j=0; j<pattern.size(); j++){
			if (pattern[j]=='('){
				string str="";
				j++;
				while (pattern[j]!=')'){
					str+=pattern[j];
					j++;
				}
				poss.push_back(str);
			}
			else
				word[k]=pattern[j];
			k++;
		}
		vector<string> tmp;
		tmp.push_back(word);
		//cout<< "good "<<i+1<<endl;
		for (int j=0; j<poss.size(); j++){
			int c;
			for (c=0; c<L; c++)
				if (tmp[0][c]==' ')
					break;
			//cout<< "bad "<<j<<endl;
			vector<string> tmp2;
			for (int k=0; k<poss[j].size(); k++){
				for (int l=0; l<tmp.size(); l++){
					string match=tmp[l];
					match[c]=poss[j][k];
					bool ahead=false;
					for (int p=0; p<D;p++){
						bool a = true;
						for (int q=0; q<=c; q++)
							if (match[q]!=words[p][q]){
								a=false;
								break;
							}
						if (a){
							ahead=true; break;
						}
							
					}
					if (ahead)
						tmp2.push_back(match);
				}
				
			}
			tmp=tmp2;		
		}
		int s=0;
		for (int j=0; j<D;j++)
			if (find(tmp.begin(), tmp.end(), words[j])!=tmp.end())
				s++;
		
		fout <<"Case #"<<i+1<<": "<<s<<endl;
	}
}

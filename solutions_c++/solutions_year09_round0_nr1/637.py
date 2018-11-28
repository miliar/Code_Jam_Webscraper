#include<iostream>
#include<vector>
#include<set>
#include<string>

using namespace std;

int main() {
	int L, D, N;
	cin>>L>>D>>N;
	vector<string> words;
	
	for(int i=0;i<D;i++) {
		string word;
		cin>>word;
		words.push_back(word);
	}
	
	for(int i=0;i<N;i++) {
		string pattern;
		cin>>pattern;
		vector<set<char> > tokens(L);
		string::iterator it = pattern.begin();
		int j=0;
		while(j<L) {
			if(*it=='(') {
				it++;
				while(*it!=')') {
					tokens[j].insert(*it);
					it++;
				}
				it++;
				j++;
			}
			else {
				tokens[j].insert(*it);
				j++;
				it++;
			}
		}
		int count = 0;
		for(int k=0;k<D;k++) {
			string word = words[k];
			int flag = 0;
			for(int l=0;l<L;l++) {
				if(tokens[l].find(word[l])==tokens[l].end()) {
					flag = 1;
					break;
				}
			}
			if(flag==0) {
			    count++;
			}
		}
			
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	
	return 0;
}

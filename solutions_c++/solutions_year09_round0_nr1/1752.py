#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<string> words;
int L,N,D;
string pattern;

bool compare(const string& first, const string& second){
	int length = first.size();
	if(length > second.size()){
		length=second.size();
	}
	return first.substr(0,length)<second.substr(0,length);
}

int count(string word, int position){
	int ret = 0;
	if(word.length()==L){
		return binary_search(words.begin(),words.end(),word,compare);
	}else{
		char next = pattern[position];
		if(next=='('){
			next=pattern[++position];
			int nextPosition = position+1;
			while(pattern[nextPosition]!=')')
				nextPosition++;
			while(next!=')'){
				if(binary_search(words.begin(),words.end(),word+next,compare)){
					ret += count(word+next,nextPosition+1);
				}
				position++;
				next=pattern[position];
			}
		}else{
			return count(word+pattern[position],position+1);
		}	
	}
	return ret;
}

int main(){
	cin >> L >> N >> D;
	string word;
	for(int i=0;i<N;i++){
		cin >> word;
		words.push_back(word);
	}
	sort(words.begin(),words.end());
	for(int i=0; i<D;i++){
		cin>>pattern;
		cout<<"Case #"<<(i+1)<<": "<<count(string(""),0)<<endl;
	}
}
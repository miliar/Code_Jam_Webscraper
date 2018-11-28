#include<algorithm>
#include<iostream>
#include<iterator>
#include<string>
#include<stack>
#include<vector>
using namespace std;

template<class Iterator>
std::vector<std::string>
separate(Iterator first,Iterator end) {
	std::vector<std::string> strs;

	bool nest=false;
	std::string tmp;
	for(;first!=end;++first) {
		if(*first=='(') {
			nest=true;
		}
		else if(*first==')') {
			strs.push_back(tmp);
			tmp.clear();
			nest=false;
		}
		else {
			if(nest)
				tmp+=*first;
			else {
				std::string s;
				s+=*first;
				strs.push_back(s);
			}
		}
	}
	return strs;
}

bool find_letter(char ch,std::string s){
	for(size_t i=0;i<s.size();i++){
		if(ch==s[i])
			return true;
	}
	return false;
}

//void testp(std::vector<std::string> v){
//	for(size_t i=0;i<v.size();++i) {
//		printf("%s\n",v[i].c_str());
//	}
//	return;
//}

int match(std::vector<std::string> dict,std::vector<std::string> tokens){
	int count=0;
	for(size_t i=0;i<dict.size();++i) {
		bool check=true;
		for(size_t itr=0;itr<tokens.size();++itr) {
			char letter=dict[i][itr];
			if(!find_letter(letter,tokens[itr])) {
				check=false;
				break;
			}
		}
		if(check)
			count++;
	}
	return count;
}


int main() {
	int L,D,N; cin>>L>>D>>N;

	vector<string> dict;
	for(int i=0;i<D;++i) {
		string s;cin >> s;
		dict.push_back(s);
	}

	vector<string> statements;
	for(int i=0;i<N;++i) {
		string s;cin >> s;
		statements.push_back(s);
	}

	for(size_t i=0;i<statements.size();++i) {
		vector<string> tokens
			= separate(statements[i].begin(),statements[i].end());
		int count = match(dict,tokens);
		cout << "Case #"<<i+1<<": "<< count << endl;
	}
	return 0;
}

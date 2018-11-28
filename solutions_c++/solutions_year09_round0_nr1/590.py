#include<iostream>
#include<vector>
#include<string>
using namespace std;
struct Accepts{
	Accepts*next[256];
	Accepts(){
		for(int i=0;i<256;++i)next[i]=0;
	}
	void regist(const char*p){
		unsigned char c=*p;
		if(!next[c])next[c]=new Accepts();
		if(c)next[c]->regist(p+1);
	}
};
pair<char*,char*> fetch(char*&pattern){
	if(*pattern++!='('){
		return std::make_pair(pattern-1,pattern);
	}else{
		char*begin=pattern;
		while(*pattern++!=')');
		return std::make_pair(begin,pattern-1);
	}
}
int solve(Accepts*acc,vector<pair<char*,char*> >::iterator begin,vector<pair<char*,char*> >::iterator end){
	if(begin == end)return 1;
	int count=0;
	for(char*p=begin->first,*e=begin->second;p!=e;++p){
		if(Accepts*next = acc->next[*p]){
			count += solve(next,begin+1,end);
		}
	}
	return count;
}
int solve(Accepts*acc,char*pattern){
	vector<pair<char*,char*> >oks;
	while(*pattern)oks.push_back(fetch(pattern));
	return solve(acc,oks.begin(),oks.end());
}
#include<fstream>
int main(){
//	std::ifstream cin("Debug/A-small-attempt1.in");

	Accepts accepts;
	int L,D,N;
	cin >> L >> D >> N;
	string word;
	for(int i=0;i<D;++i){
		cin >> word;
		accepts.regist(&word[0]);
	}
	for(int i=1;i<=N;++i){
		cin >> word;
		cout << "Case #"<<i<<": " << solve(&accepts,&word[0]) << endl;
	}
}
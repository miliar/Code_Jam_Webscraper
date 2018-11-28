#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;


int rek(int len,int pos, VI &vi,int used,const string &s){
	if(pos==len){
		string s2=s;
//		for(int i=0;i<len;i++)
//			cerr << vi[i] << " " ;
//		cerr << endl;	
		for(int i=0;i<(int)s.size();i++){
			int p=i%len;
			int off=len*(i/len);
			s2[i]=s[off+vi[p]];
		}
//		cerr << "s2: "<<s2 << " " << s << endl;
		int cnt=0;
		char old=' ';
		for(int i=0;i<(int)s2.size();i++){
			if(s2[i]!=old){
				cnt++;
				old=s2[i];
			}
		}
		return cnt;
	}
	int ma=s.size();
	for(int i=0;i<len;i++){
		if(!(used&(1<<i))){
			used=used+(1<<i);
			pos++;
			vi.push_back(i);

			ma=min(rek(len,pos,vi,used,s),ma);
			
			used=used-(1<<i);
			pos--;
			vi.pop_back();
		}
	}
	return ma;
}

int doit(){
	string s;
	int len;
	cin >> len >> s;
	if(s.size()==0) cin >> s;
	VI vi;
	return rek(len,0,vi,0,s);
	

}	

int main(){
	int num_cases;
	cin >> num_cases;
	for(int kase=1;kase<=num_cases;kase++){
		cout << "Case #"<<kase<<": "<< doit()<<endl; 
	}	
	return 0;
}	

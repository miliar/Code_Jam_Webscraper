#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;
#define forn(i,s,e) for(int i=s;i<e;i++)
typedef map<string,string> Combine;
typedef map<string,string> Opposed;
typedef Combine::iterator iC;
typedef Opposed::iterator iO;
int main(int argc,char* argv[]){
	int T;
	ifstream fin(argv[1],ios::in);
	fin>>T;
	forn(i,0,T){
		std::cout<<"Case #"<<i+1<<": [";
		int C,D,N;
		Combine comb;
		Opposed opp;
		fin>>C;
		forn(j,0,C){
			string t;
			fin>>t;
			comb.insert(pair<string,string>(t.substr(0,2),string(1,t[2])));
			comb.insert(pair<string,string>(string(1,t[1])+string(1,t[0]),string(1,t[2])));
		}
		fin>>D;
		forn(j,0,D){
			string t;
			fin>>t;
			opp.insert(pair<string,string>(string(1,t[0]),string(1,t[1])));
			opp.insert(pair<string,string>(string(1,t[1]),string(1,t[0])));
		}
		fin>>N;
		string r;
		fin>>r;
		string t;
		t.push_back(r[0]);
		forn(j,1,N){	
			iC x = comb.begin();
			iO y = opp.begin();
			t.push_back(r[j]);
			if(t.length()>1){
				if( (x=comb.find(t.substr(t.length()-2,2))) != comb.end() ){
					t.replace(t.length()-2,2,x->second);
				}
				else if( (y=opp.find(t.substr(t.length()-1,1))) != opp.end() ){
					if(t.find(y->second)!=string::npos)
						t="";
				}	
			}
		}
		if(t.length()>0){
			forn(j,0,t.length()-1){
				std::cout<<t[j]<<", ";
			}
			std::cout<<t.substr(t.length()-1,1);
		}
		std::cout<<"]\n";
	}
	return 0;
}
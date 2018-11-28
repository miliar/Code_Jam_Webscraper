#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <list>
#include <utility>

using namespace std;

int main(){
	int caseCount = 0;
	cin >> caseCount;
	cin.ignore();
	for(int i=0;i<caseCount;i++){
		string inText;
		int nonbaseCount=0;
		map< pair<char,char>,char >nonbase;
		int opposeCount=0;
		map<char,char> oppose;
		int baseCount =0;
		list<char> base;
		//get input
		getline (cin,inText);
		stringstream streamInText(inText);
		streamInText >> nonbaseCount;
		for(int j=0;j<nonbaseCount;j++){
			string nonbaseStr;
			streamInText >> nonbaseStr;
			pair<char,char> p;
			p.first = nonbaseStr[0];
			p.second = nonbaseStr[1];
			nonbase[p]=nonbaseStr[2];
			p.first = nonbaseStr[1];
			p.second = nonbaseStr[0];
			nonbase[p]=nonbaseStr[2];
		}
		streamInText >>opposeCount;
		for(int j=0;j<opposeCount;j++){
			string opposeStr;
			streamInText >> opposeStr;
			oppose[opposeStr[0]]=opposeStr[1];
			oppose[opposeStr[1]]=opposeStr[0];
		}
		streamInText >> baseCount;
		pair<char,char> p;
		char baseChar;
		char combineChar;
		map< pair<char,char>, char>::iterator nonbase_it;
		map< char, char>::iterator oppose_it;
		for(int j=0;j<baseCount;j++){
			bool  c = false;
			streamInText >> baseChar;
			p.first = base.back();
			p.second = baseChar;
			if((nonbase_it=nonbase.find(p))!=nonbase.end()){
				base.pop_back();
				baseChar=nonbase_it->second;
				c =true;
			}
			base.push_back(baseChar);

			if(c==false)
			if((oppose_it=oppose.find(baseChar))!=oppose.end()){
				for (list<char>::iterator it = base.begin(); it != base.end(); it++){
				if(*it==oppose_it->second){
				base.clear();
break;
}
}
			}
		}
		//return output

		cout << "Case #"<<i+1<<": [";
		bool f = true;
		for (list<char>::iterator it = base.begin(); it != base.end(); it++){
			if(!f)cout<<", ";
			f=false;
			cout << *it;
		}
		cout << "]" <<endl;
	}
}

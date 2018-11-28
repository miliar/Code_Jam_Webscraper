#include<iostream>
#include<map>
#include<set>
#include<list>
#include<string>

using namespace std;

int main(){
	int cas;
	cin>>cas;
	for(int ca=1; ca<=cas; ++ca){
		int c,d,n;
		string s;
		set<string> good, bad;
		map<string, char> goods;
		list<char> rtn;
		cin>>c;
		for(int i=0; i<c; ++i){
			cin>>s;
			string cur = s.substr(0,2);
			string cur2;
			cur2.append(1,cur[1]);
			cur2.append(1,cur[0]);
			good.insert(cur);
			good.insert(cur2);
			goods[cur] = s[2];
			goods[cur2] = s[2];	
		}
		cin>>d;
		for(int i=0; i<d; ++i){
			cin>>s;
			string cur2;
			cur2.append(1,s[1]);
			cur2.append(1,s[0]);
			bad.insert(s);
			bad.insert(cur2);			
		}
		cin>>n;
		cin>>s;
		list<char>::iterator it;
		for(int i=0; i<n; ++i){
			if( rtn.size() ==0 ){
				rtn.push_back(s[i]);
				continue;
			}
			char l = rtn.back();
			string check;
			check.append(1, l);
			check.append(1, s[i]);
			if( good.find(check) != good.end()) {
				rtn.pop_back();
				rtn.push_back(goods[check]);
			} else {
				
				bool found = false;
				for( it  = rtn.begin(); it != rtn.end(); it++){
					string check2;
					check2.append(1,(*it));
					check2.append(1, s[i]);
					if (bad.find(check2) != bad.end()){
						rtn.clear();
						found = true;
						break;
					}
				}
				if(!found)
					rtn.push_back(s[i]);
			}
			
		}
		if(rtn.size()==0){
			cout<<"Case #"<<ca<<": []"<<endl;
		}else {
			it  = rtn.begin();
			cout<<"Case #"<<ca<<": ["<<(*it);
			for( it++ ; it != rtn.end(); it++){
				cout<<", "<<(*it);
			}
			cout<<"]"<<endl;
		}
	}
}
#include<iostream>
#include<string>
#include<cstring>
#include<set>
using namespace std;
string dict[10000];
string order;
string chosen;
int ci;
int n,m;


int compute(set<int> s, int l){
	s.erase(ci);
//cout<<chosen<<" "<<s.size()<<"!!!"<<endl;
	if(s.size()==0)
		return 0;
	int pt = 0;
	int pos[11];
	set<int> temp;
	for(int i=0; i<26; ++i){
		char c = order[i];
		int next =0;
		for(int j=0; j<l; ++j){
			if(chosen[j] == c){
				pos[next++] = j;
			}
		}
//cout<<"blah: "<<next<<endl;
		set<int>::iterator it; 
		
		
		if(next ==0 ){
			for(it = s.begin(); it!=s.end(); it++){
				string cur = dict[*it];
				bool in = true;
				for(int j=0; j<l; ++j){
					if ( cur[j] == c) {
						in = false;
						break;
					}
				}
				if(in){
//cout<<c<<" "<<cur<<" added back"<<endl;
					temp.insert(*it);
				}
			}
//cout<<s.size()<<" "<<temp.size()<<endl;
			if ( s.size() != temp.size() ){
				++pt;
			} 
			
		}else {
			for(it = s.begin(); it!=s.end(); it++){
				string cur = dict[*it];
				bool in = true;
				bool found_one = false;
				int nn = 0;
				for(int j=0; j<l; ++j){
					if ( cur[ j ] == c){
						found_one = true;
						if(nn == next || pos[nn++] != j){
							in = false;
							break;
						}
					}
				}
				if(found_one && in && nn==next){
					temp.insert(*it);
				}
			}
		}
//cout<<"\t\t"<<c<<" "<<pt<<endl;
		s = temp;
		if ( s.size() == 0){
			return pt;
		}
		temp.clear();
	}
	return pt;
}

int main(){
	int cas;
	cin>>cas;
	string s;
	for(int ca = 1; ca<=cas; ++ca){
		
		cin>>n>>m;
		set<int> di[11];
		
		for(int i=0; i<n; ++i){
			cin>>dict[i];
			di[dict[i].size()].insert(i);
		}
		string res = "";
		for(int i=0; i<m; ++i){
			cin>>order;
			int maxx=-1;
			string rtn="";
			for(int i=0; i<n; ++i){
				ci = i;
				chosen = dict[i];
				int temp = compute(di[dict[i].size()], dict[i].size());
//cout<<"\t"<<chosen<<" "<<temp<<endl;
				if(temp>maxx){
					maxx = temp;
					rtn = dict[i];
				}
			}
			res += (" " + rtn);
		}
		cout<<"Case #"<<ca<<":"<<res<<endl;
	}
}

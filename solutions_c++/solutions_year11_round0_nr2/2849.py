#include <iostream>
#include <string>
#include <list>
using namespace std;

struct Element{
	bool opponent[128];
	char combi[128];
	Element(){
		for(int i=0;i<128;i++){opponent[i]=false;}
		for(int i=0;i<128;i++){combi[i]=0;}
	}
};

int main(){
	int t;
	cin>>t;
	for(int case_num=1;case_num<=t;case_num++){
		Element elem_map[128];
		string s;

		int c;
		cin>>c;
		for(int i=0;i<c;i++){
			cin>>s;
			elem_map[s[0]].combi[s[1]]=s[2];
			elem_map[s[1]].combi[s[0]]=s[2];
		}

		int d;
		cin>>d;
		for(int i=0;i<d;i++){
			cin>>s;
			elem_map[s[0]].opponent[s[1]]=true;
			elem_map[s[1]].opponent[s[0]]=true;
		}

		int n;
		cin>>n;
		cin>>s;
		int count[128];
		list<char> result;
		list<char>::iterator chk;
		for(int i=0;i<128;i++){count[i]=0;}
		for(string::const_iterator iter=s.begin();iter!=s.end();iter++){
			if(!result.empty()){
				chk=result.end();
				char newchr=elem_map[*iter].combi[*(--chk)];
				if(newchr){
					count[newchr]++;
					result.push_back(newchr);
					count[*chk]--;
					result.erase(chk);
					continue;
				}
				bool continue_flg=false;
				for(int i=0;i<128;i++){
					if(elem_map[*iter].opponent[i]&&count[i]){
						for(int j=0;j<128;j++){count[j]=0;}
						result.clear();
						continue_flg=true;
						break;
					}
				}
				if(continue_flg)continue;
				count[*iter]++;
				result.push_back(*iter);
			}else{
				count[*iter]++;
				result.push_back(*iter);
			}
		}		

		cout<<"Case #"<<case_num<<": [";
		for(list<char>::const_iterator iter=result.begin();iter!=result.end();iter++){
			cout<<*iter;
			if((++iter)--!=result.end()){cout<<", ";}
		}
		cout<<"]"<<endl;
	}

	return 0;
}
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;

map<string,string> change;
set<string> del;
map<string,string>::iterator it;
int C,D;
int n;
int main(){
	int T;
	cin>>T;
	for(int tc = 1; tc<=T;tc++){
		string ans = "";
		string ss;
		change.clear();
		del.clear();
		cin>>C;
		while(C--){
			cin>>ss;
			if(ss[0]>ss[1])swap(ss[0],ss[1]);
			change.insert(make_pair(ss.substr(0,2),ss.substr(2,1)));
		}
		cin>>D;
		while(D--){
			cin>>ss;
			if(ss[0]>ss[1])swap(ss[0],ss[1]);
			del.insert(ss);
		}
		cin>>n;
		cin>>ss;
		for(int i=0;i<n;i++){
			char ch = ss[i];
			bool update = true;
			while(update){
				update = false;
				if(ans.size() > 0){
					string pr = string("") + (ans[ans.size() - 1]) + ch;
					if(pr[0] > pr[1])swap(pr[0],pr[1]);
					it = change.find(pr);
					if(it==change.end()){
						bool ok = true;
						for(int j = 0;j<ans.size();j++){
							pr = string("") + ans[j] + ch;
							if(pr[0] > pr[1])swap(pr[0],pr[1]);
							if(del.find(pr)!=del.end()){
								ok = false;
								ans = "";
								break;
							}
						}
						if(ok)ans = ans + ch;
					}
					else {
						ans = ans.substr(0,ans.size() - 1);
						ch = it->second[0];
						update = true;
					}
				} else ans = ans + ch;
			}
		}
		printf("Case #%d: ",tc);
		putchar('[');
		for(int i=0;i<ans.size();i++){
			i && printf(", ");
			putchar(ans[i]);
		}
		printf("]\n");
	}
	return 0;
}

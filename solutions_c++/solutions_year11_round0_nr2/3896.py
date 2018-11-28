#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
using namespace std;



int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	string s;
	int t;
	cin>>t;
	getline(cin,s);
	for(int i=1;i<=t;i++){
		getline(cin,s);
		int c=s[0]-'0',j=0;
		s=s.substr(2);
		char x,y,z;
		map<pair<char,char>,char> elem;
		map<char,char> opp;
		for(j=0;j<c;j+=3){
			x=s[j];
			y=s[j+1];
			z=s[j+2];
			elem[make_pair(x,y)]=z;
			elem[make_pair(y,x)]=z;
		}
		if(c!=0)s=s.substr(j+1);
		int d=s[0]-'0';
		s=s.substr(2);
		for(j=0;j<d;j+=2){
			x=s[j];
			y=s[j+1];
			opp[x]=y;
			opp[y]=x;
		}
		if(d!=0)s=s.substr(j+1);
		s=s.substr(2);
		vector<char>res;
		char a,b;
		while(true){
			if(s[0]!=' ')break;
			s=s.substr(1);
		}
		//cout<<s<<"__________________________________"<<endl;

		res.push_back(s[0]);
		for(j=1;j<s.size();j++){
			///////////// compine part
			if(!res.empty()){
				pair<char,char> p=make_pair(s[j],res.back());
				if(elem.count(p)){
					res.pop_back();
					res.push_back(elem[p]);
					continue;
				}
			}
			//opposite
			if(find(res.begin(),res.end(),opp[s[j]])!=res.end())
			{
				res.clear();
				continue;
			}
			res.push_back(s[j]);

		}
		cout<<"Case #"<<i<<": [";
		for(int k = 0;k<res.size();k++){
			if(k!=res.size()-1)cout<<res[k]<<", ";
			else cout<<res[k];
		}
		cout<<"]"<<endl;
	}


	return 0;
}

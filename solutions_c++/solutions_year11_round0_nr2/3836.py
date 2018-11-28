#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	int test;
	cin>>test;
	for(int counter=1;counter<=test;counter++){
	map<string,string> combination;
	map<string,string> destruction;
	int c;
	string result="";
	map <char,int> present;
	map<char,vector<char> > trouble;
	cin>>c;
	while(c--){
		string pairs;
		cin>>pairs;
		string item=pairs.substr(0,2);
		string match=pairs.substr(2,1);
		combination[item]=match;
		reverse(item.begin(),item.end());
		combination[item]=match;
	}
	int d;
	cin>>d;
	while(d--){
		string pairs;
		cin>>pairs;
		destruction[pairs]=1;
		reverse(pairs.begin(),pairs.end());
		destruction[pairs]=1;
		for(int cnt=0;cnt<=1;cnt++){
			int acnt=(cnt+1)%2;
			if(trouble.find(pairs[cnt])!=trouble.end()){
				trouble[pairs[cnt]].push_back(pairs[acnt]);
			}
			else{
				vector<char> newarr;
				newarr.push_back(pairs[acnt]);
				trouble[pairs[cnt]]=newarr;
			}
		}
	}
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		char in;
		cin>>in;
		if(result.size()>0){
			char prev=result[result.size()-1];
			string newstring="";
			newstring=newstring+prev;
			newstring=newstring+in;
			if(combination.find(newstring)!=combination.end()){
				result=result.substr(0,result.size()-1);
				result+=combination[newstring];
				continue;
			}
			else if(destruction.find(newstring)!=destruction.end()){
				//cout<<"DESTRUCTION "<<newstring<<endl;
				result=result.substr(0,result.size()-1);
				continue;
			}
			else if(trouble.find(in)!=trouble.end()){
				vector<char> tsome=trouble[in];
				bool done=false;
				for(int j=0;j<tsome.size();j++){
					if(result.find(tsome[j])!=string::npos){
						//cout<<"REMOVING DUE TO "<<tsome[j]<<" "<<in<<endl;
						result="";
						done=true;
						break;
					}
				}
				if(!done)
					result=result+in;
			}
			else {
			//cout<<"NORMAL CASE "<<in<<endl;
			result=result+in;
			}
		}
		else
			result=result+in;
		}
	cout<<"Case #"<<counter<<": [";
	for(int i=0;i<result.size();i++){
		cout<<result[i];
		if(i<result.size()-1)
			cout<<", ";
	}
	cout<<"]\n";
	}
}

#include<iostream>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<vector>
using namespace std;
#define MP make_pair
string pattern = "welcome to code jam";

char allow[500];
int res;

void doit(int n, int start, vector<pair<char, int> >& v, int r){
	if(n==pattern.length()){
		res+=r;
		return ;
	}
	for(int i=start; i<v.size(); i++){
		if(v[i].first == pattern[n])
			doit(n+1, i+1, v, (r*v[i].second)%10000);
	}
}

int main(){
	for(int i=0; i<pattern.length(); i++) allow[pattern[i]]=1;
	freopen("in.txt","r",stdin);
	freopen("out.txt.","w",stdout);
	int T;
	char line[5000];
	gets(line);
	T = atoi(line);
	for(int TT=1; TT<=T; TT++){
		printf("Case #%d: ",TT);
		gets(line);
		string str=line;
		for(int i=str.length()-1; i>=0;i--){
			if(allow[str[i]]==0) str.erase(i,1);
		}
		vector<pair<char, int> > v;
		v.push_back(MP(str[0],1));
		for(int i=1; i<str.length(); i++)
			if(v.back().first == str[i]) v.back().second++;
			else v.push_back(MP(str[i],1));
		res=0;
		doit(0, 0, v, 1);
		printf("%.4d\n",res);

	}
//while(1);
}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
#define RVAL string

int l,d,n;
string inp[5001];

vector <RVAL> dlimit(string str,char* dlim){
  char cstr[1001]; //***check whether the size is okay***
  vector <RVAL> ret;
  strcpy(cstr,str.c_str());
  char *res = strtok(cstr,dlim);
  while(res!=NULL){
    ret.push_back(string(res));  //***this line needs modification based on return type***
    res=strtok(NULL,dlim);
  }
  return ret;
 
}


void doit(){
	string str;
	vector <string> vs;
	int tmp,tmpa,a[5001],res=0;
	cin>>str;
	//vector <RVAL> ret = dlimit(str,")");
	tmp=str.size();
	memset(a,0,sizeof(a));
	for(int i=0;i<tmp;i++){
		if(str[i]=='('){
			tmpa=i;
			while(str[tmpa]!=')')tmpa++;
			vs.push_back(str.substr(i+1,tmpa-i-1));
			i=tmpa;
		}
		else{
			vs.push_back(str.substr(i,1));
		}
	}
	//cout<<vs.size();for(int i=0;i<vs.size();i++)cout<<vs[i]<<endl;
	if(vs.size()!=l){cout<<"*****ERROR******"<<endl;return;}
	for(int pos=0;pos<l;pos++){
		tmpa=vs[pos].size();
		for(int i=0;i<tmpa;i++){
			for(int j=0;j<d;j++){
				if(inp[j][pos]==vs[pos][i] && a[j]==pos)a[j]++;
			}
		}
	}
	for(int i=0;i<d;i++){
		if(a[i]==l)res++;
	}
	cout<<res<<endl;

}
int main(){
	string str;
	cin>>l>>d>>n;
	for(int i=0;i<d;i++){
		cin>>inp[i]; 
	}
	for(int i=1;i<=n;i++){
		cout<<"Case #"<<i<<": ";
		doit();
	}
	return 0;
}

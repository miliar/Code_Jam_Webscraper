#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


int main(){
	ifstream ifs("data.txt");
	int cases;ifs >> cases;
	string s;
	getline(ifs,s);	
	char mapping[26]={
		'y','h','e','s','o','c','v','x','d',
		'u','i','g','l','b','k','r','z','t',
		'n','w','j','p','f','m','a','q'};
	for(int i=0;i<cases;++i){
		string result="";
		getline(ifs,s);
	//	cout<<s<<endl;
		for(int j=0;j<s.length();++j){
			if(s[j]>='a'&&s[j]<='z'){
				result+=mapping[s[j]-'a'];
			}else if(s[j]==' ')result+=' ';

		}
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	};
	

};


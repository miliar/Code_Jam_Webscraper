#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxn 101000
using namespace std;

char dy[]="yhesocvxduiglbkrztnwjpfmaq";

int main(){
	ios::sync_with_stdio(false);
	int n,i,j;
	string s;
	cin>>n;
		getline(cin,s);
	for(i=1;i<=n;++i){
		getline(cin,s);
		for(j=0;j<s.size();++j)if(isalpha(s[j]))s[j]=dy[s[j]-'a'];
		cout<<"Case #"<<i<<": "<<s<<endl;
	}
	return 0;
}
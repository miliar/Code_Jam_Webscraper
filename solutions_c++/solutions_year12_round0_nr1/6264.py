#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>
#include <list>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <iterator>
#include <sstream>
#include <list>
#include <set>
#include <stack>
#include <bitset>
#include <ctime>
#pragma comment(linker, "/STACK:256000000")
#define EPS 1e-7
#define PI 3.1415926535897932384626433832795
using namespace std;
char ch[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n;
	cin>>n;
	string s;
	getline(cin,s);
	bool b[113];
	for(int t=1;t<=n;t++){
		memset(b,0,sizeof(b));
		getline(cin,s);
		int len=s.length();
		for(char i='a';i<='z';i++){
			for(int j=0;j<len;j++){
				if (s[j]==ch[i-'a'] && !b[j]){
					b[j]=true;
					s[j]=i;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<s<<endl; 
	}
	return 0;
}
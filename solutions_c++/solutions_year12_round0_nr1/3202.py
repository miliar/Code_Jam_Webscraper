#include <iostream>
#include <vector>
#include <stack>
#include <iomanip>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <stdio.h>
using namespace std;

int main(){
	freopen("test.txt","r",stdin);
	freopen("test1.txt","w",stdout);
	char letter[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int k=1;
	string tmp;
	int tc;
	cin >> tc;
	getline(cin,tmp);
	while( tc-- ){
		getline(cin,tmp);
		cout << "Case #" << k++ << ": ";
		int len = tmp.length();
		for(int i=0; i<len; i++){
			if(tmp[i]!=' ')
				cout<<letter[tmp[i]-'a'];
			else
				cout<<" ";
		}
		cout << endl;
	}
	
	return 0;
}
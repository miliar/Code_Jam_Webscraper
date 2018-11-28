#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

int main(){
	string needle("welcome to code jam");
	int T;
	cin>>T;
	cin.ignore();
	for(int c=1; c<=T; c++){
		string haystack;
		getline(cin, haystack);
		vector<int> ways(20, 0);
		ways[0]=1;
		for(int i=0; i<haystack.length(); i++){
			for(int j=18; j>=0; j--)
				if(haystack[i]==needle[j])
					ways[j+1]=(ways[j+1]+ways[j])%10000;
		}
		printf("Case #%d: %04d\n", c, ways[19]);
	}
	return 0;
}

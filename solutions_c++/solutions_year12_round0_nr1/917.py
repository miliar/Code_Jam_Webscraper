/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 09:43:36 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include<iostream>
char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char b[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

using namespace std;

int main(){
	int n;
	cin >> n;
	string s2;
	getline(cin,s2);
	for (int i=1;i<=n;i++){
		string s;
		getline(cin,s);
		for(int j=0;j<s.length();j++){
			if(s[j]!=' ')
				s[j]=b[s[j]-'a'];
		}
		cout << "Case #" << i << ": " << s << endl;
	}
}

/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2012-04-14 10:02:06 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

string map="yhesocvxduiglbkrztnwjpfmaq";

int main(){
	int T;
	cin>>T;
	string sss;
	getline(cin,sss);
	for(int t=0;t<T;t++){
		string s;
		getline(cin,s);
		for(int i=0;i<s.length();i++){
			if(s[i]==' '){
				continue;
			}
			s[i]=map[s[i]-'a'];
		}
		cout<<"Case #"<<t+1<<": "<<s<<endl;
	}
}

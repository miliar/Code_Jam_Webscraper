#include <iostream>
#include <map>
#include <string>
#include <cstdio>

using namespace std;
int main()
{
	string s1,s2,s3,w1,w2,w3;
	s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	w1 = "our language is impossible to understand";
	w2 = "there are twenty six factorial possibilities";
	w3 = "so it is okay if you want to just give up";
	
	int i,j,n;
	map<char,char> M;
	string s;
	
	for(i=0;i<s1.size();i++) M[s1[i]] = w1[i];
	for(i=0;i<s2.size();i++) M[s2[i]] = w2[i];
	for(i=0;i<s3.size();i++) M[s3[i]] = w3[i];
	M['q'] = 'z';
	M['z'] = 'q';
	
	scanf("%d ",&n);
	for(i=0;i<n;i++){
		getline(cin,s);
		cout<<"Case #"<<i+1<<": ";
		for(j=0;j<s.size();j++) cout<<M[s[j]];
		cout<<"\n";
	}
	return 0;
}


	
	

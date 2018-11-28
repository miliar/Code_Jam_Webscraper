#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	//freopen("test.in", "rt", stdin);
	freopen("as.in", "rt", stdin);
	freopen("as.out","wt", stdout);

	char mapping[26]={0};
	string ex[3][2]={
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"our language is impossible to understand",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"there are twenty six factorial possibilities",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		"so it is okay if you want to just give up"};
	for (int i=0;i<3;i++)
		for (int j=0;j<(int)ex[i][0].length();j++)
			if (ex[i][0][j]!=' ')
				mapping[ex[i][0][j]-'a']=ex[i][1][j];
	mapping['q'-'a']='z';
	mapping['e'-'a']='o';
	mapping['y'-'a']='a';

	bool alreadyUsed[26]={0};
	for (int i=0;i<26;i++)
		if (mapping[i]!=0)
			alreadyUsed[mapping[i]-'a']=true;
	for (int i=0;i<26;i++)
		if (alreadyUsed[i]==false) {
			mapping['z'-'a']=i+'a';
			break;
		}


	int nCases;
	cin>>nCases;
	string g;
	getline(cin,g);
	for (int nCase=1;nCase<=nCases;nCase++) {
		cout<<"Case #"<<nCase<<": ";

		getline(cin,g);
		for (int i=0;i<(int)g.length();i++)
			if (g[i]==' ') cout<<" ";
			else cout<<mapping[g[i]-'a'];
		cout<<endl;
	}

	return 0;
}

#include<iostream>
#include<cstdio>
#include<map>
using namespace std;
bool h[26];
int main(){
	char r[4][100]={
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	},p[4][100]={
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	};
#ifndef ONLINE_JUDGE
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	map<char,char> M;
	for(int i=0; i<3; i++){
		int j=0;
		while(r[i][j]!=0){
			M[r[i][j]]=p[i][j];
			j++;
		}
	}
	M['q']='z';
	M['e']='o';
	M[' ']=' ';
//	M['z']='1';
	int t;
	cin>>t;
	char s[105],s1[105];
	for(map<char,char>::iterator it=M.begin(); it!=M.end(); it++){
		h[it->second-'a']=1;
	}
	for(int i=0; i<26; i++)
		if(!h[i])M['z']='a'+i;
//*
for(int i=0; i<t; i++){
		scanf("\n");
		gets(s);
		int j=0;
		while(s[j]!=0){
			s1[j]=M[s[j]];
			j++;
		}
		s1[j]=0;
		printf("Case #%d: %s\n",i+1,s1);
	}
//*/

	return 0;
}
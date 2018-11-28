/*
 * A.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: Yasser
 */


#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

vector<string> v;

int fun(string s){
	vector<string> v2;
	for(int i=0;i<s.size();i++){
		string s2 = "";
		if(s[i] == '('){
			int j=i+1;
			while(s[j]!=')')
				s2+=s[j],j++;
			i = j;
		}else{
			s2 += s[i];
		}
		v2.push_back(s2);
	}
	int sol = 0;
	for(int i=0;i<v.size();i++){
		int j=0;
		for(j=0;j<v[i].size();j++){
			if(v2[j].find(v[i][j])==string::npos)
				break;
		}
		if(j== v[i].size())
			sol++;
	}
	return sol;
}

int main(){
	freopen("in.in","rt",stdin);
	freopen("in.txt","wt",stdout);
	int l,d,n;
	string str;
	cin>>l>>d>>n;
	for(int i=0;i<d;i++){
		cin>>str;
		v.push_back(str);
	}

	for(int i=0;i<n;i++){
		cin>>str;
		printf("Case #%d: %d\n",i+1,fun(str));
	}


	return 0;
}

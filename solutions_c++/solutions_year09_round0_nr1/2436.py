// CJ09Alien.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int match(vector<string>& p,string& str,int cur,vector<string>& dict)
{
	int count=0;
	for(int i=0;i<p[cur].size();++i)
	{
		str.push_back(p[cur][i]);

		vector<string>::iterator first=lower_bound(dict.begin(),dict.end(),str);
		if(first==dict.end()){
			str.erase(str.end()-1);
			continue;
		}
		if(str.compare(first->substr(0,str.size()))!=0){
			str.erase(str.end()-1);
			continue;
		}

		if(cur==p.size()-1){
				count++;
		}else{
			count+=match(p,str,cur+1,dict);
		}
		str.erase(str.end()-1);
	}
	return count;
}


int _tmain(int argc, _TCHAR* argv[])
{
	
	int L,D,N;
	cin>>L>>D>>N;
	char buf1[80];
	cin.getline(buf1,80);

	vector<string> dict;
	for(int i=0;i<D;++i){
		char buf[80];
		cin.getline(buf,80);
		dict.push_back(string(buf));
	}
	sort(dict.begin(),dict.end());

	vector<vector<string>> pattern;
	for(int i=0;i<N;++i){
		char buf[255];
		cin.getline(buf,255);
		string input(buf);

		pattern.push_back(vector<string>());

		for(int j=0;j<input.size();++j){
			if(input[j]!='('){
				string single;
				single.push_back(input[j]);
				pattern[i].push_back(single);
			}else{
				int close=input.find(')',j);
				string chrs(input.begin()+j+1,input.begin()+close);
				sort(chrs.begin(),chrs.end());
				pattern[i].push_back(chrs);
				j=close;
			}
		}
	}

	for(int i=0;i<N;++i){
		vector<string>& p=pattern[i];
		cout<<"Case #"<<(i+1)<<": ";
		string str;
		cout<<match(p,str,0,dict)<<endl;

	}

	//cin.getline(buf1,80);
	return 0;
}


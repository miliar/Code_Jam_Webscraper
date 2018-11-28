#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int makedir2(string old,string newd){
	int j=0,k=0,md=1000;
	int oldsl=0,newsl=0;
	while (j<old.size() && k<newd.size()){
		if (old[j]!=newd[k]) break;
		if (old[j]=='/') oldsl++;
		j++;k++;
	}
	if (j==old.size() && k==newd.size()) return 0;
	if (j==old.size() && k!=newd.size()){
		if (newd[j]=='/'){
			md=0;
			for (int i=j;i<newd.size();i++)
				if (newd[i]=='/') md++;
		}
		else{
			md=0;
			for (int i=0;i<newd.size();i++)
				if (newd[i]=='/') md++;
			md -= (oldsl-1);
		}
	}
	if (j!=old.size() && k==newd.size()){
		if (old[k]=='/') md=0;
		else{
			md=0;
			for (int i=0;i<newd.size();i++)
				if (newd[i]=='/') md++;
			md -= (oldsl-1);
		}
	}
	if (j!=old.size() && k!=newd.size()){
		for (int i=0;i<newd.size();i++){
			if (newd[i]=='/') newsl++;
		}
		if (old[j-1]=='/')
			return newsl-(oldsl-1);
		else
			return newsl-oldsl+1;
	}
	return md;
}

int makedir(vector<string> dir,string s){
	int minimum = 1000;
	for (int i=0;i<dir.size();i++){
		int mk2 = makedir2(dir[i],s);
		if (mk2 < minimum) minimum=mk2;
	}
	if (minimum==1000){
		minimum=0;
		for (int i=0;i<s.size();i++){
			if (s[i]=='/') minimum++;
		}
	}
	return minimum;
}

int main(){

	freopen("a_big.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases,N,M,mk=0;
	
	cin >> cases; 

	for (int casenum=1;casenum<=cases;casenum++){
		vector<string> dir;
		cin >> N >> M;
		mk = 0;
		for (int i=0;i<N;i++){
			string s;
			cin >> s;
			dir.push_back(s);
		}
		for (int i=0;i<M;i++){
			string s;
			cin >> s;
			int mk0 = makedir(dir,s);
			//cout << "mk0:"<<mk0<<endl;
			if (mk0>0) dir.push_back(s);
			mk += mk0;
		}
		cout << "Case #" << casenum << ": " << mk << endl;
	}
	return 0;
}
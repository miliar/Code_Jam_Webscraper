#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 
#define iter(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


string intToStr(int x){
	stringstream vystup;
	vystup << x;
	return vystup.str();	
}


main(){
	ofstream fout ("C-large-attempt0.out");
	ifstream fin ("C-large-attempt0.in");
	int magic_constant=2000001;
//	int magic_constant=20000;
	vector<string> norm_form(magic_constant);
	
	FOR(i,magic_constant){
		string actual = intToStr(i);
		vector<string> variants;
		FOR(j,sz(actual)){			
			variants.push_back(actual);
			actual.append(actual.begin(),actual.begin()+1);
			actual.erase(actual.begin());
		}
		sort(all(variants));
		norm_form[i]=variants[0];
	}
	
	int T;
	fin>>T;
	
	FOR(num,T){
		long long out=0;
		map<string,int> words;
		int a,b;
		fin>>a>>b;
		for(int i = a ; i<=b ; i++){
			if (!words.count(norm_form[i]))
				words[norm_form[i]]=1;
			else words[norm_form[i]]++;
		}
		iter(words,it){
			if (it->second > 1){
				out+=((it->second)*(it->second-1))/2;
			}
		}

		
		fout<<"Case #"<<num+1<<": "<<out<<endl;
	}
	fout.close();
}

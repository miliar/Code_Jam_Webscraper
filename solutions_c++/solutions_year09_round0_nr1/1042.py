#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>
using namespace std;
set<string> conj;
set<string> pref[20];
int L,D,N;

int solve(string &s, int index, string tmp, int letter){
	if(pref[letter].find(tmp) == pref[letter].end()) return 0;
	if(tmp.size() >= L){
		if(conj.find(tmp) != conj.end()) return 1;
		return 0;
	}
	if(s[index] == '('){
		int ret = 0;
		int end;
		for(int i = index+1; ;i++)
			if(s[i] == ')'){
				end = i;
				break;
			}
		for(int i = index+1; i<end; i++)
			ret += solve(s,end+1,tmp+s[i],letter+1);
		return ret;
	}
	else{
		return solve(s,index+1,tmp + s[index],letter+1);
	}
}

int main()
{
	//FILE *in  = fopen("A-small-attempt1.in","r");
	//FILE *out = fopen("A-small-attempt1.out","w");
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");


	string tmp;
	
	in >> L >> D >> N;
	pref[0].insert("");
	for(int i = 0; i<D; i++){
		in >> tmp;
		for(int j = 0; j<tmp.size(); j++)
			pref[j+1].insert(tmp.substr(0,j+1));
		conj.insert(tmp);
	}
	cout << N << " casos " << endl;
	for(int t = 0; t<N; t++){
		cout << "resuelto caso " << t << endl;
		int ret = 0;
		in >> tmp;
		ret = solve(tmp,0,"",0);
		out << "Case #" << t+1 << ": " << ret << endl;
	}
    return EXIT_SUCCESS;
}

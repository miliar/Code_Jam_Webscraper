#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

map<string,char> X,Y;
int n;
void work(){
	cin >> n;
	X.clear();
	for (int i=0;i<n;i++){
		string s;cin >> s;
		string tmp="";
		tmp+=s[0];
		tmp+=s[1];
		X[tmp]=s[2];
		tmp="";
		tmp+=s[1];
		tmp+=s[0];
		X[tmp]=s[2];
	}
	cin >> n;
	Y.clear();
	for (int i=0;i<n;i++){
		string s;cin >> s;
		string tmp="";
		tmp+=s[0];
		tmp+=s[1];
		//cout << tmp <<endl;
		Y[tmp]='A';
		tmp="";
		tmp+=s[1];
		tmp+=s[0];;
		Y[tmp]='A';
	}
	int tmp;
	string s;
	cin >> tmp >> s;
	vector<char> ret;ret.clear();
	for (int i=0;i<s.size();i++){
		ret.push_back(s[i]);
		while (ret.size()>=2){
			char ch1=ret[ret.size()-1],ch2=ret[ret.size()-2];
			string tmp="";
			tmp+=ch1;
			tmp+=ch2;
			if (X.find(tmp)!=X.end()){
				ret.pop_back();ret.pop_back();
				ret.push_back(X[tmp]);
				continue;
			}
			break;
		}
		if (ret.size()>=2){
			for (int j=0;j<ret.size()-1;j++){
				string tmp="";
				tmp+=ret[j];
				tmp+=ret[ret.size()-1];
				if (Y.find(tmp)!=Y.end()) {ret.clear();break;}
			}
		}
	}
	cout <<"[";
	for (int i=0;i<ret.size();i++){
		cout << ret[i];
		if (i!=ret.size()-1) cout << ", ";
	}
	cout <<"]"<<endl;
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ": ";
		work();
	}
	//system("pause");
	return 0;
}
/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
*/

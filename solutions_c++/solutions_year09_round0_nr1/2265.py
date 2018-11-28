#include <iostream>
#include <string>

#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <map>
#include <set>

using namespace std;


void onecase(int casenum, const string& s, const vector<vector<int> >& dict, int lnum, int dnum){
//first convert the pattern into structure
//Since the words consist lower letter, let's use
//A int to indicate the pattern.
//e.g. 0x00000001 represents 'a' while 0x00000003 represents '(ab)'
vector<int> pattern;
	int wsize = s.size();
	int braflag = 0;
	int subpat = 0;
	for(int i=0; i<wsize;i++){
		if(s[i] == '('){
			braflag = 1;
		}else if(s[i] == ')'){
			braflag = 0;
			pattern.push_back(subpat);
			subpat = 0;
		}else if(braflag){
			if(s[i] >= 'a' && s[i] <= 'z'){
				subpat |= (0x1 <<int(s[i] - 'a'));
			}else{
				cerr<<"Pos2: bad letter met:"<<s[i]<<" and discarded"<<endl;
			}
		}else{
			if(s[i] >= 'a' && s[i] <= 'z'){
				pattern.push_back(0x1 <<int(s[i] - 'a'));
			}else{
				cerr<<"Pos 1: bad letter met:"<<s[i]<<" and discarded"<<endl;
			}
		}
	}
	//Now the pattern is ready. check the dictionary
	int counter = 0;
	for(int k=0;k<dict.size();k++){
		int allmatchflag = 1;
		for(int x=0;x<lnum;x++){
			if(!(dict[k][x] & pattern[x]))
				allmatchflag =0;
		}
		counter += allmatchflag;
	}
	cout<<"Case #"<<casenum<<": "<<counter<<endl;
	return;
}

void allcases(void){
int lnum, dnum, nnum; // L, D, N in first line
//convert the diction to meet the req of pattern in onecase()
//Since the words consist lower letter, let's use
//A int to indicate the pattern.
//e.g. 0x00000001 represents 'a' while 0x00000003 represents '(ab)'
vector<vector<int> > dict;
	cin >> lnum;
	cin >> dnum;
	cin >> nnum;
	int i;
	for(i=0;i<dnum;i++){
		string s;
		cin>>s;
		vector<int> oneword;
		for(int j=0;j<s.size();j++){
			if(s[j] >= 'a' && s[j] <= 'z'){
				oneword.push_back(0x1 <<int(s[j] - 'a'));
			}else{
				cerr<<"bad letter met:"<<s[j]<<" and discarded"<<endl;
			}
		}
		dict.push_back(oneword);
	}
	for(i=0;i<nnum;i++){
		string s;
		cin>>s;
		onecase(i+1, s, dict, lnum, dnum);
	}
}

int main(int argc, char **argv){

	allcases(); 
return 0;
}

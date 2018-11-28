#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <sstream>

using namespace std;

void onecase(int casenum, const string &s, ofstream& fout){

map<int, int> symbols;
int i;

    //The first symbol must be 1, the the later will going on 
    symbols[(int)s[0]] = 1;
    int numstart = 0;
    for(i = 1;i<s.size();i++){
          if(symbols.find((int)s[i]) == symbols.end()){
              //New symbol found, get the new numbers;
              symbols[(int)s[i]] = numstart;
              numstart++;
              if(numstart == 1) numstart++;
          }
    }
    if(numstart == 0) numstart = 2;
    //Now we get the base is numstart.
    //TO caculate the number
    //Need a longlong value
    unsigned long long value = 0L;
    unsigned long long nbase = 1L;
    for(i = s.size()-1;i >= 0;i--){
          
          unsigned long tmp = (unsigned long)symbols[(int)s[i]];
          value+= tmp*nbase;
          nbase *= numstart;
    }
    fout<<"Case #"<<casenum<<": "<<(long long)value<<endl;
	return;
}

void allcases(ifstream& fin, ofstream &fout){
int total;
	fin>>total;
	for(int i=0;i<total;i++){
		string s;
		fin >> s;
		//cout<<"Case #"<<i+1<<": "<<s<<endl;
		onecase(i+1, s, fout);
	}
}

int main(int argc, char **argv){

    if(argc != 3){
            cerr<<"Need 2 parameters!"<<endl;
            return 1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
	allcases(fin, fout); 
return 0;
}

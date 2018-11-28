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

void split2bases(int num, int base, vector<int> & nlist){
    nlist.clear();
    while(num > 0){
        int res = num %base;
        nlist.push_back(res);
        num /= base;
    }
    return;
}

int calcSqSum(const vector<int> & nlist){
int sum = 0;
    for(vector<int>::const_iterator itr = nlist.begin();
        itr != nlist.end(); itr++){
        sum += (*itr) * (*itr);
    }
    return sum;
}

int calcHappy(int num, int base){
vector<int> numlist;
map<int, int> nummeet; /*This record if the number is already calculated. If, so we
                     won't get 1 ever.*/
    while(true){
        split2bases(num, base, numlist);
        num = calcSqSum(numlist);
        if(num == 1) return true;
        if(nummeet.find(num) != nummeet.end()) return false;
        nummeet[num] = 1;
    }
    return false;
}

void onecase(int casenum, string s, ofstream& fout){

vector<int> bases;
    size_t pos = 0;
    while(pos != string::npos){
              size_t npos = s.find(' ', pos+1);
              string sbase = s.substr(pos, npos);
              int ibase = atoi(sbase.c_str());
              if(ibase>=0)
                          bases.push_back(ibase);
              pos = npos;
    }
    int num = 2; //begin to enumerate the number
    int hflag;
    while(num > 0){
        hflag = 1;
        for(vector<int>::iterator itr = bases.begin();
            itr != bases.end(); itr++){
            if(!calcHappy(num, *itr)){
                hflag = 0;
            }
        }
        if(hflag) break;
        num++;
    }
    if(!hflag){
       cerr<<"Error met when in case "<<casenum<<endl;
    }else{
          fout<<"Case #"<<casenum<<": "<<num<<endl;
    }
    
	return;
}

void allcases(ifstream& fin, ofstream &fout){
int total;
	fin>>total;
	char ss[4];
	fin.getline(ss,1,'\n');
	for(int i=0;i<total;i++){
		string s;
		getline(fin,s,'\n');
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

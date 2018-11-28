#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int T;

struct Case
{
	int prinum;
	int Q;
	vector<int> ql;
};

vector<Case> cases;

int input_read(char * filename)
{
	ifstream ifs;
	ifs.open(filename, ios::in);
    
    ifs >> T;

	for(int i=0; i<T; ++i){
		Case c;
		ifs >> c.prinum;
		ifs >> c.Q;
		for(int j=0; j<c.Q; ++j){
			int tmp;
			ifs >> tmp;
			c.ql.push_back(tmp-1);
		}
		cases.push_back(c);
	}

	return 0;
}

int release(int prinum, vector<int> &qlist){
/*
	cout << "[" << prinum << "]";
	for(int i=0; i<qlist.size(); ++i){
		cout << qlist[i] << ",";
	}
	cout << endl;
*/
	int coin=0;
	vector<int> prison(prinum);
	int len=qlist.size();
	for(int i=0; i<len;++i){
		prison[qlist[i]]=1;
		int s=0,e=prinum-1;
		for(int j=0; j<i; ++j){
			if(qlist[j]<qlist[i]&&s<=qlist[j])s=qlist[j]+1;
			if(qlist[j]>qlist[i]&&e>qlist[j])e=qlist[j]-1;
		}
		coin+=e-s;
	}

//	cout << coin << endl;
	return coin;
}

int solve(int prinum, vector<int> qlist){

	int min=release(prinum, qlist);
	while (next_permutation(qlist.begin(), qlist.end())){
        int tmp=release(prinum, qlist);
		if(tmp<min)min=tmp;
	}

    return min;
}



#define INFILE "C-small-attempt0.in"

int main(){
	input_read(INFILE);
	ofstream o(INFILE ".out");

	int n = 0;
	
//#define o cout
	for(vector<Case>::iterator i = cases.begin(), e = cases.end(); i != e; ++i){
		o << "Case #" << ++n << ": " << solve((*i).prinum, (*i).ql) << endl;
	}
}

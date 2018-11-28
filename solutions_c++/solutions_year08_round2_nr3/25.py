// Google Code Jam -- Online Round 1
// 26th July 2008
//
// Problem C - 

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <cmath>
#include <queue>
#include <set>
#include <algorithm>
#include <list>
#include <cstdio>

using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}

struct BinTree{
	BinTree ** children;
	int size,count;
	BinTree(int s){
		children = NULL;
		size = s;
		count = 0;
		if (size <= 1) return;
		children = new BinTree * [2];
		int leftSize = size / 2;
		children[0] = new BinTree(leftSize);
		children[1] = new BinTree(size - leftSize);
	}
	~BinTree(){if (children == NULL) return;delete children[0];delete children[1];delete [] children;}
	void add(int x){
		count++;
		if (children != NULL){
			int leftSize = children[0] -> size;;
			if (x < leftSize) children[0] -> add(x);
			else children[1] -> add(x-leftSize);
		}
	}
	int nthElement(int n){
		if (children == NULL) return 0;
		int leftSize = children[0]->size, countLeft = children[0]->size - children[0]->count;
		if (n < countLeft) return children[0] -> nthElement(n);
		return leftSize + children[1] -> nthElement(n-countLeft);
	}
};


int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		int res = 0;

		int N = get <int> (fin);

		vector <int> v = getv <int> (fin);
		int k = v[0];
		vector <int> d;
		for (int i=1;i<=k;i++)
			d.push_back(v[i] - 1);

		BinTree bTree(N);

		vector <int> output(N);
		int j = 0;
		for (int i=0;i<N;i++){
			int count = N-i;
			j = (j + i) % count;
			int index = bTree.nthElement(j % count);

			output[index] = i+1;
			bTree.add(index);
		}

		fout << "Case #" << cas << ":";
		if (argc == 4) cout  << "Case #" << cas << ":";		
		for (int i=0;i<k;i++){
			fout << " " << output[d[i]];
			if (argc == 4) cout << output[d[i]] << " ";
		}
		fout << endl;
		cout << endl;
	}
	return 0;
}
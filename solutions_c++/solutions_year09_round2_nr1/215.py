// codejam.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <numeric>
#define _USE_MATH_DEFINES 
#include <cmath>
#include <math.h>
using namespace std;

#define sz(v) ((int)(v).size())
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define FSZ(i,a,v) F(i,a,sz(v))
#define all(v) v.begin(),v.end()

// sort Dic
// 24^15 = 
// 5000*15*15*500 

// 24*15 = square by test word
// insert Dic


void test() {
	int N;
	cin >> N;
	string welcome = "welcome to code jam";
	string str;
	getline(std::cin, str);
	for(int t=0; t<N; ++t) {
		getline(std::cin, str);
//		cout << "Case #" << (t+1) << ": " << rr << endl;
	}
}

bool s_sort(string& s, int pos) {
	int p = -1;
	char v = s[pos], nv = '9';
	for(int i=pos+1; i<s.size(); ++i) {
		if(v < s[i] && s[i] <= nv) {
			p = i;
			nv = s[i];
		}
	}
	if(p == -1) return false;
	swap(s[pos], s[p]);
	sort(s.begin()+pos+1, s.end());
	return true;
}

string next(string num) {
	for(int i=num.size()-1; i>=0; --i) {
		bool b = s_sort(num, i);
		if(b) return num;
	}
	num.push_back('0');
	sort(all(num));
	int p=0;
	FSZ(i,0,num) if(num[i]!='0') {
		p = i;
		break;
	}
	swap(num[0], num[p]);
	return num;
}


class Node {
public:
	string s;		// null is end
	double value;
};

map<string, Node> node_map;

void A2() {
	int T;
	cin >> T;
	for(int t=0; t<T; ++t) {
		int lines;
		cin >> lines;
		string tree;
		string str;
		getline(std::cin, str);
		for(int l=0; l<lines; ++l) {
			getline(std::cin, str);
			tree += str;
		}
//		cout << tree;

		node_map.clear();
		string s = "";
		string before;
		FSZ(i,0,tree) {
			if(tree[i] == '(') {
				string ns = s + '0';
				if(node_map.find(ns) != node_map.end()) s += '1';
				else s += '0';

				before = "";
				for(i; tree[i+1]!='(' && tree[i+1]!=')'; ++i)
					before += tree[i+1];

				stringstream ss;
				ss << before;
				string value;
				double v;
				ss >> v >> value;
				node_map[s].value = v;
				node_map[s].s = value;
				before.clear();
			} else if(tree[i] == ')') {
				s.erase(s.size()-1);
			} else {
			}

		}

		int animal;
		cin >> animal;

		cout << "Case #" << (t+1) << ":" << endl;
		for(int i=0; i<animal; ++i) {
			string name;
			int attr;
			cin >> name >> attr;
			string s;
			set<string> attrs;
			for(int j=0; j<attr; ++j) {
				cin >> s;
				attrs.insert(s);
			}

			string chk = "0";
			double value = 1.0;
			while(node_map.find(chk)!=node_map.end()) {
				Node node = node_map[chk];
				value *= node.value;
				if(node.s.size() == 0) break;
				if(attrs.find(node.s)!=attrs.end()) {
					chk += "0";
				} else {
					chk += "1";
				}
			}
			printf("%.7f\n", value);
//			cout << value << endl;
		}
	}
}

void B2() {
	int T;
	cin >> T;
	for(int t=0; t<T; ++t) {
		string num;
		cin >> num;

		string rr = next(num);
		cout << "Case #" << (t+1) << ": " << rr << endl;
	}
}

void C2() {

}

int main(int argc, char* argv[])
{
	A2();
//	B2();
//	C2();
	return 0;
}


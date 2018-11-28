//Arash Rouhani

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>
#include <set>
#include "Primelist.h"

using namespace std;

typedef pair < int, int > II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC > VVC;
typedef stringstream SS;
typedef set < int > SI;
typedef long long  LL;

#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)

struct Node{
	string feature;
	pair < Node*, Node* > children;
	double value;
};

SS alltext;
void parse(Node* subtree);

void parse(Node* subtree){
/*
	for(;;){
		char trash;
		alltext >> trash;
		if(trash == '('){
			break;
		}
	}
	*/
	alltext >> subtree->value;
	for(;;){
		char trash;
		alltext >> trash;
		if(trash == '('){
			subtree->children.first= new Node;
			subtree->children.second= new Node;
			parse(subtree->children.first);
			for(;;){
					char trash;
					alltext >> trash;
					if(trash == '('){
						break;
					}
				}
			parse(subtree->children.second);
		}
		else if(trash == ')'){
			break;
		}
		else if(trash == ' '){

		}
		else{
			subtree->feature.push_back(trash);
		}
	}
}

double score(Node* subtree, set < string > &props){
	double recresult=1;
	if(!subtree->feature.empty()){
		if(props.find(subtree->feature)!=props.end()){
			recresult = score(subtree->children.first, props);
		}
		else{
			recresult = score(subtree->children.second, props);
		}
	}
	return subtree->value*recresult;
}



int main(){
	int N;
	cin >> N;
	sfor(int, testcase, 1, N+1){
		Node root;
		int L;
		cin >> L;
		sfor(int, i, 0, L+1){
			string s;
			getline(cin, s);
			alltext << s;
		}

		char firstparanthesis;
		alltext >> firstparanthesis;

		parse(&root);

		cout << "Case #" << testcase << ":\n";

		int A;
		cin >> A;
		sfor(int, i, 0, A){
			string trash;
			cin >> trash;
			int nprops;
			cin >> nprops;
			set < string > props;
			sfor(int, j, 0, nprops){
				string s;
				cin >> s;
				props.insert(s);
			}
			cout << score(&root, props) << endl;
		}
	}
}








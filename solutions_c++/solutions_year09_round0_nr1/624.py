#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> ivec;
typedef vector<string> svec;
typedef vector<double> dvec;
typedef pair<int,int> ipair;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

ifstream fin;
ofstream fout;
int L,D,N;

class TREE{
public:
	char c;
	set<TREE> child;
};


bool operator< (const TREE &t1, const TREE &t2){
		return t1.c<t2.c;
}

bool operator== (const TREE &t1, const TREE &t2){
		return t1.c==t2.c;
}

bool findchar(const set<char> &s, char c){
	for(set<char>::const_iterator it=s.begin();it!=s.end();it++){
		if(*it == c){
			return true;
		}
	}
	return false;
}


void process(TREE &node,int level,int &count,set<char> *token){
	if(level == L){
		count++;
		return;
	}
	for(set<TREE>::iterator iter=node.child.begin();iter!=node.child.end();iter++){
		if(token[level].count(iter->c)){
			process(*iter,level+1,count,token);
		}else{
			continue;
		}
	}
}

void printTREE(const TREE &node, int level, string s){
	if(level != 0){
	string temp(1,node.c);
	s+=temp;
	if(level == L){		
		cout<<s<<endl;
		return;
	}
	}

	for(set<TREE>::const_iterator it=node.child.begin();it!=node.child.end();it++){
		printTREE(*it, level+1,s);
	}
}


int main(){
	fin.open("A-large.in");
//	fout.open("small-result.txt");
	fout.open("large-result.txt");

	string s;
	getline(fin,s);
	stringstream ss(s);
	ss>>L>>D>>N;

	TREE root,ch;
	TREE *node=&root;

	Rep(i,D){
		getline(fin,s);
		node = &root;
		Rep(j,L){			
			ch.c=s[j];
			node = &(*((node->child).insert(ch).first));
		}
	}
//	string s2;
//	printTREE(root,0,s2);

	for(int index=0;index<N;index++){
		fin>>s;
		int j=0,i=0;
		set<char> *token = new set<char> [L];
		int flag=0;
		while(s[i]!='\0'){
			if(s[i]== '('){
				flag=1;
			}else{
				if(s[i]==')'){
					flag=0;
					j++;
				}else{
					token[j].insert(s[i]);
					if(flag==0){						
						j++;
					}
				}
			}
			i++;
		}

		int level = 0;
		int count = 0;	

		process(root, level, count, token);

//		cout<<"Case #"<<index+1<<": "<<count<<endl;
		fout<<"Case #"<<index+1<<": "<<count<<endl;
	}

	fin.close();
	fout.close();
//	cin>>N;
}

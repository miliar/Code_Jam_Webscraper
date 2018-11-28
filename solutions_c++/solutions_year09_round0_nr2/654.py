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

int T,H,W;

class TREE{
public:
	TREE():parent(NULL),altitude(),label(),ip(),childno(0),printed(false){
		typedef TREE *tptr;
		child = new tptr [4];
		for(int i=0;i<4;i++){
			child[i]=NULL;
		}
	}
	TREE *parent;
	TREE **child;
	int altitude;
	bool printed;
	char label;
	ipair ip;
	int childno;
}**tree;

typedef TREE *treeptr;

inline bool in(int i,int j){
	return i>=0 && i<H && j>=0 && j<W;
}

pair<int,int> flow(int i,int j){
	int low=tree[i][j].altitude;
//N
	if(in(i-1,j)) low= MIN(low, tree[i-1][j].altitude);
//W
	if(in(i,j-1)) low= MIN(low, tree[i][j-1].altitude);
//E 
	if(in(i,j+1)) low= MIN(low, tree[i][j+1].altitude);
//S
	if(in(i+1,j)) low= MIN(low, tree[i+1][j].altitude);

	if(low == tree[i][j].altitude) return MP(-1,-1);
	if(in(i-1,j) && low == tree[i-1][j].altitude) return MP(i-1,j);
	if(in(i,j-1) && low == tree[i][j-1].altitude) return MP(i,j-1);
	if(in(i,j+1) && low == tree[i][j+1].altitude) return MP(i,j+1);
	if(in(i+1,j) && low == tree[i+1][j].altitude) return MP(i+1,j);
}

void traverse(TREE *root, char c){
	root->label = c;
	root->printed = true;

	for(int i=0;i<root->childno;i++){
		traverse(root->child[i],c);
	}
}

void printtree(TREE &node,char c){
	TREE *p = &node;
	while(p->parent != NULL){
		p = p->parent;
	}
	traverse(p, c);
}


int main(){
	fin.open("B-large.in");
//	fout.open("small-result.txt");
	fout.open("large-result.txt");

	tree = new treeptr[100];
	Rep(i,100){
		tree[i]=new TREE [100];
	}

	fin>>T;
	Rep(index,T){
		fin>>H>>W;
		Rep(i,H){
			Rep(j,W){
				tree[i][j].childno=0;
				tree[i][j].child= new treeptr [4];
				tree[i][j].label='a';
				tree[i][j].parent=NULL;
				tree[i][j].printed=false;
				fin>>tree[i][j].altitude;
				tree[i][j].ip=MP(i,j);
			}
		}

		ipair ip;
		Rep(i,H){
			Rep(j,W){
				ip=flow(i,j);
				if(ip != MP(-1,-1)){
					int newi,newj;
					newi=ip.first;newj=ip.second;
					tree[i][j].parent=&(tree[newi][newj]);
					int num= tree[newi][newj].childno;
					tree[newi][newj].child[num]=&(tree[i][j]);
					(tree[newi][newj]).childno++;
				}
			}
		}

//		cout<<"Case #"<<index+1<<":"<<endl;
		fout<<"Case #"<<index+1<<": "<<endl;
		char c = 'a';
		Rep(i,H){
			Rep(j,W){
				if(tree[i][j].printed==0){
					printtree(tree[i][j],c);
					c++;
				}
//				cout<<tree[i][j].label<<" ";
				fout<<tree[i][j].label<<" ";
			}
			cout<<endl;
			fout<<endl;
		}	
	}
	fin.close();
	fout.close();
//	cin>>T;
}

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <list>
#include <bitset>
#include <cstring>
#include <unistd.h>
#include <stack>
#include <cmath>
#include <map>
#include <streambuf>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <queue>
#include <sys/time.h>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long int uint64;
typedef long long int int64;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define FOR(x,a,e) for(int x=a; x<=(e); ++x)
#define FORL(x,a,e) for(int x=a; x<(e); ++x)
#define FORD(x,a,e) for(int x=a; x>=(e); --x)
#define FORDG(x,a,e) for(int x=a; x>(e); --x)
#define REP(x,n) for(int x =0;x<(n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair

struct Node{

	string name;
	vector<Node *> nodes;

	Node() {};
};


int main(){

	int T;
	cin >> T;
	FOR(i, 1, T){
		cout<<"Case #" << i << ": ";

		int N, M;
		cin >> N >> M;
		//cout<<"N = " << N <<  " M = " << M << endl;
		string s;
		uint64 res  = 0;

		Node *root = new Node();
		Node *current = root;

		FORL(j, 0, N){
			cin >> s;
			//cout<<"E : " << s << endl;
			current = root;

			int pfp = 0;
			int fp  = s.find("/", pfp+1);
			int level = 0;
			while( fp != string::npos){
				string part = s.substr(pfp+1, fp-pfp-1);

				bool f = false;
				FOREACH(it, current->nodes){
					if ((*it)->name == part){
						f = true;
						current = *it;
						break;
					}
				}
				if (!f){
					Node *n =  new Node();
					n->name = part;
					(current->nodes).PB(n);
					current = n;
				}

				//cout<<"Part = " << part << endl;
				pfp = fp;
				fp  = s.find("/", pfp+1);
			}

			string part = s.substr(pfp+1, SIZE(s)-pfp-1);
			//cout<<"Part = " << part << endl;
			//current = root;
			bool f = false;
			FOREACH(it, current->nodes){
				if ((*it)->name == part){
					f = true;
					current = *it;
					break;
				}
			}
			if (!f){
				Node *n =  new Node();
				n->name = part;
				(current->nodes).PB(n);
				current = n;
			}

		}

		FORL(j, 0, M){
			cin >> s;
			//cout<<"N : " << s << endl;

			int pfp = 0;
			int fp  = s.find("/", pfp+1);

			current = root;

			while( fp != string::npos){
				string part = s.substr(pfp+1, fp-pfp-1);
				//cout<<"Part = " << part << endl;

				bool f = false;
				FOREACH(it, current->nodes){
					if ((*it)->name == part){
						f = true;
						current = *it;
						break;
					}
				}
				if (!f){
					//cout<<"Not found\n";
					++res;
					Node *n =  new Node();
					n->name = part;
					(current->nodes).PB(n);
					current = n;
				}
				//cout<<"CN = " << current->name << endl;

				pfp = fp;
				fp  = s.find("/", pfp+1);
			}
			string part = s.substr(pfp+1, SIZE(s)-pfp-1);
			//cout<<"Parta = " << part << endl;


			bool f = false;

			FOREACH(it, current->nodes){
				if ((*it)->name == part){
					f = true;
					current = *it;
					break;
				}
			}
			if (!f){
				//cout<<"Not found\n";
				++res;
				Node *n =  new Node();
				n->name = part;
				(current->nodes).PB(n);
				current = n;
			}
			//cout<<"Part = " << part << endl;
		}

		cout<<res<<endl;
	}
	return 0;
}

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define forint(i, a, b) for (int i=(int)(a); i<(int)(b); i++)

#define v1i vector< int >
#define v2i vector< vector< int > >
#define v3i vector< vector< vector< int > > >

#define v1d vector< double >
#define v2d vector< vector< double > >
#define v3d vector< vector< vector< double > > >

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int getint() {
	string str;
	getline(cin, str);
	return atoi(str.c_str());
}

int main() {

	int N = getint();

	forint(i, 0, N) {

		cout << "Case #" << (i+1) << ": ";

		map<string, int> names;
		names.clear();

		int S = getint();			
		forint(j,0,S) {
			string str;
			getline(cin, str);
			names[str]=j;			
		}

		int Q = getint(); 		

		if (Q==0) {
			cout << "0" << endl;
		}
		else {			
			vector<int> ids(Q);
			forint(j,0,Q) {
				string str;
				getline(cin, str);
				ids[j]=names[str];
			}

			vector< vector<int> > *table = new vector< vector<int> >(Q, vector<int>(S));

			forint(j,0,S) (*table)[Q-1][j] = 0;
			
			(*table)[Q-1][ids[Q-1]] = Q+1; // large number

			for(int q=Q-2; q>=0; q--) {
				forint(j,0,S) {
					if (j==ids[q]) (*table)[q][j]= Q+1;
					else {
						int qq=q+1;
						while (qq<Q && ids[qq]!=j) qq++;
						if (qq==Q) (*table)[q][j]= 0;
						else {
							(*table)[q][j]= *min_element((*table)[qq].begin(),(*table)[qq].end()) + 1;
						}
					}
				}
			}

			cout << *min_element((*table)[0].begin(),(*table)[0].end()) << endl;

			delete table;
		}
	}
}

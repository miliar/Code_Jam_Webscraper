/* kanekoA.cc
 */
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string engine[100];
string query[1000];
size_t next[100];
int main()
{
    int T, S, Q;
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> S;
	getline(cin, engine[0]); // skip \n after S
	for (int i=0; i<S; ++i) getline(cin, engine[i]);
	cin >> Q;	
	getline(cin, query[0]); // skip \n after Q
	for (int i=0; i<Q; ++i) getline(cin, query[i]);

	for (int i=0; i<S; ++i)
	    next[i] = find(query, query+Q, engine[i]) - query;
	
	int next_switch = *max_element(next, next+S), count=0;
	int cur = find(next, next+S, next_switch) - next;
	for (; next_switch < Q; ++count) {
	    for (int i=0; i<S; ++i) {
		next[i] = find(query+next_switch, query+Q, engine[i]) - query;
		// cerr << " " << next_switch << engine[i] << " " << next[i] << endl;
	    }
	    next_switch = *max_element(next, next+S);
	    cur = find(next, next+S, next_switch) - next;
	}
	cout << "Case #" << t+1 << ": " << count << endl;
    }
}

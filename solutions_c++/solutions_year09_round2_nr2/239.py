#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <list>

#include <algorithm>
#include <iterator>
#include <numeric>
#include <utility>	// make_pair(a,b)
#include <limits>


using namespace std;

string solve() {
    string s;
    cin>>s;
    if (next_permutation(s.begin(), s.end()))
	return s;
    else {
	reverse(s.begin(), s.end());
	s = "0"+s;
	next_permutation(s.begin(), s.end());
	return s;
    }
}


int main() {
    int NN;
    cin>>NN;  cin.ignore(99, '\n');
    for (int nn=1; nn<=NN; nn++)
	cout<<"Case #"<<nn<<": "<<solve()<<endl;
    return 0;
}

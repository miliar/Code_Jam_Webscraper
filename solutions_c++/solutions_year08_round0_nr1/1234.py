#include <iostream>
#include <vector>
#include <string>
#include <numeric>


using namespace std;


string read_string() {
    string s;
    getline(cin, s);
    return s;
}
int mymin(int a, int b) { return min(a,b);}

int solve() {
    int ns, nq;
    vector<string> vs, vq;

    cin>>ns;  cin.ignore(99, '\n');
    for (int s=0; s<ns; s++)
	vs.push_back( read_string() );

    cin>>nq;  cin.ignore(99, '\n');
    for (int q=0; q<nq; q++)
	vq.push_back( read_string() );
    if (nq==0)  return 0;

    vector<int> t(ns), t_(ns);
    for (int s=0; s<ns; s++)
	if (vs[s]==vq[0])
	    t[s] = nq;

    for (int q=1; q<nq; q++) {
	swap(t, t_);
	for (int s=0; s<ns; s++)
	    if (vs[s]==vq[q])
		t[s] = nq;
	    else {
		t[s] = 1 + accumulate(t_.begin(), t_.end(), nq, mymin);
		t[s] = min( t[s], t_[s] );
	    }
// 	copy(t.begin(), t.end(), ostream_iterator<int>(cerr, " "));
// 	cerr<<endl;
    }
    return accumulate(t.begin(), t.end(), nq, mymin);
}


int main() {
    int n;
    cin>>n;  cin.ignore(99, '\n');
    for (int c=1; c<=n; c++)
	cout<<"Case #"<<c<<": "<<solve()<<endl;
    return 0;
}

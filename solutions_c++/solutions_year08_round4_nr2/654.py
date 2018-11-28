#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>


using namespace std;


int N, M, A;
string solve() {
    cin>>N>>M>>A;
    vector<bool> v(N*M+1);
    vector<int> x(N*M+1);
    vector<int> y(N*M+1);
    for (int i=0; i<=N; i++)
	for (int j=0; j<=M; j++) {
	    v[i*j] = true;
	    x[i*j] = i;
	    y[i*j] = j;
	}
    for (int i=0; i<=N*M-A; i++)
	if (v[i] && v[i+A]) {
	    stringstream s;
	    s<<"0 0 "<<x[i]<<' '<<y[i+A]<<' '<<x[i+A]<<' '<<y[i];
	    return s.str();
	}
    return "IMPOSSIBLE";
}


int main() {
    int NN;
    cin>>NN;  cin.ignore(99, '\n');
    for (int c=1; c<=NN; c++)
	cout<<"Case #"<<c<<": "<<solve()<<endl;
    return 0;
}

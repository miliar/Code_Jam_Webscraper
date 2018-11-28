#include <iostream>
#include <vector>
#include <string>
#include <numeric>


using namespace std;



long solve() {
    int d;
    cin>>d;
    vector<int> v, w;
    for (int i=0; i<d; i++) {
	int t;
	cin>>t;
	v.push_back(t);
    }
    for (int i=0; i<d; i++) {
	int t;
	cin>>t;
	w.push_back(t);
    }
    sort(v.begin(), v.end());
    sort(w.begin(), w.end());
    long ret = 0;
    for (int i=0; i<d; i++)
	ret+=v[i]*w[d-i-1];
    return ret;
}


int main() {
    int n;
    cin>>n;  cin.ignore(99, '\n');
    for (int c=1; c<=n; c++)
	cout<<"Case #"<<c<<": "<<solve()<<endl;
    return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>



using namespace std;



string solve() {
    int N,M;
    cin>>N>>M;
    vector<int> batch(N+1);
    vector<int> like_malt(M);
    vector<vector<int> > no_malt(M);
    
    for (int i=0; i<M; i++) {
	int nn;
	cin>>nn;
	for (int j=0; j<nn; j++) {
	    int a,b;
	    cin>>a>>b;
	    if (b)  like_malt[i] = a;
	    else no_malt[i].push_back(a);
	}
    }

    while(true) {
	vector<int> need_malt;
	for (int i=0; i<M; i++) {
	    if (like_malt[i] && batch[like_malt[i]])
		continue;
	    bool personally_happy = false;
	    for (int j=0; j<no_malt[i].size(); j++)
		if (batch[no_malt[i][j]]==0) 
		    personally_happy = true;
	    if (!personally_happy)
		if (like_malt[i])
		    need_malt.push_back(like_malt[i]);
		else
		    return "IMPOSSIBLE";
	}
	if (need_malt.empty())
	    break;
	for (int i=0; i<need_malt.size(); i++)
	    batch[need_malt[i]] = 1;
    }
    
    ostringstream os;
    copy(batch.begin()+1, batch.end(), ostream_iterator<int>(os, " "));
    return os.str();
}


int main() {
    int n;
    cin>>n;  cin.ignore(99, '\n');
    for (int c=1; c<=n; c++)
	cout<<"Case #"<<c<<": "<<solve()<<endl;
    return 0;
}

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
    int N;
    pair<int, int> I[1000];
    int ord[1000];
    cin>>N;
    for(int i=0; i<N; i++)
        cin>>I[i].first;
    for(int i=0; i<N; i++){
        int p;
        cin>>p;
        I[i].second=p;
        ord[i]=i;
    }
    for(int it=0; it<N; it++)
        for(int i=0; i<N-1; i++){
            int j=i+1;
            int ex1=I[i].first*I[i].second+(100-I[i].second)*I[j].second*(I[i].first+I[j].first);
            int ex2=I[j].first*I[j].second+(100-I[j].second)*I[i].second*(I[i].first+I[j].first);
            if(ex2<ex1){
                swap(I[i], I[j]);
                swap(ord[i], ord[j]);
            }
        }
    for(int i=0; i<N; i++)
        cout<<ord[i]<<" ";
    cout<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}

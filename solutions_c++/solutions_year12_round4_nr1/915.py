#include <iostream>
#include <string>
#include <deque>

using namespace std;

pair<int,int> vines [20000];

#define mp make_pair

string solve(){
	int n,D;
	cin>>n;
	for( int i = 0; i < n; i++ ){
		cin>>vines[i].first>>vines[i].second;
	}
	cin>>D;
	deque<pair<int,int>> vineI;
	vineI.push_back( mp(vines[0].first, min(vines[0].first, vines[0].second)) );
	vines[n].first = D;
	vines[n].second = 0;
	n++;
	for( int i = 1; i < n; i++ ){
		while( !vineI.empty() && vineI.front().first+vineI.front().second < vines[i].first ) vineI.pop_front();
		if( vineI.empty() ){
			return "NO";
		}
		else{
			vineI.push_back( mp( vines[i].first, min(vines[i].second, vines[i].first - vineI.front().first ) ) );
		}
	}
	return "YES";
}

int main(){
	freopen("A-small.in", "r", stdin);	freopen("A-small.out", "w", stdout);
	int T;
	cin>>T;
	for( int i = 0 ; i < T; i++ ){
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
}
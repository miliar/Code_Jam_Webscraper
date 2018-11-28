#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

vector<string> eng;
vector<string> q;

bool Read(){
	eng.clear();
	q.clear();
	int n;
	char buf[500];
	scanf("%d ", &n );
	for(int i = 0; i < n; ++i){
		gets(buf);
		eng.push_back( buf );
	}
	scanf("%d ", &n);
	for(int i = 0; i < n; ++i){
		gets(buf);
		q.push_back( buf );
	}
	return true;
}

int Solve(){
	vector<int> ms;
	ms.assign( q.size(), 0 );
	for(int i = 0; i < eng.size(); ++i){
		int count = 0;
		for(int j = q.size() - 1; j >= 0; --j){
			if( q[j] == eng[i] ){
				count = 0;
			}else{
				count++;
				ms[j] = max( ms[j], count );
			}
		}
	}
	int res = 0;
	int cur = 0;
	while( cur < ms.size() ){
		cur += ms[cur];
		res++;
	}
	if( res == 0 ) return 0;
	return res - 1;
}

void Write(int k, int ans ){
	printf("Case #%d: %d\n", k, ans );
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	scanf("%d", &n );
	for(int i = 0; i < n; ++i){
		Read();
		Write(i + 1, Solve());
	}
	return 0;
}
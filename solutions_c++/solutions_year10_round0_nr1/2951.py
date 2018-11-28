#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int T;
unsigned int N,K;

string solve(){
	cin >> N >> K;
	unsigned int must = (1<<N) - 1;

	if((must&K) == must) return "ON";
	return "OFF";
}

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	cin >> T;
	for(int i = 1;i<=T;i++){
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}

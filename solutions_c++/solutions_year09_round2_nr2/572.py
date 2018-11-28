#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <list>
#include <queue>
//#include <fstream>

using namespace std;

void solve()
{
	string buffer;
	getline(cin, buffer);
	buffer = "0" + buffer;
	//cout << buffer;
	next_permutation( buffer.begin(), buffer.end() );
	if( buffer[0] == '0' ) cout << buffer.substr(1);
	else cout << buffer;
}

int main()
{
    int N;
    string Buffer;
    getline(cin, Buffer);
    N = atoi(Buffer.c_str());
    for(int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

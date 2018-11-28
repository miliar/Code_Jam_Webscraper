#include <iostream>
#include <cstdio>
using namespace std;

char table[26] = {
    'y', 'h', 'e', 's', 'o', 
    'c', 'v', 'x', 'd', 'u', 
    'i', 'g', 'l', 'b', 'k', 
    'r', 'z', 't', 'n', 'w', 
    'j', 'p', 'f', 'm', 'a', 
    'q'
};

int main(int argc, char *argv[])
{
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cin.get();
    for(int t = 0; t < T; t++)
    {
	string line;
	getline(cin, line);
	int n = line.length();
	for(int i = 0; i < n; i++)
	{
	    if(line[i] >= 'a' && line[i] <= 'z')
		line[i] = table[line[i]-'a'];
	}
	cout << "Case #" << t+1 << ": " << line;
	cout << endl;
    }

    return 0;
}

//#define trivia
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <bitset>
#define ken(i, a, b) for(int i = int(a); i < int(b); i++)
#define tehe(i, a, b) for(int i = int(a); i > int(b); i--)
using namespace std;

int n;
int inputan[1010];
int r;
int total;
int lowest;

int main()
{
	#ifndef trivia
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        cin >> n;
        for (int j = 0; j < n; j++) {
            cin >> inputan[j];
        }
        r = inputan[0];
        lowest = inputan[0];
        total = inputan[0];
        for (int j = 1; j < n; j++){
            r ^= inputan[j];
            total += inputan[j];
            if (lowest > inputan[j])
                lowest = inputan[j];
        }
        cout << "Case #" << i+1 << ": ";
        if (r != 0)
            cout << "NO\n";
        else
            cout << (total - lowest) << endl;
    }

	#ifndef trivia
	fclose(stdout);
	system("output.txt");
	#endif
	return 0;
}

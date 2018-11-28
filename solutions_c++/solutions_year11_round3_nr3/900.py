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

int n, l, h;
int freq[105];

bool appr(int a, int b) {
    if ((a % b == 0) || (b % a == 0))
        return true;
    return false;
}

int processB() {
    bool stillAppr;
    for (int i = l; i <= h; i++) {
        stillAppr = true;
        for (int j = 0; j < n; j++) {
            if (!appr(i, freq[j])) {
                stillAppr = false;
                break;
            }
        }
        if (stillAppr)
            return i;
    }
    return -1;
}

int main()
{
	#ifndef trivia
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        cin >> n >> l >> h;
        for (int j = 0; j < n; j++)
            cin >> freq[j];
        int r = processB();
        cout << "Case #" << (i+1) << ": ";
        if (r == -1) {
            cout << "NO\n";
        }
        else
            cout << r << endl;
    }

	#ifndef trivia
	fclose(stdout);
	system("output.txt");
	#endif
	return 0;
}


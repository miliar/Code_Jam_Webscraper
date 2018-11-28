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

char kamus[30][30];
char bomber[30][30];
int ada[30];
int c, d, n;

stack<char> invokespell;
stack<char> jawaban;

void clearinvoke()
{
    for (int i = 0; i < 30; i++)
        ada[i] = 0;
    while(!invokespell.empty())
        invokespell.pop();
}

void initial()
{
    for (int i = 0; i < 30; i++)
        for (int j = 0; j < 30; j++) {
            kamus[i][j] = '-';
            bomber[i][j] = '-';
        }
    clearinvoke();
}

void carisolusilagi(string inp)
{
    char one, two;
    bool bomb;
    for(int i = 0; i < inp.size(); i++) {
        if (invokespell.empty()) {
            invokespell.push(inp[i]);
            ada[inp[i]-'A'] = 1;
        }
        else {
            one = invokespell.top();
            two = inp[i];
            bomb = false;
            while((kamus[one-'A'][two-'A'] != '-') && !invokespell.empty()){
                ada[invokespell.top()-'A']--;
                invokespell.pop();
                two = kamus[one-'A'][two-'A'];
                if (invokespell.empty())
                    one = '-';
                else
                    one = invokespell.top();
            }
            for(int i = 0; i < 30; i++)
                if ((ada[i] > 0) && (bomber[i][two-'A'] == '*'))
                    bomb = true;
            if (bomb) {
                clearinvoke();
            }
            else {
                invokespell.push(two);
                ada[two-'A']++;
            }
        }
    }
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
        initial();
        cin >> c;
        string tmp;
        for (int j = 0; j < c; j++) {
            cin >> tmp;
            kamus[tmp[0]-'A'][tmp[1]-'A'] = tmp[2];
            kamus[tmp[1]-'A'][tmp[0]-'A'] = tmp[2];
        }
        cin >> d;
        for (int j = 0; j < d; j++) {
            cin >> tmp;
            bomber[tmp[0]-'A'][tmp[1]-'A'] = '*';
            bomber[tmp[1]-'A'][tmp[0]-'A'] = '*';
        }
        cin >> n;
        cin >> tmp;
        carisolusilagi(tmp);
        while(!invokespell.empty()) {
            jawaban.push(invokespell.top());
            invokespell.pop();
        }
        cout << "Case #" << i+1 << ": [";
        while (!jawaban.empty()) {
            cout << jawaban.top();
            jawaban.pop();
            if (jawaban.empty())
                break;
            cout << ", ";
        }
        cout << "]" << endl;
    }

	#ifndef trivia
	fclose(stdout);
	system("output.txt");
	#endif
	return 0;
}

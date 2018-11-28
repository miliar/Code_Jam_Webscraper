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

int posisiO, posisiB;
queue<char> urutanRobot;
queue<int> urutanRobotO;
queue<int> urutanRobotB;
int n;
int solusi;

void carisolusi()
{
    int tmpO, tmpB;
    while (!urutanRobot.empty()) {
        tmpO = abs(urutanRobotO.front() - posisiO);
        tmpB = abs(urutanRobotB.front() - posisiB);
        if (urutanRobot.front() == 'O') {
            tmpO++;
            solusi += tmpO;
            posisiO = urutanRobotO.front();
            if (tmpB >= tmpO)
                if (urutanRobotB.front() > posisiB)
                    posisiB += tmpO;
                else
                    posisiB -= tmpO;
            else
                posisiB = urutanRobotB.front();
            urutanRobotO.pop();
        }
        else {
            tmpB++;
            solusi += tmpB;
            posisiB = urutanRobotB.front();
            if (tmpO >= tmpB)
                if (urutanRobotO.front() > posisiO)
                    posisiO += tmpB;
                else
                    posisiO -= tmpB;
            else
                posisiO = urutanRobotO.front();
            urutanRobotB.pop();
        }
        urutanRobot.pop();
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
    for (int i = 0; i < tc; i++)
    {
        cin >> n;
        solusi = 0;
        posisiO = 1;
        posisiB = 1;
        char tmpchar;
        int tmpint;
        for (int j = 0; j < n; j++) {
            scanf(" %c", &tmpchar);
            cin >> tmpint;
            urutanRobot.push(tmpchar);
            if(tmpchar == 'O')
                urutanRobotO.push(tmpint);
            else
                urutanRobotB.push(tmpint);
        }
        carisolusi();
        cout << "Case #" << i+1 << ": " << solusi << endl;
    }

	#ifndef trivia
	fclose(stdout);
	system("output.txt");
	#endif
	return 0;
}

#include <iostream>
#include <fstream>
using namespace std;

void rotate(char tab[][100], int n) {
    char temp[100][100];
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            temp[n-1-y][x] = tab[x][y];
        }
    }
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            tab[x][y] = temp[x][y];
        }
    }
}

void gravity(char tab[][100], int n) {
    int temp[100][100] = {0};
    for (int x = 0; x < n; x++) {
        int y = n-1;
        int cnt = 0;
        while (y >= 0) {
            temp[x][y] = cnt;
            if (tab[x][y] == '.')
                cnt++;
            y--;
        }
    }
    for (int x = 0; x < n; x++) {
        for (int y = n-1; y >= 0; y--) {
            if (y+temp[x][y] > n-1) {
                continue;
            }
            tab[x][y+temp[x][y]] = tab[x][y];
        }
        for (int y = 0; y < temp[x][0]; y++) {
            tab[x][y] = '.';
        }
    }
}

void output(char tab[][100], int n) {
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cout << tab[x][y];
        }
        cout << endl;
    }
}

void flood(int x, int y, char key, char floodDirection, int a, int b, char tab[][100], int n, int& count) {
    if (x < 0 || x > n-1 || y < 0 || y > n-1)
        return;
    if (tab[x][y] != key)
        return;
    count++;
    if (floodDirection == 'h') {
        flood(x+a, y, key, floodDirection, a,b, tab, n, count);
    } else if (floodDirection == 'v') {
        flood(x, y+a, key, floodDirection, a,b, tab, n, count);
    } else {
        flood(x+a, y+b, key,floodDirection, a,b, tab, n, count);
    }
}

void checkScore(int k, char tab[][100], int n, bool &isWinBlue, bool &isWinRed) {
    isWinBlue = false;
    isWinRed = false;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            int count1 = 0, count2 = 0, count3a = 0, count3b = 0, count3c = 0, count3d = 0, count4 = 0, count5 = 0, count6a = 0,count6b = 0,count6c = 0,count6d = 0;
            if (tab[x][y] == 'B') {
                count1 = count2 = count3a = count3b =count3c =count3d =1;
                flood(x-1, y, 'B', 'h', -1, 0, tab, n, count1);
                flood(x+1, y, 'B', 'h', 1, 0,tab, n, count1);
                flood(x, y-1, 'B', 'v', -1,0, tab, n, count2);
                flood(x, y+1, 'B', 'v', 1, 0,tab, n, count2);
                flood(x+1, y+1, 'B', 'd', 1, 1,tab, n, count3a);
                flood(x-1, y-1, 'B', 'd', -1, -1,tab, n, count3b);
                flood(x-1, y+1, 'B', 'd', -1, 1,tab, n, count3c);
                flood(x+1, y-1, 'B', 'd', 1, -1,tab, n, count3d);
            }
            if (tab[x][y] == 'R') {
                count4 = count5 = count6a = count6b = count6c = count6d = 1;
                flood(x-1, y, 'R', 'h', -1,0, tab, n, count4);
                flood(x+1, y, 'R', 'h', 1, 0,tab, n, count4);
                flood(x, y-1, 'R', 'v', -1,0, tab, n, count5);
                flood(x, y+1, 'R', 'v', 1, 0,tab, n, count5);
                flood(x+1, y+1, 'R', 'd', 1, 1,tab, n, count6a);
                flood(x-1, y-1, 'R', 'd', -1, -1,tab, n, count6b);
                flood(x-1, y+1, 'R', 'd', -1, 1,tab, n, count6c);
                flood(x+1, y-1, 'R', 'd', 1, -1,tab, n, count6d);
            }
            if (count1 >= k || count2 >= k || count3a >= k || count3b >= k || count3c >= k || count3d >= k)
                isWinBlue = true;
            if (count4 >= k || count5 >= k || count6a >= k|| count6b >= k|| count6c >= k|| count6d >= k)
                isWinRed = true;
        }
    }
}

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T, n, k; 
    char tab[100][100];
    cin >> T;
    for (int j = 0; j < T; j++) {
        cout << "Case #" << j+1 << ": ";
        cin >> n >> k;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                cin >> tab[x][y];
            }
        }
        
        bool isWinBlue, isWinRed;
        /*checkScore(k, tab, n, isWinBlue, isWinRed);
        if (isWinBlue || isWinRed) {
            cout << "Error!\n";
            return 0;
        }*/

        //output(tab, n);
        rotate(tab, n);
        //cout << endl << endl;
        //output(tab, n);
        //cout << endl<< endl;
        gravity(tab, n);
        //output(tab, n);
        /*rotate(tab, n);
        gravity(tab, n);*/

        checkScore(k, tab, n, isWinBlue, isWinRed);
        if (isWinBlue && isWinRed) {
            cout << "Both\n";
        } else if (isWinBlue) {
            cout << "Blue\n";
        } else if (isWinRed) {
            cout << "Red\n";
        } else {
            cout << "Neither\n";
        }
    }

}
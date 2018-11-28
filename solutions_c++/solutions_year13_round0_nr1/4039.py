#include <iostream>
#include <stdio.h>

using namespace std;

int A[5][5];

bool check(int id){
    bool answer = 0;
    // rows
    for(int i = 0; i < 4; i++)
    {
        int num = 0;
        for(int j = 0; j < 4; j++)
        {
            if(A[i][j] == id || A[i][j] == 3)
            {
                num++;
            }
        }
        if(num == 4){
            return true;
        }
    }
    //cols
    for(int i = 0; i < 4; i++)
    {
        int num = 0;
        for(int j = 0; j < 4; j++)
        {
            if(A[j][i] == id || A[j][i] == 3)
            {
                num++;
            }
        }
        if(num == 4){
            return true;
        }
    }
    //dig
    int num = 0;
    for(int i = 0; i < 4; i++)
    {
        if(A[i][i] == id || A[i][i] == 3)
        {
            num++;
        }
    }
    if(num == 4){
        return true;
    }

    num = 0;
    for(int i = 0; i < 4; i++)
    {
        if(A[i][3 - i] == id || A[i][3 - i] == 3)
        {
            num++;
        }
    }
    if(num == 4){
        return true;
    }

}



int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for(int i2 = 0; i2 < tests; i2++)
    {
       int num_points = 0;
       for(int i = 0; i < 4; i++)
       {
           for(int j = 0; j < 4; j++)
           {
               char x[3];
               scanf("%1s", x);
               if(x[0] == '.'){
                    A[i][j] = 0;
                    num_points++;
                }
                else if (x[0] == 'X'){
                    A[i][j] = 1;
                }
                else if (x[0] == 'O'){
                    A[i][j] = 2;
                }
                else if(x[0]== 'T'){
                    A[i][j] = 3;
                }
           }
       }

       cout << "Case #" << i2 + 1<<": ";
       if(check(1)){
            cout << "X won" << endl;
       }
       else if(check(2)){
        cout << "O won" << endl;
       }
       else if (num_points == 0) {
           cout << "Draw" << endl;
       } else {
            cout << "Game has not completed" << endl;
       }
    }
    return 0;
}

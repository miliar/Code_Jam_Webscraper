#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <fstream>
#include <math.h>
#include <cmath>
#include <vector>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <iomanip>
#include <deque>
#include <list>
#include <cctype>
#include <utility>

using namespace std;


const double PI = 2 * acos (0);

int main()
{
    //Tic-Tac-Toe-Tomek
/*
8

OOOT
....
XX..
....

O.XO
O.XO
T.TO
X.XX

XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
*/

    int T;
    cin>>T;

    string Xw="X won";
    string Ow="O won";
    string Dr="Draw";
    string In="Game has not completed";


    for(int i=1; i<=T; i++)
    {
        char A[5][5];
        for(int k=0; k<4; k++)
        {
            cin>>A[k];
        }
        string veredict="P";
        bool T=false;//si acabo o no

        while(1)
        {
            int t2=0, t3=0, t4=0;//para O
            int y2=0, y3=0, y4=0;//para y
            for(int k=0; k<4; k++)
            {
                int t=0, t1=0;
                int y=0, y1=0;

                for(int j=0; j<4; j++)
                {
                    if(A[k][j]=='O' || A[k][j]=='T') t++; //fila
                    if(A[j][k]=='O' || A[j][k]=='T') t1++;//columna
                    if(j==k)//diagonal derecha
                    {
                        if(A[j][k]=='O' || A[j][k]=='T') t2++;
                    }
                    if(j+k==3)//diagonal izquierda
                    {
                        if(A[j][k]=='O' || A[j][k]=='T') t3++;
                    }

                    if(A[k][j]=='X' || A[k][j]=='T') y++;//fila
                    if(A[j][k]=='X' || A[j][k]=='T') y1++;//columna
                    if(j==k)//diagonal derecha
                    {
                        if(A[j][k]=='X' || A[j][k]=='T') y2++;
                    }
                    if(j+k==3)//diagonal izquierda
                    {
                        if(A[j][k]=='X' || A[j][k]=='T') y3++;
                    }

                    if(A[j][k]=='.') t4++;
                }
                if(t==4 || t1==4)
                {
                    T=true;
                    veredict=Ow;
                    break;
                }
                if(y==4 || y1==4)
                {
                    T=true;
                    veredict=Xw;
                    break;
                }
            }
            if(t3==4 || t2==4)
            {
                T=true;
                veredict=Ow;
            }
            if(y2==4 || y3==4)
            {
                T=true;
                veredict=Xw;
            }
            if(T==false && t4==0 && veredict=="P")
            {
                veredict=Dr;
            }

            if(T==false && t4>0 && veredict=="P")
            {
                veredict=In;
            }
            break;
        }


        cout<<"Case #"<<i<<": "<<veredict<<endl;
    }

    return 0;
}

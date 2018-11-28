#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>

using namespace std;
int main()
{
    ifstream cin ("A-small-attempt1.in");
    ofstream cout ("prog1.out");
int t,i,j,counter=0;
cin>>t;
char arr1[4][4],arr2[4][4],arr3[4][4];
while(t--)
{
    char c='D';
    bool check1=0,check2=0,check3=0;
    counter++;
    for(i=0;i<4;i++)
    {
        check1=0;check2=0;
        for(j=0;j<4;j++)
        {
            cin>>arr1[i][j];
            if(arr1[i][j]=='.')check3=1;

            arr2[i][j]=arr1[i][j];
            if(arr2[i][j]=='T')arr2[i][j]='X';

            arr3[i][j]=arr1[i][j];
            if(arr3[i][j]=='T')arr3[i][j]='O';

            if(arr2[i][j]!='X')
            check1=1;
            if(arr3[i][j]!='O')
            check2=1;
        }
        if(!check1)c='X';
        else if(!check2)c='O';
    }
    for(i=0;i<4;i++)
    {
            check1=0;check2=0;
            for(j=0;j<4;j++)
            {
                if(arr2[j][i]!='X')
                check1=1;
                if(arr3[j][i]!='O')
                check2=1;
            }
            if(!check1)c='X';
            else if(!check2)c='O';
    }
    if(arr2[0][0]==arr2[1][1]==arr2[2][2]==arr2[3][3]=='X')c='X';
    else if(arr3[0][0]=='O'&&arr3[1][1]=='O'&&arr3[2][2]=='O'&&arr3[3][3]=='O')c='O';
    if(arr2[0][3]==arr2[1][2]==arr2[2][1]==arr2[3][0]=='X')c='X';
    else if(arr3[0][3]=='O'&&arr3[1][2]=='O'&&arr3[2][1]=='O'&&arr3[3][0]=='O')c='O';
    cout<<"Case #"<<counter<<": ";
    if(c=='D'&&check3)c='A';
    if(c=='X')
    cout<<"X won\n";
    else if(c=='D')
    cout<<"Draw\n";
    else if(c=='O')
    cout<<"O won\n";
    else if(c=='A')
    cout<<"Game has not completed\n";
}

return 0;
}

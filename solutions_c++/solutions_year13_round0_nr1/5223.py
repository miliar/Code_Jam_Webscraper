#include<iostream>
#include<string.h>
#include<fstream>

using namespace std;

int result(string a1, string a2, string a3, string a4);

int main(){
    
    ifstream input("A-large.in");
    ofstream output("output.txt");
    int N;
    input>>N;
    string a[4*N];
    int i,j;
    
    
    for(i=0;i<(4*N);i++)
    {
                        input>>a[i];
                        }
    for(i=0;i<4*N;i+=4)
    {
                        j=result(a[i],a[i+1],a[i+2],a[i+3]);
                        switch(j)
                        {
                               case 0:
                                    output<<"Case #"<<i/4+1<<": X won"<<endl;
                                    break;
                                    
                               case 1:
                                    output<<"Case #"<<i/4+1<<": O won"<<endl;
                                    break;
                                    
                               case 2:
                                    output<<"Case #"<<i/4+1<<": Draw"<<endl;
                                    break;
                               
                               case 3:
                                    output<<"Case #"<<i/4+1<<": Game has not completed"<<endl;
                                    break;
                               }
                        }
    return 0;
    }

int result(string a1, string a2, string a3, string a4)
{
    string a[4];
    
    a[0]=a1;
    a[1]=a2;
    a[2]=a3;
    a[3]=a4;
    
    int i,j;
    
    
    for(i=0;i<4;i++)
    if((a[i][0]=='X' || a[i][0]=='T') && (a[i][1]=='X' || a[i][1]=='T') && (a[i][2]=='X' || a[i][2]=='T') && (a[i][3]=='X' || a[i][3]=='T'))
    return 0;
    for(j=0;j<4;j++)
    if((a[0][j]=='X' || a[0][j]=='T') && (a[1][j]=='X' || a[1][j]=='T') && (a[2][j]=='X' || a[2][j]=='T') && (a[3][j]=='X' || a[3][j]=='T'))
    return 0;
    if((a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T'))
    return 0;
    if((a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X' || a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X' || a[3][0]=='T'))
    return 0;
    
    for(i=0;i<4;i++)
    if((a[i][0]=='O' || a[i][0]=='T') && (a[i][1]=='O' || a[i][1]=='T') && (a[i][2]=='O' || a[i][2]=='T') && (a[i][3]=='O' || a[i][3]=='T'))
    return 1;
    for(j=0;j<4;j++)
    if((a[0][j]=='O' || a[0][j]=='T') && (a[1][j]=='O' || a[1][j]=='T') && (a[2][j]=='O' || a[2][j]=='T') && (a[3][j]=='O' || a[3][j]=='T'))
    return 1;
    if((a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T'))
    return 1;
    if((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O' || a[3][0]=='T'))
    return 1;
    
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)
    if(a[i][j]=='.')
    return 3;
    
    return 2;
    }

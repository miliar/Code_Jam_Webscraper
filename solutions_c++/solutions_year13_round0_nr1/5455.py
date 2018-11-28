#include <fstream>
#include <string>
using namespace std;
ofstream cout("output.txt");
ifstream cin("A-small-attempt1.in");

long t;
char a[4][4];

int main()
{
    cin>>t;

    for (long i=0;i<t;i++){
        cin>>a[0][0]>>a[0][1]>>a[0][2]>>a[0][3]>>a[1][0]>>a[1][1]>>a[1][2]>>a[1][3]>>a[2][0]>>a[2][1]>>a[2][2]>>a[2][3]>>a[3][0]>>a[3][1]>>a[3][2]>>a[3][3];
    bool end=1;
    bool ctd=0;
    for (long j=0;j<4;j++)
    for (long k=0;k<4;k++)
    if (a[j][k]=='.')
        end=0;

    for (long j=0;j<4;j++){
    if (a[j][0]!='.'){
        if (a[j][0]=='T'){
            if (a[j][1]==a[j][2] && a[j][2]==a[j][3] && a[j][2]!='.')
                if (!ctd){
                cout<<a[j][2]<<" won\n";
                ctd=1;
                }
        }
        else
            if ((a[j][1]==a[j][0] || a[j][1]=='T') && (a[j][2]==a[j][0] || a[j][2]=='T') && (a[j][3]==a[j][0] || a[j][3]=='T'))
                if (!ctd){
                cout<<a[j][0]<<" won\n";
                ctd=1;}
        }
    }

    for (long j=0;j<4;j++)
    if (a[0][j]!='.'){
        if (a[0][j]=='T'){
            if (a[1][j]==a[2][j] && a[2][j]==a[3][j] && a[2][j]!='.')
                if (!ctd){
                cout<<a[2][j]<<" won\n";
                ctd=1;
                }
            }
        else
            if ((a[1][j]==a[0][j] || a[1][j]=='T') && (a[2][j]==a[0][j] || a[2][j]=='T') && (a[3][j]==a[0][j] || a[3][j]=='T'))
                if (!ctd){
                cout<<a[0][j]<<" won\n";
                ctd=1;}
    }


if (a[0][0]!='.'){
    if (a[0][0]=='T'){
        if (a[1][1]==a[2][2] && a[2][2]==a[3][3])
            if (!ctd){
                cout<<a[1][1]<<" won\n";
                ctd=1;
            }
    }
    else
    if ((a[1][1]==a[0][0] || a[1][1]=='T') && (a[2][2]==a[0][0] || a[2][2]=='T') && (a[3][3]==a[0][0] || a[3][3]=='T'))
        if (!ctd){
        cout<<a[0][0]<<" won\n";
        ctd=1;
        }
}

if (a[3][0]!='.'){
    if (a[3][0]=='T'){
        if (a[2][1]==a[1][2] && a[1][2]==a[0][3])
            if (!ctd){
                cout<<a[2][1]<<" won\n";
                ctd=1;
            }
    }
    else
    if ((a[2][1]==a[3][0] || a[2][1]=='T') && (a[1][2]==a[3][0] || a[1][2]=='T') && (a[0][3]==a[3][0] || a[0][3]=='T'))
        if (!ctd){
        cout<<a[0][3]<<" won\n";
        ctd=1;
        }
}
if (!ctd)
        end ? cout<<"Draw\n":cout<<"Game has not completed\n";
}


    return 0;
}

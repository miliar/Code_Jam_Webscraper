#include<iostream>
#include<cstring>
using namespace std;
char Matrix[27][2];
void createDic()
{
     Matrix[0][0]=' ';Matrix[0][0]=' ';
     Matrix[1][0]='a';Matrix[1][1]='y';
     Matrix[2][0]='b';Matrix[2][1]='h';
     Matrix[3][0]='c';Matrix[3][1]='e';
     Matrix[4][0]='d';Matrix[4][1]='s';
     Matrix[5][0]='e';Matrix[5][1]='o';
     Matrix[6][0]='f';Matrix[6][1]='c';
     Matrix[7][0]='g';Matrix[7][1]='v';
     Matrix[8][0]='h';Matrix[8][1]='x';
     Matrix[9][0]='i';Matrix[9][1]='d';
     Matrix[10][0]='j';Matrix[10][1]='u';
     Matrix[11][0]='k';Matrix[11][1]='i';
     Matrix[12][0]='l';Matrix[12][1]='g';
     Matrix[13][0]='m';Matrix[13][1]='l';
     Matrix[14][0]='n';Matrix[14][1]='b';
     Matrix[15][0]='o';Matrix[15][1]='k';
     Matrix[16][0]='p';Matrix[16][1]='r';
     Matrix[17][0]='q';Matrix[17][1]='z';
     Matrix[18][0]='r';Matrix[18][1]='t';
     Matrix[19][0]='s';Matrix[19][1]='n';
     Matrix[20][0]='t';Matrix[20][1]='w';
     Matrix[21][0]='u';Matrix[21][1]='j';
     Matrix[22][0]='v';Matrix[22][1]='p';
     Matrix[23][0]='w';Matrix[23][1]='f';
     Matrix[24][0]='x';Matrix[24][1]='m';
     Matrix[25][0]='y';Matrix[25][1]='a';
     Matrix[26][0]='z';Matrix[26][1]='q';
}
int main()
{
    int N;
    string In;
    char Temp[100];
    createDic();
    cin>>N;
    getline(cin,In);
    for(int i=1;i<=N;i++)
    {
            getline(cin,In);
            strcpy(Temp,In.data());
            cout<<"Case #"<<i<<": ";
            for(int j=0;j<In.length();j++)
            {
                    if(Temp[j]!=' ')
                    cout<<Matrix[Temp[j]-96][1];
                    else
                    cout<<" ";
            }
            cout<<endl;
    }
    return 0;
}

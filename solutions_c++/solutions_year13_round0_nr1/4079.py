#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int check(char p[][4],char s);
int main()
{
    ifstream input("input.txt");

    ofstream myfile;
    myfile.open ("outputttt.txt");
    //cout<<r<<endl<<k<<endl<<p<<endl<<l;

    int t;
    input>>t;

    int ppp=0;
    while(t--)
    {
        int flag=0;
        char a[4][4];
        for(int i=0;i<=3;i++)
        {
        for(int j=0;j<=3;j++)
        {
        input>>a[i][j];
        if(a[i][j]=='.')
        flag=1;
        }
        }
        if((check(a,'O'))==1)
        myfile<<"Case #"<<(++ppp)<<": "<<"O won"<<endl;
       else if((check(a,'X'))==1)
        myfile<<"Case #"<<(++ppp)<<": "<<"X won"<<endl;
       else if((flag==1))
        myfile<<"Case #"<<(++ppp)<<": "<<"Game has not completed"<<endl;
        else
        myfile<<"Case #"<<(++ppp)<<": "<<"Draw"<<endl;



    }

}

int check(char p[][4],char s)
{

    for(int i=0;i<=3;i++)
    {
        if((int(p[i][0])+int(p[i][1])+int(p[i][2])+int(p[i][3])==(3*int(s)+84))||(int(p[i][0])+int(p[i][1])+int(p[i][2])+int(p[i][3])==(4*int(s))))
        return 1;
        if((int(p[0][i])+int(p[1][i])+int(p[2][i])+int(p[3][i])==(3*int(s)+84))||(int(p[0][i])+int(p[1][i])+int(p[2][i])+int(p[3][i])==(4*int(s))))
        return 1;

    }
    if(((int)p[0][0]+(int)p[1][1]+(int)p[2][2]+(int)p[3][3]==(3*int(s)+84))||((int)p[0][0]+(int)p[1][1]+(int)p[2][2]+(int)p[3][3]==(4*int(s))))
    return 1;
    if(((int)p[3][0]+(int)p[2][1]+(int)p[1][2]+(int)p[0][3]==(3*int(s)+84))||((int)p[3][0]+(int)p[2][1]+(int)p[1][2]+(int)p[0][3]==(4*int(s))))
    return 1;
    else
    return 0;
}

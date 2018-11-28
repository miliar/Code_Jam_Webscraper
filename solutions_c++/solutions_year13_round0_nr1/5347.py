#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ifstream fin("abc.in");
ofstream fout("out.out");
int n,xhori[5][5],xvert[5][5]={0},xdiag[5][5]={0},xdiag2[5][5]={0},ohori[5][5]={0},overt[5][5]={0},odiag[5][5]={0},odiag2[5][5]={0},xwon,owon,u,v,dotcount=0;
char map[5][5],a[5];
fin>>n;
fin.getline(a,'\n');
for (int i=0;i<n;i++)
    {
    fin.getline(map[0],'\n');
    fin.getline(map[1],'\n');
    fin.getline(map[2],'\n');
    fin.getline(map[3],'\n');
    fin.getline(a,'\n');

    xwon=0; owon=0; dotcount=0;
    for(int x=0;x<4;x++)
        {
        for(int y=0;y<4;y++)
            {
            if(map[x][y]=='.')
                {
                dotcount++;
                if(x==0 && y==0)
                    {
                    xhori[x][y]=0; xvert[x][y]=0; xdiag[x][y]=0;
                    ohori[x][y]=0; overt[x][y]=0; odiag[x][y]=0;
                    }
                else if(x==0)
                    {
                    xhori[x][y]=0+xhori[x][y-1]; ohori[x][y]=0+ohori[x][y-1];
                    xvert[x][y]=0;overt[x][y]=0;
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(y==3) {xdiag2[x][3]=0; odiag2[x][3]=0;}
                    }
                else if(y==0)
                    {
                    xhori[x][y]=0;ohori[x][y]=0;
                    xvert[x][y]=0+xvert[x-1][y];overt[x][y]=0+overt[x-1][y];
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(x==3) {xdiag2[x][y]=0+xdiag2[x-1][y+1]; odiag2[x][y]=0+odiag2[x-1][y+1];}
                    }
                else
                    {
                    xhori[x][y]=0+xhori[x][y-1];ohori[x][y]=0+ohori[x][y-1];
                    xvert[x][y]=0+xvert[x-1][y];overt[x][y]=0+overt[x-1][y];
                    if(x==y) {xdiag[x][y] = 0 + xdiag[x-1][y-1]; odiag[x][y] = 0 + odiag[x-1][y-1];}
                    else {xdiag[x][y]=0;odiag[x][y]=0;}

                    if(x==(3-y)) {xdiag2[x][y] = 0 + xdiag2[x-1][y+1]; odiag2[x][y] = 0 + odiag2[x-1][y+1];}
                    else {xdiag2[x][y]=0; odiag2[x][y]=0;}
                    }
                }

            else if(map[x][y]=='X')
                {
                if(x==0 && y==0)
                    {
                    xhori[x][y]=1; xvert[x][y]=1; xdiag[x][y]=1;
                    ohori[x][y]=0; overt[x][y]=0; odiag[x][y]=0;
                    }
                else if(x==0)
                    {
                    xhori[x][y]=1+xhori[x][y-1]; ohori[x][y]=0+ohori[x][y-1];
                    xvert[x][y]=1;overt[x][y]=0;
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(y==3) {xdiag2[x][3]=1; odiag2[x][3]=0;}
                    }
                else if(y==0)
                    {
                    xhori[x][y]=1;ohori[x][y]=0;
                    xvert[x][y]=1+xvert[x-1][y];overt[x][y]=0+overt[x-1][y];
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(x==3) {xdiag2[x][y]=1+xdiag2[x-1][y+1]; odiag2[x][y]=0+odiag2[x-1][y+1];}
                    }
                else
                    {
                    xhori[x][y]=1+xhori[x][y-1]; ohori[x][y]=0+ohori[x][y-1];
                    xvert[x][y]=1+xvert[x-1][y];overt[x][y]=0+overt[x-1][y];
                    if(x==y) {xdiag[x][y] = 1 + xdiag[x-1][y-1]; odiag[x][y] = 0 + odiag[x-1][y-1];}
                    else {xdiag[x][y]=0;odiag[x][y]=0;}

                    if(x==(3-y)) {xdiag2[x][y] = 1 + xdiag2[x-1][y+1]; odiag2[x][y] = 0 + odiag2[x-1][y+1];}
                    else {xdiag2[x][y]=0; odiag2[x][y]=0;}
                    }
                }

            else if(map[x][y]=='O')
                {
                if(x==0 && y==0)
                    {
                    xhori[x][y]=0; xvert[x][y]=0; xdiag[x][y]=0;
                    ohori[x][y]=1; overt[x][y]=1; odiag[x][y]=1;
                    }
                else if(x==0)
                    {
                    xhori[x][y]=0+xhori[x][y-1]; ohori[x][y]=1+ohori[x][y-1];
                    xvert[x][y]=0;overt[x][y]=1;
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(y==3) {xdiag2[x][3]=0; odiag2[x][3]=1;}
                    }
                else if(y==0)
                    {
                    xhori[x][y]=0;ohori[x][y]=1;
                    xvert[x][y]=0+xvert[x-1][y];overt[x][y]=1+overt[x-1][y];
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(x==3) {xdiag2[x][y]=0+xdiag2[x-1][y+1]; odiag2[x][y]=1+odiag2[x-1][y+1];}
                    }
                else
                    {
                    xhori[x][y]=0+xhori[x][y-1]; ohori[x][y]=1+ohori[x][y-1];
                    xvert[x][y]=0+xvert[x-1][y];overt[x][y]=1+overt[x-1][y];
                    if(x==y) {xdiag[x][y] = 0 + xdiag[x-1][y-1]; odiag[x][y] = 1 + odiag[x-1][y-1];}
                    else {xdiag[x][y]=0;odiag[x][y]=0;}

                    if(x==(3-y)) {xdiag2[x][y] = 0 + xdiag2[x-1][y+1]; odiag2[x][y] = 1 + odiag2[x-1][y+1];}
                    else {xdiag2[x][y]=0; odiag2[x][y]=0;}
                    }
                }

            else if(map[x][y]=='T')
                {
                if(x==0 && y==0)
                    {
                    xhori[x][y]=1; xvert[x][y]=1; xdiag[x][y]=1;
                    ohori[x][y]=1; overt[x][y]=1; odiag[x][y]=1;
                    }
                else if(x==0)
                    {
                    xhori[x][y]=1+xhori[x][y-1]; ohori[x][y]=1+ohori[x][y-1];
                    xvert[x][y]=1;overt[x][y]=1;
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(y==3) {xdiag2[x][3]=1; odiag2[x][3]=1;}
                    }
                else if(y==0)
                    {
                    xhori[x][y]=1;ohori[x][y]=1;
                    xvert[x][y]=1+xvert[x-1][y];overt[x][y]=1+overt[x-1][y];
                    xdiag[x][y]=0;odiag[x][y]=0;
                    if(x==3) {xdiag2[x][y]=1+xdiag2[x-1][y+1]; odiag2[x][y]=1+odiag2[x-1][y+1];}
                    }
                else
                    {
                    xhori[x][y]=1+xhori[x][y-1]; ohori[x][y]=1+ohori[x][y];
                    xvert[x][y]=1+xvert[x-1][y];overt[x][y]=1+overt[x-1][y];
                    if(x==y) {xdiag[x][y] = 1 + xdiag[x-1][y-1]; odiag[x][y] = 1 + odiag[x-1][y-1];}
                    else {xdiag[x][y]=0;odiag[x][y]=0;}

                    if(x==(3-y)) {xdiag2[x][y] = 1 + xdiag2[x-1][y+1]; odiag2[x][y] = 1 + odiag2[x-1][y+1];}
                    else {xdiag2[x][y]=0; odiag2[x][y]=0;}
                    }
                }
            }
        }


    for (int z=0;z<4;z++)
        {
        if(xhori[z][3]==4 || xvert[3][z]==4) xwon=1;
        if(ohori[z][3]==4 || overt[3][z]==4) owon=1;
        }
        if(xdiag[3][3]==4) xwon=1;
        if(odiag[3][3]==4) owon=1;
        if(xdiag2[3][0]==4) xwon=1;
        if(odiag2[3][0]==4) owon=1;

    if(xwon==owon)
        {
        if(!dotcount) fout<<"Case #"<<i+1<<": Draw";
        else fout<<"Case #"<<i+1<<": Game has not completed";
        }
    else if (xwon) fout<<"Case #"<<i+1<<": X won";
    else if (owon) fout<<"Case #"<<i+1<<": O won";

    if(i!=n-1) fout<<endl;
/*
    for(u=0;u<4;u++)
        {
        for(v=0;v<4;v++)
            {
            cout<<odiag[u][v]<<" ";
            }
        cout<<endl;
        }
    cout<<endl;
*/
    }
return 0;
}

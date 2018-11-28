#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 1002
using namespace std;
typedef long  ll;
char a[6][6];
int Tx, Ty, empt;
void repp()
{
    int i,j;
	Tx = Ty=10;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            if(a[i][j]=='T')
            {
                Tx = i; Ty = j;
            }
            if(a[i][j]=='.') empt =1;
        }

}
bool Win(char x)
{
    int i,j,k,l;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[i][j]!=x) break;
        }
        if(j==4) return true;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[j][i]!=x) break;
        }
        if(j==4) return true;
    }
    for(i=0;i<4;i++)
        if(a[i][i]!=x) break;
    if(i==4) return true;
    for(i=0,j=3;i<4;j--,i++)
        if(a[i][j]!=x) break;
     if(i==4) return true;

    return false;

}
void check()
{
	repp();
	if(Tx*Ty!=100)
    a[Tx][Ty] = 'X';
    if(Win('X'))
    {
        puts("X won");
        return ;
    }
	if(Tx*Ty!=100)
	a[Tx][Ty] = 'O';
    if(Win('O'))
    {
        puts("O won");
        return ;
    }
    if(empt==0)
    {
        puts("Draw");
        return ;
    }
    puts("Game has not completed");
}
int main()
{
   // freopen("D:\\in.txt","r",stdin);
   // freopen("D:\\out.txt","w",stdout);
    int i,j,k=1,l;
    cin >> l;
    while(l--)
    {
        empt =0;
		printf("Case #%d: ",k++);
        gets(a[0]);
        for(i=0;i<4;i++) gets(a[i]);
        check();
    }

	return 0;
}

#include<stdio.h>
#include<string.h>
using namespace std;
char * buf[4];
bool check(char x)
{
    for (int i=0;i<4;i++)
    {
	bool ok= true;
	for (int j=0;j<4;j++)
	    if(buf[i][j]!=x && buf[i][j]!='T') {ok = false;break;}
	if(ok) return true;
    }
    for (int i=0;i<4;i++)
    {
	bool ok= true;
	for (int j=0;j<4;j++)
	    if(buf[j][i]!=x && buf[j][i]!='T') {ok = false;break;}
	if(ok) return true;
    }
    bool ok = true;
    for (int i=0;i<4;i++)
    {
	if(buf[i][i] != x && buf[i][i]!= 'T') { ok=false; break;}
    }
    if(ok) return true;
    ok=true;
    for (int i=0;i<4;i++)
    {
	if(buf[i][4-i-1] != x && buf[i][4-i-1]!= 'T') { ok=false; break;}
    }
    return ok;
}
int main()
{
    int zes;scanf("%d",&zes);
    for (int i=0;i<4;i++)
	buf[i]= new char [5];
    for (int z=0;z<zes;z++)
    {
	for (int  i=0;i<4;i++)
	{
	    buf[i]= new char [5];
	    scanf("%s",buf[i]);
	}
	if(check('X'))
	{
	    printf("Case #%d: X won\n",z+1);
	    continue;
	}
	if(check('O'))
	{
	    printf("Case #%d: O won\n",z+1);
	    continue;
	}
	int ile =0 ;
	for (int i=0;i<4;i++)for (int j=0;j<4;j++) ile+=buf[i][j]=='.';
	if(ile)
	{
   	    printf("Case #%d: Game has not completed\n",z+1);
	}
	else
	{
	    printf("Case #%d: Draw\n",z+1);
	}
    }
    for (int i=0;i<4;i++)
	 delete [] buf[i];
}


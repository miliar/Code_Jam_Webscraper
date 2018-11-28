#include<iostream>
#include<stack>
#include<map>
#include<utility>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<map>
#include<fstream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<cstring>
using namespace std;
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
int main()
{
    int t,c=0;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
	char a[4][4],temp;
	bool flag=0;
	for(int i=0;i<4;i++)
	{
	    for(int j=0;j<4;j++)
		cin>>a[i][j];
	}
	for(int i=0;i<4;i++)
	{
	    int o=0,x=0,r=0;
	    for(int j=0;j<4;j++)
	    {
		if(a[i][j]=='O')
		    o++;
		else if (a[i][j]=='X')
		    x++;
		else if (a[i][j]=='T')
		    r++;
	    }
	    if((x==3 && r==1) || (x==4))
	    {
		cout<<"Case #"<<tt<<": "<<"X won"<<endl;
		flag=1;
		break;
	    }
	    else if((o==3 && r==1) || (o==4))
	    {
		cout<<"Case #"<<tt<<": "<<"O won"<<endl;
		flag=1;
		break;
	    }
	}
	if(!flag)
	{
	    for(int j=0;j<4;j++)
	    {
		int o=0,x=0,r=0;
		for(int i=0;i<4;i++)
		{
		    if(a[i][j]=='O')
			o++;
		    else if (a[i][j]=='X')
			x++;
		    else if (a[i][j]=='T')
			r++;
		}
		if((x==3 && r==1) || (x==4))
		{
		    cout<<"Case #"<<tt<<": "<<"X won"<<endl;
		    flag=1;
		    break;
		}
		else if((o==3 && r==1) || (o==4))
		{
		    cout<<"Case #"<<tt<<": "<<"O won"<<endl;
		    flag=1;
		    break;
		}
	    }
	}
	if(!flag)
	{
	    int o=0,x=0,r=0;
	    for(int i=0;i<4;i++)
	    {
		if(a[i][i]=='O')
		    o++;
		else if (a[i][i]=='X')
		    x++;
		else if (a[i][i]=='T')
		    r++;
	    }
	    if((x==3 && r==1) || (x==4))
	    {
		cout<<"Case #"<<tt<<": "<<"X won"<<endl;
		flag=1;
	    }
	    else if((o==3 && r==1) || (o==4))
	    {
		cout<<"Case #"<<tt<<": "<<"O won"<<endl;
		flag=1;
	    }
	}
	if(!flag)
	{
	    int o=0,x=0,r=0;
	    for(int i=0;i<4;i++)
	    {
		if(a[i][3-i]=='O')
		    o++;
		else if (a[i][3-i]=='X')
		    x++;
		else if (a[i][3-i]=='T')
		    r++;
	    }
	    if((x==3 && r==1) || (x==4))
	    {
		cout<<"Case #"<<tt<<": "<<"X won"<<endl;
		flag=1;
	    }
	    else if((o==3 && r==1) || (o==4))
	    {
		cout<<"Case #"<<tt<<": "<<"O won"<<endl;
		flag=1;
	    }
	}
	if(!flag)
	{
	    for(int i=0;i<4;i++)
	    {
		for(int j=0;j<4;j++)
		{
		    if(a[i][j]=='.')
			flag=1;
		}
	    }
	    if(flag)
		cout<<"Case #"<<tt<<": "<<"Game has not completed"<<endl;
	    else
		cout<<"Case #"<<tt<<": "<<"Draw"<<endl;
	}
    }
    return 0;
}

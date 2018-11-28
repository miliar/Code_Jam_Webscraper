using namespace std;

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>

typedef long long unsigned int LLU;

int main()
{
    //freopen("A-small.in","r",stdin);
    //freopen("out-large.txt","w",stdout);
    int t,i=0,j=0,k=0;
    char game[4][4];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                cin>>game[j][k];
            }
        int uncompleted = 0;
        int win = 0;
	        	int j = 0;
	        	int k = 0;
	        	for(j = 0; j < 4; j++)
	        	{
	        		int x = 0;
	        		int o = 0;
	        		int t = 0;
	        		for(k = 0; k < 4; k++)
	        		{
	        			x += (game[j][k] == 'X')? 1:0;
	        			o += (game[j][k] == 'O')? 1:0;
	        			t += (game[j][k] == 'T')? 1:0;
	        			if (game[j][k] == '.')
                            uncompleted = 1;
	        		}
	        		if (x+t == 4)
	        		{
	        			cout<<"Case #"<<i<<": X won\n";
	        			win  = 1;
	        			break;
	        		}
	        		if (o+t == 4)
	        		{
	        			cout<<"Case #"<<i<<": O won\n";
	        			win  = 1;
	        			break;
	        		}
	        	}
	        	if(win)
	        	{
	        		continue;
	        	}

	        	for(j = 0; j < 4; j++)
	        	{
	        		int x = 0;
	        		int o = 0;
	        		int t = 0;
	        		for(k = 0; k < 4; k++)
	        		{
	        			x += (game[k][j] == 'X')? 1:0;
	        			o += (game[k][j] == 'O')? 1:0;
	        			t += (game[k][j] == 'T')? 1:0;
	        		}
	        		if (x+t == 4)
	        		{
	        			cout<<"Case #"<<i<<": X won\n";
	        			win  = 1;
	        			break;
	        		}
	        		if (o+t == 4){
	        			cout<<"Case #"<<i<<": O won\n";
	        			win  = 1;
	        			break;
	        		}
	        	}
	        	if(win)
	        	{
	        		continue;
	        	}
	        	int x = 0;
        		int o = 0;
        		int t = 0;

	        	for(j = 0; j < 4; j++)
	        	{
	        		x += (game[j][j] == 'X')? 1:0;
        			o += (game[j][j] == 'O')? 1:0;
        			t += (game[j][j] == 'T')? 1:0;
	        	}
	        	if (x+t == 4)
	        	{
        			cout<<"Case #"<<i<<": X won\n";
        			//br.readLine();
        			continue;
        		}
        		if (o+t == 4){
        			cout<<"Case #"<<i<<": O won\n";
        			continue;
        		}
        		x = 0;
        		o = 0;
        		t = 0;

        		for(j = 0; j < 4; j++)
        		{
	        		x += (game[j][3-j] == 'X')? 1:0;
        			o += (game[j][3-j] == 'O')? 1:0;
        			t += (game[j][3-j] == 'T')? 1:0;
	        	}
	        	if (x+t == 4){
        			cout<<"Case #"<<i<<": X won\n";
        			continue;
        		}
        		if (o+t == 4){
        			cout<<"Case #"<<i<<": O won\n";
        			continue;
        		}

	        	if(uncompleted)
	        	{
	        		cout<<"Case #"<<i<<": Game has not completed\n";
	        		continue;
	        	}
	        	cout<<"Case #"<<i<<": Draw\n";

	        }
    return 0;
}

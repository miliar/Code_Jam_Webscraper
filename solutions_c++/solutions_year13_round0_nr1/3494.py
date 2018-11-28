#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	int a[1001];
	for(int i=0;i<1001;i++) a[i] = 4;
	for(int k=0;k<t;k++)
	{
		char s[5][5];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++) 
				cin >> s[i][j];
		char q[100];
		gets(q);
		for(int i=0;i<4;i++)
		{
			int xc = 0, oc = 0, tc = 0; 
			for(int j=0;j<4;j++)
			{
				if(s[i][j] == 'X') xc++;
				if(s[i][j] == 'O') oc++;
				if(s[i][j] == 'T') tc++;		
			}	
			if(xc == 4 || (xc == 3 && tc == 1)) a[k] = 1;
			if(oc == 4 || (oc == 3 && tc == 1)) a[k] = 2;
		}
		for(int i=0;i<4;i++)
		{
			int xc = 0, oc = 0, tc = 0;
			for(int j=0;j<4;j++)
			{
				if(s[j][i] == 'X') xc++;
				if(s[j][i] == 'O') oc++;
				if(s[j][i] == 'T') tc++;		
			}	
			if(xc == 4 || (xc == 3 && tc == 1)) a[k] = 1;
			if(oc == 4 || (oc == 3 && tc == 1)) a[k] = 2;
		}
		int xc = 0 , oc = 0, tc = 0;
		for(int i=0;i<4;i++)
		{
			if(s[i][i] == 'X') xc++;
			if(s[i][i] == 'O') oc++;
			if(s[i][i] == 'T') tc++;	
		}
		if(xc == 4 || (xc == 3 && tc == 1)) a[k] = 1;
		if(oc == 4 || (oc == 3 && tc == 1)) a[k] = 2;
		xc = 0, oc = 0 , tc = 0; 
		for(int i=0;i<4;i++)
		{
			if(s[i][3-i] == 'X') xc++;
			if(s[i][3-i] == 'O') oc++;
			if(s[i][3-i] == 'T') tc++;	
		}
		if(xc == 4 || (xc == 3 && tc == 1)) a[k] = 1;
		if(oc == 4 || (oc == 3 && tc == 1)) a[k] = 2;
		
		if(a[k] == 4)
		{
			bool flag = false;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					if(s[i][j] == '.')
						flag = true;
			if(!flag) a[k] = 3;
		}	
	}
	for(int i=0;i<t;i++)
	{
		if(a[i] == 1) printf("Case #%d: X won\n",i+1);
		if(a[i] == 2) printf("Case #%d: O won\n",i+1);
		if(a[i] == 3) printf("Case #%d: Draw\n",i+1);
		if(a[i] == 4) printf("Case #%d: Game has not completed\n",i+1);	
	}
	return 0;	
}

#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <iomanip>

using namespace std;

char s[60][60];
int kol,t,n,m,k,i,j;

int main()
{
	freopen("A-large.in","r",stdin);	freopen("output.txt","w",stdout);
	cin>>t; k=1;
	while(t--)
	{
		cout<<"Case #"<<k<<":"<<endl;
		bool b=true;
		cin>>n>>m; kol=0;
		for(i=0;i<n;i++)
		{
			cin>>s[i]; 
			for(j=0;j<m;j++) {if (s[i][j]=='#') kol++;}
		}
		if(kol%4!=0&&kol>0) {cout<<"Impossible"<<endl;}
		else
		{
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
					if(s[i][j]=='#')
					{
						if(s[i+1][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j+1]=='#') {s[i][j]='/'; s[i][j+1]=92; s[i+1][j]=92; s[i+1][j+1]='/';} else {b=false; break;}
					}
				if(b==false) break;
			}
			if(b)
			{
				for(i=0;i<n;i++)
				{
					for(j=0;j<m;j++) cout<<s[i][j];
						cout<<endl;
				}
			} else {cout<<"Impossible"<<endl;}
		}

		k++;
	}


	fclose(stdin); fclose(stdout);
	return 0;
}
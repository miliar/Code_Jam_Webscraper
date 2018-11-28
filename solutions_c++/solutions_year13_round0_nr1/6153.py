#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<fstream>
#include<stack>
#include<queue>
using namespace std;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	char buf;
	char a[5][5];
	int tc;
	int sol;
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++)
	{
		scanf("%c",&buf);
		for(int i=0;i<4;i++)
			gets(a[i]);
		

				for(int i=0;i<4;i++)
				{
					char c = a[i][0];sol=0;if(c=='T')c=a[i][1]; if(c=='.'){sol=1;continue; }
					for(int j=1;j<4;j++)
						if(a[i][j]!=c && a[i][j]!='T') {sol=1; break;}
					if(!sol)
					{
						cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
						break;
					}
				}
				if(sol){
				for(int j=0;j<4;j++)
				{
					char c = a[0][j];sol=0; if(c=='T')c=a[1][j];if(c=='.'){sol=1;continue;}
					for(int i=1;i<4;i++)
						if(a[i][j]!=c && a[i][j]!='T'){sol=1; break;}
					if(!sol){
						cout<<"Case #"<<t<<": "<<c<<" won"<<endl; break;}

				}
				}
				if(sol){
					char c=a[0][0];sol=0; if(c=='T')c=a[1][1];if(c=='.'){sol=1;goto here;}
				for(int i=1;i<4;i++)
					if(a[i][i]!=c && a[i][i]!='T'){sol=1; break;}
					
				if(!sol)
					cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
				}

				here:
				if(sol){
					char c=a[0][3];sol=0; if(c=='T')c=a[1][2];if(c=='.'){sol=1;goto there;}
				for(int i=1;i<4;i++)
					if(a[i][3-i]!=c && a[i][3-i]!='T'){sol=1; break;}
				if(!sol){
					cout<<"Case #"<<t<<": "<<c<<" won"<<endl;
				}
				}
				there:
				if(sol){
				sol=0;
				for(int i=0;i<4;i++)
					for(int j=0;j<4;j++)
						if(a[i][j]=='.'){
							 sol=1; break;}
				if(sol)
					cout<<"Case #"<<t<<": Game has not completed"<<endl;
				else
					cout<<"Case #"<<t<<": Draw"<<endl;
				}
	}

	
	return 0;
}
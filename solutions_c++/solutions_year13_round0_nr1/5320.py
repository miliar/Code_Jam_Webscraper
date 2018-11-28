#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,in;
	for(in = 1,scanf("%d",&t);t--;in++)
	{
		char c[4][5];
		for(i=0;i<4;i++)
		scanf("%s",c[i]);
		printf("Case #%d: ",in);
		bool fdot = false;
		for(i=0;i<4 && !fdot;i++)
		for(j=0;j<4;j++)if(c[i][j]=='.'){fdot = true;break;}
		bool f = false;
		for(i=0;i<4;i++)
		{
			bool fr = false;
			char c1 = c[i][0];
			for(j=1;j<4;j++)
			{
				if(c1 == 'T' &&c[i][j] != '.')c1  = c[i][j];
				else if(c1 == '.' || (c[i][j]!=c1 && c[i][j]!='T')){
					fr = true;
					break;
				}
			}
			if(!fr){cout << c1 << " won\n";f =true; break;}
		}
		if(!f)
		{
			for(i=0;i<4;i++)
			{
				bool fc = false;
				char c1 = c[0][i];
				for(j=1;j<4;j++)
				{
					if(c1 == 'T' &&c[j][i] != '.')c1  = c[j][i];
					else if(c1 == '.' || (c[j][i]!=c1 && c[j][i]!='T')){
						fc = true;
						break;
					}
				}
				if(!fc){cout << c1 << " won\n";f =true; break;}
			}
		}
		if(!f)
		{
			char c1 = c[0][0], c2 = c[0][3];
			if(c1!='T' && c1 != '.' && (c[1][1]== c1 || c[1][1]=='T') && (c[2][2]==c1|| c[2][2]=='T') && (c[3][3]== c1|| c[3][3]=='T')){
				f = true;
				cout << c1 << " won\n";
			}
			else if(c1 == 'T' && c[1][1]== c[2][2] && c[2][2]==c[3][3]&& c[1][1]!='.')
			{
				f = true;
				cout << c[1][1] << " won\n";
			}
			if(!f)
			{
					if(c2!='T' && c2 != '.' && (c[1][2]== c2 || c[1][2]=='T') && (c[2][1]==c2|| c[2][1]=='T') && (c[3][0]== c2|| c[3][0]=='T')){
					f = true;
					cout << c2 << " won\n";
				}
				else if(c2 == 'T' && c[1][2]== c[2][1] && c[2][1]==c[3][0]&& c[1][2]!='.')
				{
					f = true;
					cout << c[1][2] << " won\n";
				}
			}
		}
		if(!f && fdot)cout << "Game has not completed\n";
		else if(!f &&!fdot)cout << "Draw\n";
	}
}
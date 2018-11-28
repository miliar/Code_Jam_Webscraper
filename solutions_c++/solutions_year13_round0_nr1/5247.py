#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int m;
	cin>>m;
	int mm=m;
	vector<string > s(4);
	while(m--)
	{
		getline(cin,s[0]);
		for(int i=0;i<4;i++)getline(cin,s[i]);
		string res="Draw";
		bool f=false;
		for(int i=0;i<4;i++)
		{
			int cX=0,cO=0;
			for(int j=0;j<4;j++)
			{
				if(s[i][j]=='T'){cX++;cO++;}
				if(s[i][j]=='X')cX++;
				if(s[i][j]=='O')cO++;
				if(s[i][j]=='.'){f=true;break;}
			}
			if(cX==4){res="X won";f=false;break;}
			if(cO==4){res="O won";f=false;break;}
			/////
			cX=0,cO=0;
			for(int j=0;j<4;j++)
			{
				if(s[j][i]=='T'){cX++;cO++;}
				if(s[j][i]=='X')cX++;
				if(s[j][i]=='O')cO++;
				if(s[j][i]=='.'){f=true;break;}
			}
			if(cX==4){res="X won";f=false;break;}
			if(cO==4){res="O won";f=false;break;}
			//////
			if(i)continue;
			cX=0,cO=0;
			for(int j=0;j<4;j++)
			{
				if(s[j][j]=='T'){cX++;cO++;}
				if(s[j][j]=='X')cX++;
				if(s[j][j]=='O')cO++;
				if(s[j][j]=='.'){f=true;break;}
			}
			if(cX==4){res="X won";f=false;break;}
			if(cO==4){res="O won";f=false;break;}
			/////////
			cX=0,cO=0;
			for(int j=0;j<4;j++)
			{
				if(s[j][3-j]=='T'){cX++;cO++;}
				if(s[j][3-j]=='X')cX++;
				if(s[j][3-j]=='O')cO++;
				if(s[j][3-j]=='.'){f=true;break;}
			}
			if(cX==4){res="X won";f=false;break;}
			if(cO==4){res="O won";f=false;break;}
		}
		if(f)res="Game has not completed";
		cout<<"Case #"<<(mm-m)<<": "<<res<<endl;
	}
	return 0;
}
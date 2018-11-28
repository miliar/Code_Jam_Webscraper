#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;



int main()
{
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		string s;
		int xr[4]={0},yr[4]={0},xc[4]={0},yc[4]={0},xd[2]={0},yd[2]={0},e=0;
		vector<string> v;
		for(int j=0;j<4;j++)
		{
			cin>>s;
			for(int k=0;k<s.size();k++)
			{
				if(s[k]=='X')
				{
					xr[k]++;
					xc[j]++;
					if(j==k)
						xd[0]++;
					if(j+k==3)
						xd[1]++;
				}
				else if(s[k]=='O')
				{
					yr[k]++;
					yc[j]++;
					if(j==k)
						yd[0]++;
					if(j+k==3)
						yd[1]++;
				}
				else if(s[k]=='T')
				{
					xr[k]++;
					xc[j]++;
					if(j==k)
						xd[0]++;
					if(j+k==3)
						xd[1]++;
					yr[k]++;
					yc[j]++;
					if(j==k)
						yd[0]++;
					if(j+k==3)
						yd[1]++;
				}
				else 
					e++;

			}
		}
		int x=0,o=0;
		for(int j=0;j<4;j++)
		{
			if(xr[j]==4 || xc[j]==4)
			{
				x=1;
				break;
			}
			if(yr[j]==4 || yc[j]==4)
			{
				o=1;
				break;
			}
		}
		if(xd[0]==4 || xd[1]==4)
			x=1;
		if(yd[0]==4 || yd[1]==4)
			o=1;
		if(x==1)
			cout<<"Case #"<<c<<": X won"<<endl;
		else if(o==1)
			cout<<"Case #"<<c<<": O won"<<endl;
		else if(e!=0)
			cout<<"Case #"<<c<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<c<<": Draw"<<endl;
		}
	return 0;
}

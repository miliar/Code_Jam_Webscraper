#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("p1.in");
	ofstream fout("p1.out");
	int t;
	vector <int> ans;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		string A[4];
		for(int j=0;j<4;j++)
		fin>>A[j];
		int x,y,p=0;
		for(int j=0;j<4;j++)
		{
			x=0;y=0;
			for(int k=0;k<4;k++)
			{
				if(A[j][k]=='X')
				{
					x++;
					p++;
				}
				if(A[j][k]=='O')
				{
					y++;
					p++;
				}
				if(A[j][k]=='T')
				{
					x++;
					y++;
					p++;
				}
			}
			if(x==4)
			{
				ans.push_back(1);
				break;
			}
			if(y==4)
			{
				ans.push_back(2);
				break;
			}
		}
		if((x==4)||(y==4))
		continue;
		for(int k=0;k<4;k++)
		{
			x=0;y=0;
			for(int j=0;j<4;j++)
			{
				if(A[j][k]=='X')
				{
					x++;
					p++;
				}
				if(A[j][k]=='O')
				{
					y++;
					p++;
				}
				if(A[j][k]=='T')
				{
					x++;
					y++;
					p++;
				}
			}
			if(x==4)
			{
				ans.push_back(1);
				break;
			}
			if(y==4)
			{
				ans.push_back(2);
				break;
			}
		}
		if((x==4)||(y==4))
		continue;
		x=0;y=0;
		for(int j=0,k=0;j<4;j++,k++)
		{
			if(A[j][k]=='X')
			{
				x++;
				p++;
			}
			if(A[j][k]=='O')
			{
				y++;
				p++;
			}
			if(A[j][k]=='T')
			{
				x++;
				y++;
				p++;
			}
		}
		if(x==4)
		{
			ans.push_back(1);
			continue;
		}
		if(y==4)
		{
			ans.push_back(2);
			continue;
		}
		x=0;y=0;
		for(int j=0,k=3;j<4;j++,k--)
		{
			if(A[j][k]=='X')
			{
				x++;
				p++;
			}
			if(A[j][k]=='O')
			{
				y++;
				p++;
			}
			if(A[j][k]=='T')
			{
				x++;
				y++;
				p++;
			}
		}
		if(x==4)
		{
			ans.push_back(1);
			continue;
		}
		if(y==4)
		{
			ans.push_back(2);
			continue;
		}
		if(p==40)
		ans.push_back(3);
		else
		ans.push_back(4);
	}
	for(int i=0;i<ans.size();i++)
	{
		fout<<"Case #"<<i+1<<":";
		if(ans[i]==1)
		fout<<" X won\n";
		else if(ans[i]==2)
		fout<<" O won\n";
		else if(ans[i]==3)
		fout<<" Draw\n";
		else
		fout<<" Game has not completed\n";
	}
	fin.close();
	fout.close();
	return 0;
}
	

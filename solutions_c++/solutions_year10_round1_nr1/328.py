#include<iostream>
#include<fstream>
using namespace std;

int map[51][51];
int t,n,k,c;
char ch;



bool win(int i,int j,int f)
{
	int g=0;
	int sum=0;
	while (i+g<n && map[i+g][j]==f)
	{
		++g;
		++sum;
	}
	if (sum>=k) return true;

	g=0;
	sum=0;
	while (j+g<n && map[i][j+g]==f)
	{
		++g;
		++sum;
	}
	if (sum>=k) return true;

	g=0;
	sum=0;
	while (i+g<n && j+g<n && map[i+g][j+g]==f)
	{
		++g;
		++sum;
	}
	if (sum>=k) return true;

		g=0;
	sum=0;
	while (i+g<n && j-g>=0 && map[i+g][j-g]==f)
	{
		++g;
		++sum;
	}
	if (sum>=k) return true;
	return false; 
}


int main()
{
	ifstream fin;
	fin.open("A.in");
	ofstream fout;
	fout.open("A.out");
	fin>>t;
	for (int c=0;c<t;++c)
	{
		fin>>n>>k;
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
			{
				do{fin>>ch;}while (ch!='.'&&ch!='R'&& ch!='B');
				switch (ch)
				{
				case '.':
					map[i][j]=0;
					break;
				case 'R':
					map[i][j]=1;
					break;
				case'B':
					map[i][j]=2;
				}
			}

			for (int i=0;i<n;i++)
			{
				int j=n-1;
				while (j>=0)
				{
					bool yes;
					while(map[i][j]==0)
					{
						yes=false;
						for (int g=j;g>=0;g--)
							if (map[i][g]!=0) yes=true;
						if (!yes) break;
						for (int g=j;g>0;g--)
							map[i][g]=map[i][g-1];
						map[i][0]=0;
					}
					j--;
				}
			}
///*
			for (int i=0;i<n;i++)
			{
				for (int j=0;j<n;j++)
					cout<<map[i][j];
				cout<<endl;
			}
//*/
			bool rwin=false ,bwin=false;
			for (int i=0;i<n;++i)
				for (int j=0;j<n;++j)
				{
					if (rwin==false &&map[i][j]==1)
					{
						rwin=win(i,j,1);
					}
					if (bwin==false && map[i][j]==2)
					{
						bwin=win(i,j,2);
					}
				}

			fout<<"Case #"<<c+1<<": ";
			if (rwin && bwin) fout<<"Both"<<endl;
			if (rwin && !bwin)fout<<"Red"<<endl;
			if (!rwin && bwin)fout<<"Blue"<<endl;
			if (!rwin && !bwin)fout<<"Neither"<<endl;
	}
	fout.close();
	//system("pause");
	return 0;
}
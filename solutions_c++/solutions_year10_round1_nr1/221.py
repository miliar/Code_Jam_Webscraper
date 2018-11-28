#include <iostream>
using namespace std;
const int MAXS=55;
char map[MAXS][MAXS];
char anwser[4][10]={"Red","Blue","Both","Neither"};
int t,result,n,k;
void check(int &result)
{
	result=3;
	for (int i=0;i<n;i++)
	{
		int cnt=0;
		char cur='.';
		for (int j=0;j<n;j++)
		{
			if (map[i][j]==cur)
			{
				cnt++;
			}
			else 
			{
				cur=map[i][j];
				cnt=1;
			}
			if(cnt>=k)
			{
				if (result==3)
				{
					if (cur=='R')
						result=0;
					else if (cur=='B')
						result=1;
				}
				else if (result!=2)
				{
					if (result==0&&cur=='B')
						result=2;
					else if (result==1&&cur=='R')
						result=2;
				}
			}
			if (result==2) return ;
		}
	}
	for (int i=0;i<n;i++)
	{
		int cnt=0;
		char cur='.';
		for (int j=0;j<n;j++)
		{
			if (map[j][i]==cur)
			{
				cnt++;
			}
			else 
			{
				cur=map[j][i];
				cnt=1;
			}
			if(cnt>=k)
			{
				if (result==3)
				{
					if (cur=='R')
						result=0;
					else if (cur=='B')
						result=1;
				}
				else if (result!=2)
				{
					if (result==0&&cur=='B')
						result=2;
					else if (result==1&&cur=='R')
						result=2;
				}
			}
			if (result==2) return ;
		}
	}
	int ci,cj;
		for (int j=0;j<n;j++)
		{
			int cnt=0;
			char cur='.';
			for (int l=0;j+l<n;l++)
			{
				ci=l;
				cj=j+l;
				if (map[ci][cj]==cur)
				{
					cnt++;
				}
				else 
				{
					cur=map[ci][cj];
					cnt=1;
				}
				if(cnt>=k)
				{
					if (result==3)
					{
						if (cur=='R')
							result=0;
						else if (cur=='B')
							result=1;
					}
					else if (result!=2)
					{
						if (result==0&&cur=='B')
							result=2;
						else if (result==1&&cur=='R')
							result=2;
					}
				}
				if (result==2) return ;
			}
		}
			for (int j=0;j<n;j++)
			{
				int cnt=0;
				char cur='.';
				for (int l=0;j+l<n;l++)
				{
					ci=l;
					cj=j+l;
					if (map[cj][ci]==cur)
					{
						cnt++;
					}
					else 
					{
						cur=map[cj][ci];
						cnt=1;
					}
					if(cnt>=k)
					{
						if (result==3)
						{
							if (cur=='R')
								result=0;
							else if (cur=='B')
								result=1;
						}
						else if (result!=2)
						{
							if (result==0&&cur=='B')
								result=2;
							else if (result==1&&cur=='R')
								result=2;
						}
					}
					if (result==2) return ;
				}
			}
				for (int j=0;j<n;j++)
				{
					int cnt=0;
					char cur='.';
					for (int l=0;l<n&&j-l>=0;l++)
					{
						ci=l;
						cj=j-l;
						if (map[ci][cj]==cur)
						{
							cnt++;
						}
						else 
						{
							cur=map[ci][cj];
							cnt=1;
						}
						if(cnt>=k)
						{
							if (result==3)
							{
								if (cur=='R')
									result=0;
								else if (cur=='B')
									result=1;
							}
							else if (result!=2)
							{
								if (result==0&&cur=='B')
									result=2;
								else if (result==1&&cur=='R')
									result=2;
							}
						}
						if (result==2) return ;
					}
				}
					for (int j=0;j<n;j++)
					{
						int cnt=0;
						char cur='.';
						for (int l=0;l<n&&j+l<n;l++)
						{
							ci=n-l;
							cj=j+l;
							if (map[cj][ci]==cur)
							{
								cnt++;
							}
							else 
							{
								cur=map[cj][ci];
								cnt=1;
							}
							if(cnt>=k)
							{
								if (result==3)
								{
									if (cur=='R')
										result=0;
									else if (cur=='B')
										result=1;
								}
								else if (result!=2)
								{
									if (result==0&&cur=='B')
										result=2;
									else if (result==1&&cur=='R')
										result=2;
								}
							}
							if (result==2) return ;
						}
					}
}
void printboard()
{
	for (int i=0;i<n;i++)
		cout<<map[i]<<endl;
}
int main()
{
	freopen("outA.out","w",stdout);
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>n>>k;
		for (int j=0;j<n;j++)
			cin>>map[j];
		int cnt=n-1;
		for (int j=0;j<n;j++)
		{
			cnt=n-1;
			for (int l=n-1;l>=0;l--)
			{
				if (map[j][l]!='.')
				{
					map[j][cnt]=map[j][l];
					cnt--;
				}
			}
			for (;cnt>=0;cnt--)
				map[j][cnt]='.';
		}
//		printboard();
		check(result);
//		cout<<"Case #1: Neither"<<endl;
		cout<<"Case #"<<i<<": "<<anwser[result]<<endl;
	}
}
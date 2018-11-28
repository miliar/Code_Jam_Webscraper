#include<iostream>
#include<fstream>
using namespace std;
int alt[100][100];
int map[100][100];
char ans[100][100];
int T,H,W;
int North=1;
int South=2;
int East=4;
int West=8;
char curr;
bool isin(int i,int j, int H,int W)
{
	return (i>=0 && i<H && j>=0 && j<W);
}
void floodfill(int r,int c,int H,int W)
{
	if(isin(r,c,H,W) && ans[r][c]==0)
	{
		ans[r][c]=curr;
		if(map[r][c]&North)
			floodfill(r-1,c,H,W);
		if(map[r][c]&South)
			floodfill(r+1,c,H,W);
		if(map[r][c]&West)
			floodfill(r,c-1,H,W);
		if(map[r][c]&East)
			floodfill(r,c+1,H,W);
	}
}
int main()
{
	int i,j,k;
	int minalt;
	ifstream fin("B-large.in");
	ofstream fout("B.out");
	fin>>T;
	for(i=0;i<T;++i)
	{
		fout<<"Case #"<<(i+1)<<":"<<endl;
		fin>>H>>W;
		for(j=0;j<H;++j)
		{
			for(k=0;k<W;++k)
			{
				fin>>alt[j][k];
				map[j][k]=0;
				ans[j][k]=0;
			}
		}
		//minalt=1000000000;
		//build undirected graph;
		for(j=0;j<H;++j)
		{
			for(k=0;k<W;++k)
			{
				minalt=alt[j][k];
				if(isin(j-1,k,H,W) && minalt>alt[j-1][k])
					minalt=alt[j-1][k];	
				if(isin(j+1,k,H,W) && minalt>alt[j+1][k])
					minalt=alt[j+1][k];	
				if(isin(j,k-1,H,W) && minalt>alt[j][k-1])
					minalt=alt[j][k-1];	
				if(isin(j,k+1,H,W) && minalt>alt[j][k+1])
					minalt=alt[j][k+1];	
				if(j==0&& k==1)
					cout<<alt[j][k]<<" "<<minalt<<" "<<T<<" "<<H<<" "<<W<<endl;
				if(minalt<alt[j][k]){
				if(isin(j-1,k,H,W) && minalt==alt[j-1][k])//North
				{
					map[j][k]|=North;
					map[j-1][k]|=South;
				}
				else if(isin(j,k-1,H,W) && minalt==alt[j][k-1])//West
				{
					map[j][k]|=West;
					map[j][k-1]|=East;
				}
				else if(isin(j,k+1,H,W) && minalt==alt[j][k+1])//East
				{
					map[j][k]|=East;
					map[j][k+1]|=West;
				}
				else if(isin(j+1,k,H,W) && minalt==alt[j+1][k])//South
				{
					map[j][k]|=South;
					map[j+1][k]|=North;
				}
				}
			}
		}
		//floodfill
		curr='a';
		for(j=0;j<H;++j)
		{
			for(k=0;k<W;++k)
			{
				if(ans[j][k]==0)
				{
					floodfill(j,k,H,W);
					++curr;
				}
			}
		}
		//print
		for(j=0;j<H;++j)
		{
			fout<<ans[j][0];
			for(k=1;k<W;++k)
			{
				fout<<" "<<ans[j][k];
			}
			fout<<endl;
		}
	}
	return 0;
}
					

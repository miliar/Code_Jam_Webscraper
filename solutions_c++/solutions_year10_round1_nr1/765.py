#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream dat("a.in");
ofstream sol("a.out");

char a[51][51];
int b[51][51][4];
int c[5001][2];

int n,k;

int Find(char ch)
{
	int i,j,q;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			if(a[i][j]==ch) 
			{
				if (j-1>=0 && a[i][j-1]==ch) b[i][j][0]+=b[i][j-1][0];
				if (i-1>=0 && j-1>=0 && a[i-1][j-1]==ch) b[i][j][1]+=b[i-1][j-1][1];
				if (i-1>=0 && j>=0 && a[i-1][j]==ch) b[i][j][2]+=b[i-1][j][2];
				if (i-1>=0 && j+1<n && a[i-1][j+1]==ch) b[i][j][3]+=b[i-1][j+1][3];
				for(q=0;q<4;q++)
					if(b[i][j][q]>=k) return 1;
			}
	}
	return 0;
}
int main()
{
	int t;
	dat >> t;
	int i,j,p,q;
	char ch;
	string s;
	for(p=1;p<=t;p++)
	{
		dat >> n >> k;
		for(i=0;i<n;i++)
		{
			s="";
			for(j=0;j<n;j++)
			{
				dat >> ch;
				if (ch!='.') s=s+ch;
				for(q=0;q<4;q++) b[i][j][q]=1;				
			}
			int l=s.length();
			for(j=0;j<n-l;j++) a[i][j]='.';
			for(j=n-l;j<n;j++) a[i][j]=s[j-n+l];			
		}
		int r1=Find('R'),r2=Find('B');
		sol << "Case #"<<p<<": ";
		if (r1 && r2) sol << "Both" << endl;
		else if (r1 && !r2) sol << "Red" << endl;
		else if (!r1 && r2) sol << "Blue" << endl;
		else sol << "Neither" << endl;
	}
	return 0;
} 
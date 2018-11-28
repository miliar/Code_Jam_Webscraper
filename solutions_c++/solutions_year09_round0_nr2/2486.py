#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int T, H, W;

int **hh = NULL;
ifstream o("B-large.in");
ofstream oo("a.out");
void read()
{
	
	
	int i, j;
	if(hh!=NULL)
	{
		for(i=0; i<H; i++)
			delete []hh[i];
		delete []hh;
	}
	o>>H>>W;
	cout<<H<<" "<<W<<endl;
	hh = new int*[H];
	for(i=0; i<H; i++)
		hh[i] = new int[W];
	
	for(i=0; i<H; i++)
	{
		for(j=0; j<W; j++)
		{
			o>>hh[i][j];
			cout<<hh[i][j]<<" ";
		}
		cout<<endl;
	}
}



void onecase(int x)
{
	int i, j;
	
	char currentc = 'a';
	//mm
	char **mm = new char*[H];
	for(i=0; i<H; i++)
		mm[i] = new char[W];
	for(i=0; i<H; i++)
	{
		for(j=0; j<W; j++)
		{
			mm[i][j]='-';
		}
	}
	//ll
	int **ll = new int*[H];
	for(i=0; i<H; i++)
		ll[i] = new int[W];
	for(i=0; i<H; i++)
	{
		for(j=0; j<W; j++)
		{
			int m=i;
			int n=j;
			int a = hh[m][n];
			int ah, aw;
			if(m-1>=0)
			{
				if(mm[m-1][n]=='-' && hh[m-1][n]<a)
				{
					a=hh[m-1][n];
					ah = m-1;
					aw = n;
				}
			}
			if(n-1>=0)
			{
				if(mm[m][n-1]=='-' && hh[m][n-1]<a)
				{
					a=hh[m][n-1];
					ah = m;
					aw = n-1;
				}
			}
			if(n+1<W)
			{
				if(mm[m][n+1]=='-' && hh[m][n+1]<a)
				{
					a=hh[m][n+1];
					ah = m;
					aw = n+1;
				}
			}
			if(m+1<H)
			{
				if(mm[m+1][n]=='-' && hh[m+1][n]<a)
				{
					a=hh[m+1][n];
					ah = m+1;
					aw = n;
				}
			}
			if(a<hh[m][n])
			{
				ll[m][n]=ah*W+aw;
				
			}
			else
				ll[m][n]=-1;
		}
		
	}
	//start
	for(i=0; i<H; i++)
	{
		for(j=0; j<W; j++)
		{
			if(mm[i][j]=='-') //one river
			{
				queue<int> q;
				mm[i][j]=currentc;
				q.push(i*W+j);
				while(q.size()>0)
				{
					int m, n;
					m=q.front()/W;
					n=q.front()%W;
					q.pop();
					int ah, aw;
					if(ll[m][n]>=0)
					{
						ah=ll[m][n]/W;
						aw=ll[m][n]%W;
						if(mm[ah][aw]=='-')
						{
							mm[ah][aw]=currentc;
							q.push(ah*W+aw);
						}
					}
					if(m-1>=0)
					{
						if(mm[m-1][n]=='-' && ll[m-1][n]==m*W+n)
						{
							mm[m-1][n]=currentc;
							q.push((m-1)*W+n);
						}
					}
					if(n-1>=0)
					{
						if(mm[m][n-1]=='-' && ll[m][n-1]==m*W+n)
						{
							mm[m][n-1]=currentc;
							q.push((m)*W+n-1);
						}
					}
					if(n+1<W)
					{
						if(mm[m][n+1]=='-' && ll[m][n+1]==m*W+n)
						{
							mm[m][n+1]=currentc;
							q.push((m)*W+n+1);
						}
					}
					if(m+1<H)
					{
						if(mm[m+1][n]=='-' && ll[m+1][n]==m*W+n)
						{
							mm[m+1][n]=currentc;
							q.push((m+1)*W+n);
						}
					}
					
				}
				currentc = currentc+1;
			}
			
		}
	}
	oo<<"Case #"<<x<<":\n";
	cout<<"Case #"<<x<<":\n";
	for(i=0; i<H; i++)
	{
		for(j=0; j<W; j++)
		{
			oo<<mm[i][j];
			if(j<W-1)
				oo<<" ";
			else
				oo<<"\n";
			cout<<mm[i][j];
			if(j<W-1)
				cout<<" ";
			else
				cout<<"\n";
		}
	}
	
}

int main()
{
	o>>T;
	cout<<T<<endl;
	for(int i=1; i<=T; i++)
	{
		read();
		onecase(i);
	}
	oo.close();
	return 0;
}

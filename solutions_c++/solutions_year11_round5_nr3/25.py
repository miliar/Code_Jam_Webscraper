#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

int leftdeg[10000];
int rightdeg[10000];

bool leftdone[10000];
bool rightdone[10000];

int leftedges[10000][8];
int rightedges[10000][8];

int r,c;

int toint(int row, int col)
{
	return row*c + col;
}

void add(int left, int right)
{
	//cerr << left << " " << right << endl;
	leftedges[left][leftdeg[left]]=right;
	leftdeg[left]++;
	rightedges[right][rightdeg[right]]=left;
	rightdeg[right]++;
}



int mod = 1000003;

int dolis[25000];

int MX = 1000000;


void show(int n)
{
	return;
	for(int i=0; i<n; i++)
	{
		cerr << i << " " << leftdone[i] << " " << leftdeg[i] << " ";
		for(int j=0; j<leftdeg[i]; j++)
		{
			cerr << leftedges[i][j] << " ";
		}
		cerr << endl;
	}
	cerr << endl;
	for(int i=0; i<n; i++)
	{
		cerr << i << " " << rightdone[i] << " " << rightdeg[i] << " ";
		for(int j=0; j<rightdeg[i]; j++)
		{
			cerr << rightedges[i][j] << " ";
		}
		cerr << endl;
	}
	cerr << endl << endl;
}

int sol(int n)
{
	show(n);
	int readfrom = 0;
	int writeto = 0;
	
	
	int i,j,k,m;
	
	for(i=0; i<n; i++)
	{
		if(rightdeg[i]==0)
			return 0;
		if(rightdeg[i]==1)
		{
			dolis[writeto]=i+MX;
			writeto++;
		}
	}
	
	while(readfrom < writeto)
	{
		k = dolis[readfrom];
		
		if(k >= MX)
		{
			//cerr << k << endl;
			//right vertex
			k-=MX;
			if(rightdeg[k]==1)
			{
				rightdeg[k]--;
				rightdone[k]=true;
				i = rightedges[k][0];
				
				for(j=0; j<leftdeg[i]; j++)
				{
					if(leftedges[i][j]==k)
						continue;
					m = leftedges[i][j];
//					int x = 0;
					for(int x=0; x<rightdeg[m]; x++)
					{
						if(rightedges[m][x]==i)
						{
							rightedges[m][x]=rightedges[m][rightdeg[m]-1];
							rightdeg[m]--;
							break;
						}
					}
					if(rightdeg[m]==1)
					{
						dolis[writeto]=m+MX;
						writeto++;
					}
				}
			}
		}
		readfrom++;
	}
	
	show(n);
	
	for(i=0; i<n; i++)
	{
		if(rightdeg[i]==0 && rightdone[i]==false)
			return 0;
		
	}
	
	int ans = 1;
	
	//count cycles
	
	for(i=0; i<n; i++)
	{
		if(rightdone[i])
			continue;
		
		j = i;
		k = -1;
		
		do
		{
			rightdone[j]=true;
			
			if(rightedges[j][0]==k)
			{
				m = rightedges[j][1];
			}
			else {
				m=rightedges[j][0];
			}
			
			leftdone[m]=true;
			
			if(leftedges[m][0]==j)
			{
				j = leftedges[m][1];
			}
			else {
				j=leftedges[m][0];
			}
			k =m;
		} while(j!=i);
		
		ans*=2;
		ans%=mod;
	}
	return ans;
}
		


					
					
				
				
			
	

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		int ans = 0;
		
		
		memset(leftdeg,0,sizeof(leftdeg));
		memset(rightdeg,0,sizeof(rightdeg));
		
		memset(leftedges,0,sizeof(leftedges));
		memset(rightedges,0,sizeof(rightedges));
		
		memset(leftdone,0,sizeof(leftdone));
		memset(rightdone,0,sizeof(rightdone));
		
		fin >> r >> c;
		
		char cc;
		
		int nr,nc;
		
		for(i=0; i<r;i++)
		{
			for(j=0; j<c; j++)
			{
				fin >> cc;
				int curr = toint(i,j);
				if(cc=='|')
				{
										
					k = toint((i+1)%r,(j)%c);
					add(curr,k);
					k = toint((i+r-1)%r,(j)%c);
					add(curr,k);
				}
				else if(cc=='-')
				{
					k = toint((i)%r,(j+1)%c);
					add(curr,k);
					k = toint((i)%r,(j+c-1)%c);
					add(curr,k);
				}
				else if(cc=='/')
				{
					k = toint((i+r-1)%r,(j+1)%c);
					add(curr,k);
					k = toint((i+1)%r,(j+c-1)%c);
					add(curr,k);
				}
				else {
					k = toint((i+1)%r,(j+1)%c);
					add(curr,k);
					k = toint((i+r-1)%r,(j+c-1)%c);
					add(curr,k);
				
				}

			}
		}
		
		
					
		ans=sol(r*c);
		
		
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
		
	}
	
	
	return 0;
}


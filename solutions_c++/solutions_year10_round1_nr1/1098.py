#include<iostream>
#include<fstream>
#include<cmath>
#include<conio.h>

#include<stdio.h>
#include<time.h>
using namespace std;
int arr[50][50],b[50][50],n,k;
void init()
{
	memset(arr,0,sizeof(arr));
}
void disp(int a[50][50])
{
	for ( int y = 0 ; y < n; y++)
	{
		for ( int z = 0 ; z < n ; z++)
		{
			cout << (char)a[y][z]<< " ";
		}
		cout << endl;
	}
	
}
void swap(int &a,int &b)
{
	int t = a;
	a =b;
	b = t;
}
int check(int c[50][50],int col)
{
	for(int i = n-1; i >= 0 ; i--)
	{
		if(c[i][col]=='.')
		{
			for(int j = i-1; j>=0;j--)
			{
				if(c[j][col] != '.')
				{
					return 0;

				}
			}
		}
	}
	return 1;
}
void col(int c[50][50],int col)
{
	for(int i = n-1; i >= 0 ; i--)
	{

		if(c[i][col]=='.')
		{
			for(int j = i-1; j>=0;j--)
			{
				if(c[j][col] != '.')
				{
					swap(c[j][col],c[i][col]);
					
					if(check(c,col))
						return;
					
					break;

				}
			}
		}
	}
}
int check_rc(int b[50][50],int aa)
{
	char c;
	int flag;
	if(aa == 1)
		c='R';
	else
		c='B';
	for(int i = 0 ; i < n; i++)
	{
		for(int j = 0 ; j < n; j++)
		{
			if(b[i][j]==c)
			{
				int p;
				for( p = 0 ; p < k ; p++)
				{
					if(j+p >= n)
					{
						
						break;
					}
					if(b[i][j+p] != c)
					{
						
						break;
					}
				}
				if(p==k)
					return 1;


				
				for( p = 0 ; p < k  ; p++)
				{
					
					if(i+p >= n)
					{
						
						break;
					}
					if(b[i+p][j] != c)
					{
						
						break;
					}
				}
				if(p==k)
					return 1;

				
				for( p = 0 ; p < k  ; p++)
				{
					if(j+p >= n || i+p >=n)
					{
						
						break;
					}
					if(b[i+p][j+p] != c)
					{
						
						break;
					}
				}
				if(p==k)
					return 1;
				for(p = 0 ; p < k  ; p++)
				{
					if(j-p < 0 || i+p >=n)
					{
						
						break;
					}
					if(b[i+p][j-p] != c)
					{
						
						break;
					}
				}
				if(p==k)
					return 1;
			}
		}
	}
	return 0;
}

int func()
{
	//cout << "N : " << n << " K :"<< k<<endl;
	
	int i,j,kk;
	for( i = n-1,kk=0 ; i>=0 ; i--,kk++)
	{
		for(j=0;j<n;j++)
		{
			b[j][kk]=arr[i][j];
		}
	}
	for(i = 0 ; i < n ; i++)
		col(b,i);
//	disp(b);
	i=check_rc(b,1);
	//cout << " I : " << i;
	j=check_rc(b,2);
	//cout << " j : " << j;
	
	if(i==0&&j==0)
		i=1;
	else if(i==1&&j==1)
		i=2;
	else if(i==1&&j==0)
		i=3;
	else if(i==0&&j==1)
		i=4;


	
	return (i);

}
int main()
{  



	
	int no,temp;
	char c;
    FILE *f;
	f=fopen("input.txt","r");
	fstream f2("output.txt",ios::out);
	fscanf(f,"%d",&no);
	long long unsigned int y,z;
	for ( int i = 1 ; i <= no ; i ++)
	{
		cout << i << endl;
		fscanf(f,"%d %d",&n,&k);
		c=fgetc(f);
		for ( y = 0 ; y < n; y++)
		{
			for ( int z = 0 ; z < n ; z++)
			{
				fscanf(f,"%c",&arr[y][z]);
			}
			c=fgetc(f);
			
				
			
		}
		
		temp = func();
		if ( temp == 1)
		{
			f2 << "Case #" <<i<<": Neither"<<endl;
		}
		else if (temp == 2)
		{
			f2 << "Case #"<<i<<": Both"<<endl;
		}
		else if (temp == 3)
		{
			f2 << "Case #"<<i<<": Red"<<endl;
		}
		else if (temp == 4)
		{
			f2 << "Case #"<<i<<": Blue"<<endl;
		}
	}
	//cin.get();
	f2.close();
}


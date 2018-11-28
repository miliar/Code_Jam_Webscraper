#include<iostream>

using namespace std;
char arry[101][101];
char arry1[101][101];
bool red=false;
bool blue=false;
void search(int m,int n,int N,int K)
{
	int i,j,k;
	
	int r=1,b=1;
	//right
	if(N-n+1>=K)
	{
		if(!red&&arry[m][n]=='R')
		{
			for(j=n+1;j<=N;j++)
			{
				if(arry[m][j]!='R')
				{
					break;
				}
				else
				{ r++;if(r==K) red=true;}
			}
			r=1;
		}
		else if(!blue&&arry[m][n]=='B')
		{
			for(j=n+1;j<=N;j++)
			{
				if(arry[m][j]!='B')
				{
					break;
				}
				else
				{ b++;if(b==K) blue=true;}
			}
			b=1;
		}
	}

	
	//down
	if(N-m+1>=K)
	{
		if(!red&&arry[m][n]=='R')
		{
			for(j=m+1;j<=N;j++)
			{
				if(arry[j][n]!='R')
				{
					break;
				}
				else
				{ r++;if(r==K) red=true;}
			}
			r=1;
		}
		else if(!blue&&arry[m][n]=='B')
		{
			for(j=m+1;j<=N;j++)
			{
				if(arry[j][n]!='B')
				{
					break;
				}
				else
				{ b++;if(b==K) blue=true;}
			}
			b=1;
		}
	}
		


	//down right

	if(N-m+1>=K&&N-n+1>=K)
	{
		if(!red&&arry[m][n]=='R')
		{
			for(j=n+1,i=m+1;i<=N&&j<=N;i++,j++)
			{
				if(arry[i][j]!='R')
					break;
				else
				{ r++;if(r==K) red=true;}
			}
			r=1;
			
		}
		else if(!blue&&arry[m][n]=='B')
		{
			for(j=n+1,i=m+1;i<=N&&j<=N;i++,j++)
			{
				if(arry[i][j]!='B')
					break;
				else
				{ b++;if(b==K) blue=true;}
			}
			b=1;
		}
	}
	//down left
	if(N-m+1>=K&& n>=K)
	{
		if(!red&&arry[m][n]=='R')
		{
			for(j=n-1,i=m+1;i<=N&&j>=1;i++,j--)
			{
				if(arry[i][j]!='R')
					break;
				else
				{ r++;if(r==K) red=true;}
			}
			r=1;
			
		}
		else if(!blue&&arry[m][n]=='B')
		{
			for(j=n-1,i=m+1;i<=N&&j>=1;i++,j--)
			{
				if(arry[i][j]!='B')
					break;
				else
				{ b++;if(b==K) blue=true;}
			}
			b=1;
		}
	}
	


}
int main()
{
	int T ,N ,K;
	int i,j,k,l;
	char temp;
	cin>>T;
	for(i=0;i<T;i++)
	{	

		red=false;
		blue=false;
		cin>>N>>K;

		for(j=1;j<=N;j++)
		{
			for(k=1;k<=N;k++)
			{
				arry[j][k]='.';
			}
		}
	    for(j=1;j<=N;j++)
		{
			for(k=1;k<=N;k++)
			{
				cin>>arry1[j][k];
	
			}
		}

		for(j=1;j<=N;j++)
		{
			for(k=N,l=N;k>=1&&l>=1;l--)
			{
				if(arry1[j][l]!='.')
				{
					arry[j][k]=arry1[j][l];
					k--;
				}
			}
		}
		for(j=1;j<=N;j++)
		{
			for(k=1;k<=N;k++)
			{
				search(j,k,N,K);
			}
		}

		if(red&&blue)
		{
			cout<<"Case #"<<i+1<<": Both"<<endl;
		}
		else if(red)
		{
			cout<<"Case #"<<i+1<<": Red"<<endl;
		}
		else if(blue)
		{
			cout<<"Case #"<<i+1<<": Blue"<<endl;
		}
		else
			cout<<"Case #"<<i+1<<": Neither"<<endl;
	}
}
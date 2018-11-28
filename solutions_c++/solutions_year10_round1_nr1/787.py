#include <iostream>

using namespace std;

int t,n,k;
char board[51][51];
bool findr,findb;

void rotate()
{
	int i,j,k1;
	for (i=0; i<n; i++)
		for (j=n-1; j>=0; j--)
			if (board[i][j]!='.')
			{
				k1=j+1;
				while (board[i][k1]=='.') k1++;
				k1--;
				board[i][k1]=board[i][j];
				if (k1!=j) board[i][j]='.';
			}
	/*for (i=0; i<n; i++)
	{
		for (j=0; j<n; j++)
			cout<<board[i][j];
		cout<<endl;
	}*/
}

void findr1()
{
	int i,j,l,m;
	bool flag;
	for (i=0; i<n; i++)
		for (j=0; j<=n-k; j++)
		{
			if (board[i][j]!='R') continue;
			l=j+1;
			while (board[i][j]==board[i][l]) l++;
			if (l-j>=k)
			{
				findr=true;
				return;
			}
		}
		//cout<<"ok1"<<endl;
	for (j=0; j<n; j++)
		for (i=0; i<=n-k; i++)
		{
			if (board[i][j]!='R') continue;
			l=i+1;
			while (board[i][j]==board[l][j]) l++;
			if (l-i>=k)
			{
				findr=true;
				return;
			}
		}
		//cout<<"ok2"<<endl;
	for (i=0; i<=n-k; i++)
		for (j=0; j<=n-k; j++)
		{
			if (board[i][j]!='R') continue;
			l=i+1;
			m=j+1;
			while (board[i][j]==board[l][m]) 
			{
				l++;
				m++;
			}
			if (l-i>=k)
			{
				findr=true;
				return;
			}
		}
		//cout<<"ok3"<<endl;
	for (i=0; i<=n-k; i++)
		for (j=n-1; j>=k-1; j--)
		{
			if (board[i][j]!='R') continue;
			l=i+1;
			m=j-1;
			while (board[i][j]==board[l][m]&&m>=0) 
			{
				l++;
				m--;
			}
			if (l-i>=k)
			{
				findr=true;
				return;
			}
		}		
		//cout<<"ok4"<<endl;
}

void findb1()
{
	int i,j,l,m;
	bool flag;
	for (i=0; i<n; i++)
		for (j=0; j<=n-k; j++)
		{
			if (board[i][j]!='B') continue;
			l=j+1;
			while (board[i][j]==board[i][l]) l++;
			if (l-j>=k)
			{
				findb=true;
				return;
			}
		}
		//cout<<"ok1"<<endl;
	for (j=0; j<n; j++)
		for (i=0; i<=n-k; i++)
		{
			if (board[i][j]!='B') continue;
			l=i+1;
			while (board[i][j]==board[l][j]) l++;
			if (l-i>=k)
			{
				findb=true;
				return;
			}
		}
		//cout<<"ok2"<<endl;
	for (i=0; i<=n-k; i++)
		for (j=0; j<=n-k; j++)
		{
			if (board[i][j]!='B') continue;
			l=i+1;
			m=j+1;
			while (board[i][j]==board[l][m]) 
			{
				l++;
				m++;
			}
			if (l-i>=k)
			{
				findb=true;
				return;
			}
		}
		//cout<<"ok3"<<endl;
	for (i=0; i<=n-k; i++)
		for (j=n-1; j>=k-1; j--)
		{
			if (board[i][j]!='B') continue;
			l=i+1;
			m=j-1;
			while (board[i][j]==board[l][m]&&m>=0) 
			{
				l++;
				m--;
			}
			if (l-i>=k)
			{
				findb=true;
				return;
			}
		}		
		//cout<<"ok4"<<endl;
}

int main()
{
	int i,j,c;
	cin>>t;
	for (c=1; c<=t; c++)
	{
		for (i=0; i<51; i++)
			for (j=0; j<51; j++)
				board[i][j]=' ';
		findr=false;
		findb=false;
		cin>>n>>k;
		for (i=0; i<n; i++)
			cin>>board[i];
		rotate();
		findr1();
		findb1();
		cout<<"Case #"<<c<<": ";
		if (findr&&findb)
			cout<<"Both"<<endl;
		else if (findr)
			cout<<"Red"<<endl;
		else if (findb)
			cout<<"Blue"<<endl;
		else
			cout<<"Neither"<<endl;
	}
	return 0;
}

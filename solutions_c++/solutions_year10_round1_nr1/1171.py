#include <iostream>
#include <vector>

using namespace std;

bool check(vector< vector<char> >& t,int K,char x)
{	
	int N=t.size();
	
	int m;
	for(int i=0; i!=N ; i++)
	{
		m=0;
		int j=0;
		while(j<N)
		{
			while(j<N && t[i][j]==x)
			{
				m++;
				j++;

				if(m==K)
				return 1;
			}

			m=0;
			j++;

		}
	}

		
	for(int i=0; i!=N ; i++)
	{
		 m=0;
		int j=0;
		while(j<N)
		{
			while( j<N && t[j][i]==x)
			{
				m++;
				j++;

				if(m==K)
				return 1;
			}
			m=0;
			j++;

		}
	}
	

	 
	for(int i=0; i!=N ; i++)
	{
		 m=0;
		int j=0;
		int k=i;
		while(j<i+1)
		{
			while(k>=0 && j<N && t[k][j]==x)
			{
				m++;
				j++;
				k--;
				if(m==K)
				return 1;
			}
			m=0;
			j++;
			k--;

		}
	}

	 
	for(int i=1; i != N   ; i++)
	{
		 m=0;
		int j=N-1;
		int k=i;
		while(k<N)
		{
			while(j>=0 && k<N && t[j][k]==x)
			{
				m++;
				j--;
				k++;
				if(m==K)
				return 1;
			}
			m=0;
			j--;
			k++;

		}
	}

	
	
	for(int i=0; i!=N ; i++)
	{
		 m=0;
		int j=N-1;
		int k=i;
		while(k>=0)
		{
			while(k>=0 && j>=0 && t[j][k]==x)
			{
				m++;
				j--;
				k--;
				if(m==K)
				return 1;
			}
			m=0;
			j--;
			k--;

		}
	}

	
	for(int i=N-2; i >=0   ; i--)
	{

		 m=0;
		int j=N-1;
		int k=i;
		while(k>=0)
		{
			while(k>=0 && j>=0 && t[k][j]==x)
			{
				m++;
				j--;
				k--;
				if(m==K)
				return 1;
			}
			m=0;
			j--;
			k--;

		}
	}

	return 0;
}

		

int main()
{
	int num_case;

	cin>>num_case;

	for(int i=0; i!=num_case ; i++)
	{
		

		int N,K;

		cin>>N;
cin>>K;
	char c;

	vector<char> x(N,0);
	vector< vector<char> > table(N,x);
	for(int j=0; j!=N; j++)
	for(int k=0; k!=N; k++)
	{
		cin>>c;
		table[j][k]=c;
	}

	for(int j=0; j!=N; j++)
	{
		int k;
		int m=N;

		while(1)
		{
		k=m;
		for( k=m-1;table[j][k]=='.';k--);

		if(k<0)
		break;

		c=table[j][m-1];
		table[j][m-1]= table[j][k];
		table[j][k]=c;

		m--;
		}
	}

	/*
	for(int j=0; j!=N; j++)
	{
	for(int k=0; k!=N; k++)
	{
		
		cout<<table[j][k];
	}
	cout<<endl;
	}*/

	bool red,blue;

	red=check(table,K,'R');
	blue=check(table,K,'B');
	
	//cout<<red<<blue<<"flags"<<endl;
	cout<<"Case #"<<i+1<<": ";
	if(red & blue)
	cout<<"Both";
	 if ( red & !blue)
	cout<<"Red";
	if(!red & blue)
	cout<<"Blue";
	if( !red & !blue )
	cout<<"Neither";
	
	cout<<endl;
	}

	return 0;
}
		

	
		
		

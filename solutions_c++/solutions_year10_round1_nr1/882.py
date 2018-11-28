#include <iostream>
using namespace std;
int T;
int N,K;

unsigned char** table;
char c;
bool red;
bool blue;
bool both;

void testInRow(int i, int j)
{
	unsigned char testChar=table[i][j];
	bool* assign;
	if(testChar=='B')
		assign=&blue;
	else
		assign=&red;
	int count=1;
	int ii=i,jj=j;
	while(--ii>=0)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	ii=i;
	while(++ii<N)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	if(count>=K)
	{
		*assign=true;
		return;
	}

	ii=i;
	count=1;
	while(--jj>=0)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	jj=j;
	while(++jj<N)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	if(count>=K)
	{
		*assign=true;
		return;
	}

	jj=j;
	count=1;
	while(--jj>=0&&--ii>=0)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	jj=j;ii=i;
	while(++jj<N&&++ii<N)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	if(count>=K)
	{
		*assign=true;
		return;
	}

	jj=j;ii=i;
	count=1;
	while(++jj<N&&--ii>=0)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	jj=j;ii=i;
	while(--jj>=0&&++ii<N)
	{
		if(table[ii][jj]==testChar)count++;
		else break;
	}
	if(count>=K)
	{
		*assign=true;
		return;
	}
}
void testInARow()
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(table[i][j]!=',')
				testInRow(i,j);
			if(blue&&red)
			{
				both=true;
				return;
			}
		}
	}
}
int main()
{
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>N>>K;
		table=new unsigned char*[N];
		for(int i=0;i<N;i++)
			table[i]=new unsigned char[N];

		for(int i=0;i<N;i++)
		{
			for( int j=0;j<N;j++)
			{
				cin>>table[i][j];
			}
		}

		for(int i=0;i<N;i++)
		{
			int j=N-1;
			while(j>=0)
			{
				if(table[i][j]=='.')
				{
					for(int jj=j;jj>0;jj--)
					{
						table[i][jj]=table[i][jj-1];
					}
					table[i][0]=',';
				}
				else
				{
					j--;
				}
			}
		}

		testInARow();

		if(both)
			cout<<"Case #"<<t<<": Both"<<endl;
		else if(blue)
			cout<<"Case #"<<t<<": Blue"<<endl;
		else if(red)
			cout<<"Case #"<<t<<": Red"<<endl;
		else
			cout<<"Case #"<<t<<": Neither"<<endl;

		for( int i=0;i<N;i++)
			delete[] table[i];
		delete[] table;
		red=false;
		blue=false;
		both=false;
	}
	return 0;
}


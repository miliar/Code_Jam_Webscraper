#include <iostream>
using namespace std;


int T,test,N,K,i,j,k,l,f;
char a[55][55],b[55][55],buf[55];
bool red=false,blue=false;
int main()
{
	

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		red=blue=false;
		cin>>N>>K;
		for(i=0;i<N;i++)
			cin>>a[i];
		for(i=0;i<N;i++)
			for(j=0;j<N;j++)
				b[i][j]=a[N-1-j][i];

		
		for(i=0;i<N;i++)
		{
			k=0;
			for(j=0;j<51;j++)
				buf[j]=0;
			for(j=N-1;j>=0;j--)
				if(b[j][i]!='.')
					buf[k]=b[j][i],k++;
			k=0;
			for(j=N-1;j>=0&&buf[k];j--)
				b[j][i]=buf[k],k++;
			for(;j>=0;j--)
				b[j][i]='.';

		}
	for(i=0;i<N&&!red;i++)
		for(j=0;j<=N-K&&!red;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i][j+l]!='R')
					f=0;
			if(f)red=true;
		};
				
	for(i=0;i<N&&!blue;i++)
		for(j=0;j<=N-K&&!blue;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i][j+l]!='B')
					f=0;
			if(f)blue=true;
		};

	for(i=0;i<=N-K&&!red;i++)
		for(j=0;j<N&&!red;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+l][j]!='R')
					f=0;
			if(f)
				red=true;
		};
	for(i=0;i<=N-K&&!blue;i++)
		for(j=0;j<N&&!blue;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+l][j]!='B')
					f=0;
			if(f)
				blue=true;
		};
	for(i=0;i<=N-K&&!red;i++)
		for(j=0;j<=N-K&&!red;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+l][j+l]!='R')
					f=0;
			if(f)
				red=true;
		};
	for(i=0;i<=N-K&&!blue;i++)
		for(j=0;j<=N-K&&!blue;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+l][j+l]!='B')
					f=0;
			if(f)
				blue=true;
		};
	for(i=0;i<=N-K&&!red;i++)
		for(j=0;j<=N-K&&!red;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+K-l-1][j+l]!='R')
					f=0;
			if(f)
				red=true;
		};
	for(i=0;i<=N-K&&!blue;i++)
		for(j=0;j<=N-K&&!blue;j++)
		{
			f=1;
			for(l=0;l<K;l++)
				if(b[i+K-l-1][j+l]!='B')
					f=0;
			if(f)
				blue=true;
		};
	cout<<"Case #"<<test<<": ";
	if(blue&&red)
		cout<<"Both";
	else
	{
		if(blue)
			cout<<"Blue";
		else
			if(red)
				cout<<"Red";
			else
				cout<<"Neither";
	}
	cout<<"\n";
	}	
	return 0;
}
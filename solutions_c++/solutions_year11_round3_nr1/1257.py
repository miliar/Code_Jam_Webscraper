#include <iostream>

using namespace std;

long long n,a,b,i,j,k,mas[100][100],im=1,cas=1;
char c;

void casen()
{
cout<<"Case #"<<cas<<":"<<endl;
cas++;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>n;
	
	for(i=0;i<n;i++)
	{
		cin>>a>>b;
		im=1;
	for(j=0;j<a;j++)
		for(k=0;k<b;k++)
			{
			cin>>c;
			if(c=='#') mas[j][k]=1;
			if(c=='.') mas[j][k]=0;
			}
	for(j=0;j<a;j++)
		for(k=0;k<b;k++)
			{
				if(mas[j][k]==1)
				{
				if(mas[j][k+1]==1&&mas[j+1][k]==1&&mas[j+1][k+1]==1)
				{
				mas[j][k]=2;
				mas[j][k+1]=3;
				mas[j+1][k]=4;
				mas[j+1][k+1]=5;
				}
				else im=0;
				}
			}
			casen();
			if(im)
			{
			for(j=0;j<a;j++){
			for(k=0;k<b;k++)
			{
			if(mas[j][k]==0)cout<<'.';
			if(mas[j][k]==2||mas[j][k]==5)cout<<'/';
			if(mas[j][k]==3||mas[j][k]==4)cout<<'\\';
			}
			cout<<endl;
			}
			}
			else cout<<"Impossible"<<endl;
		
		
	}
	return 0;
}
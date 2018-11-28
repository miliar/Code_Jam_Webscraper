#include<iostream>
using namespace std;
int main()
{
	int l,n,d;
	cin>>l>>d>>n;
	char di[d][l];
	int k;
	string a;
	string in[n];
	for(int i=0;i<d;i++)
	{
		cin>>a;
		for(int j=0;j<l;j++)
		{
			di[i][j]=a[j];
		}
	}
	for(int i=0;i<n;i++)
	{
		cin>>in[i];
		int counter=0;

		for(int j=0;j<d;j++)
		{
			int pos=0;
			for(k=0;k<l;k++)
			{
				if(in[i][pos]=='(')
				{
					bool valid=false;
					while(in[i][pos]!=')')
					{
						if(in[i][pos]==di[j][k])
							valid=true;
						pos++;
					}
					if(!valid)
						break;
				}
				else if(in[i][pos]!=di[j][k])
				{
					pos++;
					//cout<<"chirag";
					break;
				}
				pos++;
				
			}
			if(k==l)
				counter++;
		}
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}

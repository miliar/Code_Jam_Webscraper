#include <iostream>
using namespace std;

int main()
{
	int t,r,c,i,j,k;
	bool b;
	char s[50][52];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>r>>c;
		b=1;
		for(i=0;i<r;i++)
			cin>>s[i];
		for(i=0;i<r;i++)
			for(k=0;k<c;k++)
				if(s[i][k]=='#')
				{
				//	cout<<i<<' '<<j<<endl;
					if(i==r-1 || k==c-1 || s[i][k+1]!='#' || s[i+1][k]!='#' || s[i+1][k+1]!='#')
					{
						b=0;goto ans;
					}
					s[i][k]='/';
					s[i][k+1]='\\';
					s[i+1][k+1]='/';
					s[i+1][k]='\\';
				}
ans:
		
		cout<<"Case #"<<j<<":\n";
		if(b)
		{
			for(i=0;i<r;i++)
				cout<<s[i]<<endl;
		}else
			cout<<"Impossible\n";
		
	}
}

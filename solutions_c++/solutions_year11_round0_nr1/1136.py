#include <iostream>

using namespace std;

int t,n;
char s[100];
int a[100];

int main()
{
	cin>>t;
	for(int id=1;id<=t;id++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>s[i]>>a[i];
		}
		int pi=0,pj=0,i=1,j=1;
		int tot=0;
	//	cout<<n<<endl;
		while(1)
		{
			while(pi<n&&s[pi]!='O')pi++;
			while(pj<n&&s[pj]!='B')pj++;
		//	cout<<pi<<' '<<pj<<endl;
			if(pi==n&&pj==n)break;
			tot++;
			if(pi<n)
			{
				if(i!=a[pi])
				{
					if(i>a[pi])i--;else i++;
				}else if(pi<pj)
					pi++;
			}
			if(pj<n)
			{
				if(j!=a[pj])
				{
					if(j>a[pj])j--;else j++;
				}else if(pj<pi)
					pj++;
			}
		}
		cout<<"Case #"<<id<<": ";
		cout<<tot<<endl;
	}
}

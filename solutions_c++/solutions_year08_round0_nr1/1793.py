#include <iostream>
#include <string>
using namespace std;

string a[100];
int b[100],c[1000],s,q;

int remain()
{
	int sum=0,i;
	for (i=0;i<s;i++)
		if (b[i]==0) sum++;
	return sum;
};

int main()
{
	int t,n,i,j,k=1,res;
	string str;
	char ch[100];

	for (cin>>t;t>0;t--)
	{
		res=0;
		cin>>s;
		getchar();
		for (i=0;i<s;i++) {cin.getline(ch,sizeof(ch));a[i]=ch;b[i]=0;}
		cin>>q;
		getchar();
		for (i=0;i<q;i++)
		{
			cin.getline(ch,sizeof(ch));
			str=ch;
			for (j=0;j<s;j++)
			{
				if (str==a[j]) c[i]=j;
			}
		}
		for (i=0;i<q;i++)
		{
			b[c[i]]++;
			if (remain()==0)
			{
				res++;
				for (j=0;j<s;j++) b[j]=0;
				b[c[i]]++;
			}
		}
		cout<<"Case #"<<k++<<": "<<res<<endl;
	}
	return 0;
}

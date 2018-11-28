#include <iostream>
#include <string>
using namespace std;
string w[5005];
char temp[100000];
bool b[100000][30];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int c,k,n,len,i,j,z,f,s;
	cin>>c>>k>>n;
	for(i=0;i<k;i++)
	{
		cin>>w[i];
	}
	for(i=1;i<=n;i++)
	{
		s=0;
		cin>>temp;
		len=strlen(temp);
		z=0;
		for(j=0;j<len;j++)
		{
			memset(b[z],0,sizeof(b[z]));
			if(temp[j]=='(')
			{
				for(f=j+1;temp[f]!=')';f++)
				{
					b[z][temp[f]-'a']=true;
				}
				z++;
				j=f;
			}
			else
			{
				b[z][temp[j]-'a']=true;
				z++;
			}
		}
		for(j=0;j<k;j++)
		{
			bool match=true;
			for(f=0;f<c;f++)
			{
				if(!b[f][w[j][f]-'a'])
				{
					match=false;
					break;
				}
			}
			if(match) s++;
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
	}

	return 0;
}


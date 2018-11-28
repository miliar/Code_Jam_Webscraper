#include<iostream>
#include<string>
#include<map>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;
	int t =1;
	while(t<=n)
	{
		string a;
		cin>>a;
		map<char , int > ma;
		for(int i = 0 ; i < a.length(); i++)
		{
			//ma.find(a[i])
			ma[a[i]]=-1;
		}
		int len = ma.size();
		if(len==1)
			len++;
		ma[a[0]]=1;
		int j=0;
		for(i = 1 ; i< a.length(); i++)
		{
			
				if(ma[a[i]]==-1)
				{
					if(j==1)j++;
					ma[a[i]]=j;
					j++;
				}
		}
		__int64 an=0,mi=1;
		for(i = a.length()-1; i>=0 ; i--)
		{
			//cout<<len<<" "<<ma[a[i]]<<endl;
			an +=mi*ma[a[i]];
			mi *= len;
		
		}
		printf("Case #%d: %I64d\n",t,an);
		t++;
	}
}
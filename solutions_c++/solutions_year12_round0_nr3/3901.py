#include <iostream>
using namespace std;

string gao(int x)
{
	if(x==0)
	return "0";
	string s="";
	while(x)
	{
		s=s+(char)(x%10+'0');
		x/=10;
		
	}
	string t="";
	for(int i=s.size()-1;i>=0;i--)
	t=t+s[i];
	return t;
}

int main()
{
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int a,b,i,j;
	int cases=1;
	int repeat;
	cin>>repeat;
	while(repeat--)
	{
		cin>>a>>b;
		int ans=0;
		for(i=a;i<=b;i++)
		{
			//cout<<i<<endl;
			string s=gao(i);
			
			int T=10;
		
			while(T--)
			{
				if(s.size()>1)
				s=s.substr(1)+s[0];
				else s=s;
				
				int y=0;
				for(j=0;j<s.size();j++)
				{
					y=y*10+s[j]-'0';
				}
				if(y>i&&y<=b)
					ans++;
				if(y==i)
				break;
			}
		
			
		}
		cout<<"Case #"<<cases++<<": "<<ans<<endl;
	}
	



	return 0;
	
	
}
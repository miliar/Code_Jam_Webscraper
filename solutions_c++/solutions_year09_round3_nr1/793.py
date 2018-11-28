#include<iostream>
using namespace std;

int cha[100];

int GetIndex(char a)
{
	if(a>='a'&&a<='z') return int(a-'a');
	else if(a>='A'&&a<='Z') return int(a-'A'+26);
	else if(a>='0'&&a<='9') return int(a-'0'+52);
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T;
	string s;
	cin>>T;
	for(int line=1;line<=T;line++)
	{
		cin>>s;
		int base=0;
		memset(cha,-1,sizeof(cha));
		for(int i=0;i<s.length();i++)
		{
			int index=GetIndex(s[i]);
			if(cha[index]==-1)
			{
				cha[index]=-2;
				base++;
			}			
		}
		if(base==1) base++;
		cha[GetIndex(s[0])]=1;
		int number=0;
		for(int i=1;i<s.length();i++)
		{
			if(number==1) number++;
			if(cha[GetIndex(s[i])]>=0) continue;
			cha[GetIndex(s[i])]=number;
			number++;
		}
		long long int  ans=0;
		for(int i=0;i<s.length();i++)
		{
			ans = ans*base +  cha[GetIndex(s[i])];
		}
		cout<<"Case #"<<line<<": "<<ans<<endl;		
	}
}

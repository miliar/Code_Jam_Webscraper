#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int a[900];
int bb[900];
int main()
{
	ifstream cin("in.txt");
	ofstream cout("out1.txt");
	int T;
	cin>>T;
	int k;
	for(k=1; k<=T; k++)
	{
		int i,j;
		for(i=0; i<900; i++)
			a[i]=-1;
		memset(bb,0,sizeof(bb));
		int an,b,n;
		cin>>an;
		for(i=0; i<an; i++)
		{
			string s;
			cin>>s;
			a[(s[0]-'A')*26+(s[1]-'A')]=s[2]-'A';
			a[(s[1]-'A')*26+(s[0]-'A')]=s[2]-'A';
			//cout<<<<endl;
		}
		cin>>b;
		for(i=0; i<b; i++)
		{
			string s;
			cin>>s;
			bb[(s[0]-'A')*26+(s[1]-'A')]=-2;
			bb[(s[1]-'A')*26+(s[0]-'A')]=-2;
			
		}
		cin>>n;
		string s;
		cin>>s;
		for(i=1; i<n; i++)
		{
			int temp=i-1;
			int begin=i;
			if(a[(s[i-1]-'A')*26+(s[i]-'A')]!=-1)
			{
				s[i-1]='A'+a[(s[i-1]-'A')*26+(s[i]-'A')];
				s.erase(i,1);
				n--;
				temp=i-2;
				i=i-1;
				if(i==0)
					i=1;
				begin=i;
			}
			for(j=temp; j>=0; j--)
			{
				int ans=26*(s[begin]-'A');
				if(bb[ans+(s[j]-'A')]==-2)
				{
					s.erase(0,temp+2);
				//	cout<<"s=="<<s<<endl;
					n=s.size();
					i=0;
					break;
				}
			}
		}
		
		cout<<"Case #"<<k<<": "<<"[";
		int len;
		len=s.size();
		if(len==0)
			cout<<"]"<<endl;
		else
		{
			for(i=0; i<len-1; i++)
			{
				cout<<s[i];
				cout<<", ";
			}
			cout<<s[i]<<"]"<<endl;
		}

	}
	return 0;
}
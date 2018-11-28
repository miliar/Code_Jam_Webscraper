#include<iostream>
#include<vector>
#include<sstream>
#define pb push_back

using namespace std;
int ans;
vector<vector<string> >v1;
void go(string s)
{

//cout<<s<<endl;
	vector<string>t;
	//cout<<s<<"  ";
	stringstream st(s);
			while(st >> s)
			{
				t.pb(s);
			}
int key=0;			
			for(int i=0;i<v1.size();i++)
			{
				
					int k=0;int j=0;
					while(v1[i][j]==t[k])
					{
						
					
							k++;
							j++;
							if(j == v1[i].size() || k == t.size())break;
							}
							key=max(k,key);
				
			}
		//	cout<<key<<endl;
if(key!=t.size())
{
	ans+=t.size()-key ;
	v1.pb(t);
	}
	}
							

			
int main()
{
	int t;
	 cin>>t;
	 int ct=0;
	 while(t--)
	 {
	 ct++;
	 ans=0;
	 int a,b;
	 scanf("%d %d",&a,&b);
	 v1.clear();
	//cout<<a<<"  "<<b<<endl;
	 for(int i=0;i<a;i++)
	 {
		string s;
		cin>>s;
		
		int ct=0;
		for(int j=0;j<s.size();j++)
		{
			if(s[j]=='/'){s[j]=' ';}
			}
		
			stringstream st(s);
			vector<string>sss;
			while(st >> s)
			{
			//cout<<s<<endl;
				sss.pb(s);
			}
			v1.pb(sss);
		}	
			
			
		 
		
		
	for(int i=0;i<b;i++)
	{
	
		string s;
		cin>>s;
		for(int j=0;j<s.size();j++)
		{
			if(s[j]=='/')s[j]=' ';
			}
			go(s);
			
			
	}
	
	 
	cout<<"Case #"<<ct<<": "<<ans<<endl;
	 }
		return 0;
		
}		
	 
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int t,i,flag=0,count=0,j,k,a,n,m,flag1=0;
	cin>>t;
	vector <string> cre,alr;
	string s,temp;
	size_t found;

	for(k=1;k<=t;k++)
	{
		cin>>n>>m;
		cre.clear();
		cre.resize(n);
		for(i=0;i<n;i++)
		{
			cin>>s;	
			s+='/';
			//cout<<s<<"\n";
			cre[i]=s;
		}
		alr.clear();
		count=0;
		for(j=0;j<m;j++)
		{
			s="";			
			cin>>s;
			s+='/';
			temp="";
			temp+='/';
			for(i=1;i<s.length();i++)
			{
				temp+=s[i];
				if(s[i]=='/')
				{
					flag=0;					
					for(a=0;a<alr.size();a++)
					{
						if(temp==alr[a])
						{
							flag=1;
							break;
						}
					}
					if(flag==0 && n==0)
					{
						alr.push_back(temp);
						count++;
					}
					if(flag==0)
					{					
						flag1=0;						
						for(a=0;a<n;a++)
						{
							found=cre[a].find(temp);
							//cout<<"temp = "<<temp<<"\n";
							if((found!=string::npos && (int)found==0) || temp==cre[a])
							{
								alr.push_back(temp);
								flag1=1;
								break;
							}
						
						}
						if(flag1==0 && n!=0)
							{
								count++;
								//cout<<temp<<"\n";
								alr.push_back(temp);
							}
					}
				}
			}
		}
		cout<<"Case #"<<k<<": "<<count<<"\n";
	}
	return 0;
}

				
				

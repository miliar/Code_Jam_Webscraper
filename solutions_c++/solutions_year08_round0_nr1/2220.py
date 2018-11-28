#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
int N;
cin>>N;
for(int k=0;k<N;k++)
{
int s,q,count=0,switches=0;
cin>>s;
vector<string> eng;
string temp;
bool flag[s];
for(int i=0;i<s;i++)
	flag[i]=false;
getline(cin,temp);
for(int i=0;i<s;i++)
	{
	getline(cin,temp);
	eng.push_back(temp);
	}
/*for(int i=0;i<s;i++)
	cout<<eng[i]<<endl;*/
//fflush(stdin);
cin>>q;
getline(cin,temp);
for(int i=0;i<q;i++)
	{	
		getline(cin,temp);
		for(int j=0;j<eng.size();j++)
			{
			//cout<<"j="<<j<<" ";
			if(temp==eng[j])
				{
				//cout<<"temp==eng[j]"<<temp<<" ";
				if(flag[j]==false)
					{
					count++;
					flag[j]=true;
					if(count==s)
						{						
						switches++;
						count=1;
						for(int k=0;k<s;k++) flag[k]=false;
						flag[j]=true;
						}					
					}
				break;
				}
			}
	}
cout<<"Case #"<<k+1<<": "<<switches<<endl;
}
return 0;
}


# include <iostream>
# include <vector>
# include <algorithm>
# include <string>
# include <cmath>
# include <stdio.h>
using namespace std;
int main()
{
	int i,j,k,vis[200],base[200],cases,v[200];
	double baseneeded;
	long long int n,cnt,res;
	cin>>n;
	char mp[37]={1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35};
	for(cases=1;cases<=n;cases++)
	{
		string str;
		cin>>str;
		memset(vis,0,sizeof(vis));
		memset(base,0,sizeof(base));
		memset(v,0,sizeof(v));
		cnt=0;
		res=0;
		for(i=0;i<str.size();i++)
		{
			if(!vis[str[i]-'0'])
			{
				vis[str[i]-'0']=1;
				cnt++;
			}
		}
		if(cnt==1)
			baseneeded=2;
		else
			baseneeded=cnt;
		k=0;
		for(i=0;i<str.size();i++)
		{
			if(!base[str[i]] && !v[str[i]])
			{
				//cout<<str[i]<<" "<<i<<" "<<k<<endl;
				base[str[i]]=mp[k];
				v[str[i]]=1;
				k++;
			}
		}
		//cout<<"over"<<baseneeded<<endl;		
		
		/*for(i=0;i<str.size();i++)
		{
			cout<<base[str[i]]<<endl;
		}*/
		

		double m=0;
		reverse(str.begin(),str.end());
		for(i=0;i<str.size();i++)
		{
			//cout<<base[str[i]]<<" "<<baseneeded<<" "<<m<<endl;
			
			long long int pwr=(long long int)pow(baseneeded,m);
			res+=base[str[i]]*pwr;
			m++;
		}
		cout<<"Case #"<<cases<<": "<<res<<endl;
	}
}


/*
if(str.size()==1)
		{
			res=1;
			break;
		}
		else if(str.size()==2)
		{
	     		if(cnt==2)
					res=2;
				else if(cnt==1)
					res=3;
				break;
		}
		else
		{
			base[str[i]]=mp[k];
		}
*/

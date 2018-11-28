#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

int main()
{
	int test;
	cin>>test;
	int r=1;
	while(test--)
	{
				string str;
				cin>>str;
				int base=0,ind=1;
				int len=str.size();
				vector<bool>seen(len,true);
				for(int i=0;i<len;i++)
				{
					if(seen[i])
					{
						base++;
						for(int j=i+1;j<len;j++)
						{
							if(str[i]==str[j]) seen[j]=false;
						}
					}
				}
				if(base==1) base++;
				//cout<<base<<endl;
				map<char,int>mm;
				int cnt=0;
				for(int i=0;i<len;i++)
				{
					if(seen[i])
					{
						if(cnt==1)
						{
							mm[str[i]]=0;
							cnt++;
						}
						else
						{
							mm[str[i]]=ind++;
							cnt++;
						}
					}
				}
				/*for(map<char,int>::iterator it=mm.begin();it!=mm.end();it++)
				{
					cout<<(*it).first<<" "<<(*it).second<<endl;
				}*/
				unsigned long long ret=0UL,mult=1UL;
				for(int i=len-1;i>=0;i--)
				{
					ret+=(mm[str[i]]*mult);
					mult*=base;
					//cout<<ret<<endl;
				}
				cout<<"Case #"<<r++<<": "<<ret<<endl;
	}
	return 0;
}
		

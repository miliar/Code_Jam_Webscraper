#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
	FILE* ifp = freopen("B-large.in","r",stdin);
	//FILE* ifp = freopen("B-A.in","r",stdin);
	FILE* ofp = freopen("B-large.out","w",stdout);
	int n,index,absv;
	string str,str_b;
	cin>>n;
	for(int i=0;i<n;++i)
	{
		cin>>str;
		str_b = str;
		absv = -1;
		for(int j=str.size()-2;j>=0;--j)
		{			
			for(int k=j+1;k<str.size();++k)
			{
				if(str[j] < str[k])
				{
					if((absv > 0) && (absv > str[k] - str[j]))
					{
						absv = str[k] - str[j];	
						index = k;					
					}
					else
					{
						absv = str[k] - str[j];
						index = k;
					}
				}				
			}
			if(absv >0)
			{
				swap(str[j],str[index]);
				sort(str.begin()+j+1,str.end());
				break;
			}
		}
		if(str.compare(str_b) == 0)
		{
			sort(str.begin(),str.end());
			str.insert(1,"0");
			if(str[0] == '0')
				for(int k=1;k<str.size();++k)
				{
					if(str[k] != '0')						
					{
						swap(str[0],str[k]);
						break;
					}
				}
		}
		cout<<"Case #"<<i+1<<": "<<str<<endl;
	}
	return 0;
}

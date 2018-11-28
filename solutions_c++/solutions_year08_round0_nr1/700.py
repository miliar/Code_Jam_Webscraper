#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
int main()
{
	freopen("A-large.in","r",stdin);
  	freopen("A-large.out","w",stdout);
	int i,j,Case,num,s,q,ans,t;
	char str1[101];
	string str;
	cin>>Case;
	gets(str1);
	num=1;
	map<string,int>map1;
	vector<string> name;
	while (Case--)
	{
		map1.clear();
		name.clear();
        cin>>s;
		gets(str1);
		for(i=0;i<s;i++)
		{
			gets(str1);
			str=str1;
			map1[str]=0;
			name.push_back(str); 
		}
		ans=0;
		t=0;
	    cin>>q;
		//cout<<q<<endl;
		gets(str1);
		for(i=0;i<q;i++)
		{
			gets(str1); 
			str=str1;
		    if(map1[str]==0)
			{
			  t++;
			  if(t==s)
			  {
			    for(j=0;j<s;j++)
				{
				  map1[name[j]]=0;
				}
				t=1;
				ans++;
			  }	
			  map1[str]=1;
			}
		}	
		printf("Case #%d: %d\n",num++,ans);	
	}
	return 0; 
}
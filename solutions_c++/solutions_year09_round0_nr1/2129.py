#include<iostream>
#include<regex.h>
#include<vector>
#include<cstring>
using namespace std;
int main()
{
	int l,d,n,c=1;
	cin>>l>>d>>n;
	vector<string>list;
	
	for(int i=0;i<d;i++)
	{
		string s;
		cin>>s;
		list.push_back(s);
		
	}
	while(c<=n)
	{
		int tot=0;
		string pattern="",temp;
		cin>>temp;
		for(int j=0;j<temp.size();j++)
		{
			if(temp[j]=='(')
			pattern+='[';
			else if(temp[j]==')')
			pattern+=']';
			else pattern+=temp[j];
		}
		regex_t reg;
		regmatch_t matches[1];
		regcomp(&reg,pattern.c_str(),REG_EXTENDED|REG_ICASE);
		for(int i=0;i<list.size();i++)
		{
			string str=list[i];
			if (regexec(&reg,str.c_str(),1,matches,0)==0 )
				tot++;
		}
		cout<<"Case #"<<c<<": "<<tot<<"\n";
		c++;
	}
	
	
}

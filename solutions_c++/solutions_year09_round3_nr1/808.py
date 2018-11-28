#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<map>
using namespace std;
unsigned __int64 mypow(int x,int y)
{

	
	if(y==0) return 1;
	unsigned __int64 ret=1;

	unsigned __int64 base=x;
	for(int i=0;i<y;i++)
		ret*=base;
	return ret;
}
int main()
{
	ifstream in("d:/study/gcj/A-large.in");
	ofstream out("d:/study/gcj/A-large.out");
	int N;

	in>>N;
	for(int i=0;i<N;i++)
	{
		string str;
		in>>str;
		int base=0;
		for(int j=0;j<str.length();j++)
		{

			if(j>0)
			{
				if(str.substr(0,j).find(str[j])!=string::npos)
				{
					continue;
				}else
					base++;
			}else base++;

		}
		if(base==1) base=2;
		;
		vector<int> base10;
		map<char,int> tab;
		int start=0;
		for(int t=0;t<str.length();t++)
		{
			if(t==0)
			{
				base10.push_back(1);
				tab.insert(pair<char,int>(str[t],1));

			}else
			{
				if(tab.find(str[t])!=tab.end())
				{
					base10.push_back(tab[str[t]]);
				}else
				{

					if(start==1) start++;
					tab.insert(pair<char,char>(str[t],start));
					base10.push_back(start);
					start++;

				}
			}
		}
		unsigned __int64 ret=0;
		int s=base10.size();
		for(int f=0;f<base10.size();f++)
		{
			
			ret+=base10[f]*mypow(base,s-f-1);
		}
		string strret="";
		while(ret!=0)
		{
			strret+=char('0'+ret%10);
			ret=ret/10;
		}
	  out<<"Case #"<<(i+1)<<": ";
	  for(int p=strret.length()-1;p>=0;p--)
		  out<<strret[p];
	  out<<endl;

		

	}
	return 0;
}


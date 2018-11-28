#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

main()
{
int l,d,n;
vector <string> dict;
string a;

scanf("%d %d %d\n",&l,&d,&n);

for(int i=0;i<d;i++)
{
 getline(cin,a);
 dict.push_back(a);
}

sort(dict.begin(),dict.end());

for(int i=1;i<=n;i++)
{
 		int k=0;
		vector <string> valid(dict);
 		getline(cin,a);
		for(int j=0;j<a.size();j++,k++)
 		{
	 		if(a[j]=='(')
	 		{
		 	  int x=j+1;
		 	  while(a[x]!=')')
   				x++;
			
			 for(int c=valid.size()-1;c>=0;c--)
			  {
				  bool cont=false;
				  for(int l=j+1;l<x;l++)
				  {
					if(a.at(l)==valid[c].at(k))
					 cont=true;
				   }
				   if(!cont)
				   {
				   valid.erase(valid.begin()+c);
				   }
			   }
			   if(valid.empty())
			   break;
			   j=x;
			}
			else
			{
				for(int c=valid.size()-1;c>=0;c--)
				{
					if(a.at(j)!=valid[c].at(k))
					{
					   valid.erase(valid.begin()+c);
			   		}
			   }
			   if(valid.empty())
			   break;
			}
		}
	cout<<"Case #"<<i<<": "<<valid.size()<<endl;
}
}

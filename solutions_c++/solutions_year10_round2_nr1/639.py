#include<iostream>
#include<map>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	int k;
	cin>>k;
	int tll=0;
	map<string,bool> mp;
	while(k--)
	{
		tll++;
		int n,m;
		cin>>n>>m;
		char abc[103];
			char * pch;
			string tmp,tmp1="";
		for(int i=0;i<n;i++)
		{
			cin>>abc;
			// printf ("Splitting string \"%s\" into tokens:\n",str);
			pch = strtok (abc,"/");
			tmp1="";
			while (pch != NULL)
			{
				tmp=pch;
				tmp+="-";
				tmp1+=tmp;
			    
				//printf ("%s\n",pch);
		//		cout<<tmp<<" "<<tmp1<<endl;
				mp[tmp1]=true;
				//	m.insert(pair<string,bool>(tmp,true));
				pch = strtok (NULL, "/");
			}


		}
		long long int cnt=0;
		for(int i=0;i<m;i++)
		{
			cin>>abc;
			pch = strtok (abc,"/");
			//string tmp;
tmp1="";
			while (pch != NULL)
			{
				tmp=pch;  
				tmp+="-";
				tmp1+=tmp;
				if(mp[tmp1]!=true)  
					cnt++;
				mp[tmp1]=true;
				//printf ("%s\n",pch);
				//cout<<tmp;
				//mp[tmp]=true;
				//	m.insert(pair<string,bool>(tmp,true));
				pch = strtok (NULL, "/");

			}



		}
mp.clear();
cout<<"Case #"<<tll<<": "<<cnt<<endl;
	}
}

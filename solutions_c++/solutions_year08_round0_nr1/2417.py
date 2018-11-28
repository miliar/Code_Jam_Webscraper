#include<iostream>
#include<string>
#include<map>
#include<fstream>
using namespace std;

int main1()
{
	map<string,int> se;
	string str;
	int query[1001];
	int array[101];
	int s=0;
	int q=0;

	for(int i=0;i<101;i++)
		array[i]=0;

	cin>>s;
	getline(cin,str,'\n');
	for(int i=0;i<s;i++)
	{
//		cin>>str;
		getline(cin,str,'\n');
		se[str]=i;
//		cout<<str<< ":" ;
	}

	cin>>q;
	getline(cin,str,'\n');
	int tot=0;
	for(int i=0;i<q;i++)
	{
		map<string,int>::iterator it;
		getline(cin,str,'\n');

		it=se.find(str);
		if ( it == se.end() )
			continue;
		query[tot]=(*it).second;
		tot++;
	}

	//std::cout<<tot<<std::endl;
	
	int ans=0;
	for(int i=0;i<tot;i++)
	{
		array[query[i]]=true;
		bool found=true;
	//	for(int j=0;j<s;j++) std::cout<<array[j]<<" ";
	//	cout<<std::endl;
		for(int j=0;j<s;j++)
		{
			if(array[j]!=true)
			{
				found=false;
				break;
			}
		}

		if(found)
		{
			++ans;
			for(int j=0;j<s;j++) array[j]=false;
			array[query[i]]=true;
		}
	}

	std::cout<<ans<<std::endl;
	return 0;
}

int main(void)
{
	int cases;
	int i=0;
	cin>>cases;
	while(cases)
	{
		++i;
		std::cout<<"Case #"<<i<<": ";
		main1();
		--cases;
	}
}

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) (i)=(c).begin();i!=(c).end();i++)
#define present(c,x) ((c).find(x)!=(c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;

typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<VVS> VVVS;

typedef pair<int,int> II;

typedef map<string, vector<string> > MSVS;

bool is_exist(MSVS pre,string key, string value)
{
	for(int i=0; i<pre[key].size(); i++)
	{
		if(pre[key][i].compare(value)== 0)
			return true;
	}
	return false;
}

void parse(MSVS& pre, string s)
{
	size_t first ;
	size_t  second;

	first = s.find("/");
	second = s.find("/",first+1);

	string temp, temp2;
	if(second!=string::npos)
	{
		temp = "/";
		temp2 = s.substr(0,(second));
		if(!is_exist(pre,temp,temp2))
				pre[temp].push_back(temp2);
			temp = temp2;
	}
	else
	{
		temp = "/";
		temp2 = s;
		if(!is_exist(pre,temp,temp2))
				pre[temp].push_back(temp2);
			temp = temp2;
			return;
	}

	while(1)
	{
		first = second;
		second = s.find("/",first+1);
		
		if(second!=string::npos)
		{
			temp2 = s.substr(0,(second));
			if(!is_exist(pre,temp,temp2))
				pre[temp].push_back(temp2);
			temp = temp2;
		}
		else
		{
			temp2 = s.substr(0);
			if(!is_exist(pre,temp,temp2))
				pre[temp].push_back(temp2);
			temp = temp2;
			return;
		}
	}
}

void my_print(MSVS& pre)
{
	for(MSVS::iterator it=pre.begin(); it!=pre.end(); it++)
	{
		string key = it->first;
		cout<<"key: "<<key<<endl;
		for(int i=0; i<it->second.size(); i++)
		{
			cout<<it->second[i]<<" ";
		}
		cout << endl;
	}
}
			
int process(MSVS& want, MSVS& pre)
{
	int ans = 0;

 for(MSVS::iterator (it)=(pre).begin();it!=(pre).end();it++)
 {
		string key = it->first;
		for(int i=0; i<it->second.size(); i++)
		{
			if(!is_exist(want,key,it->second[i]))
				ans++;
		}
	}
	return ans;
}
		
			

		


		



		



main()
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
	map<string,vector<string> > pre;
	map<string,vector<string> > want;

		cout <<"Case #"<<t<<": ";
		int N, M;
		cin>>N>>M;
		for(int i=0; i<N; i++)
		{
			string s;
			cin>>s;
			parse(pre,s);
		}

	//	cout<<"pre:"<<endl; //debug
	//	my_print(pre);//debug
		for(int j=0; j<M; j++)
		{
			string s;
			cin>>s;
			parse(want,s);
		}

	//	cout<<"want: "<<endl; //debug
	//	my_print(want); //debug
		cout<<process(pre,want)<<endl;
	}
}




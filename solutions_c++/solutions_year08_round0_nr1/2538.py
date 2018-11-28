#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("output.in");
vector<string> names;
vector<string> queries;
vector<vector<int> > v;
int memo[101][1001];
// q can be 0
int recurse(int e,int pos)
{
	if(e!=-1 && memo[e][pos]!=-1)
		return memo[e][pos];
	//if(queries.size()>1 && pos==queries.size()-1)
	//	return 1;
	int i,ans=10000,j,newpos;
	for(i=0;i<names.size();++i)
	{
		if(i==e || names[i]==queries[pos]) continue;
		bool found=0;
		for(j=0;j<v[i].size();++j)
			if(v[i][j]>pos)
			{
				newpos=v[i][j];
				found=true;
				break;
			}
		if(found)
		{
			//if(newpos==queries.size()-1)
			//	return 2;
			ans=min(ans,1+recurse(i,newpos));
		}
		else
		{
			if(e!=-1)
				memo[e][pos]=1;
			return 1;
		}
	}

	if(e!=-1)
		memo[e][pos]=ans;
	return ans;
}
int doit()
{
	if(queries.size()==0)
		return 0;
	int i,j,ans=100000;
	v.resize(names.size());
	for(i=0;i<names.size();++i)
		for(j=0;j<queries.size();++j)
		{
			if(queries[j]==names[i])
			{
				v[i].push_back(j);
			}
		}
	//for(i=0;i<names.size();++i)
	//{
		//if(names[i]!=queries[0])
		//{
		//	ans=min(ans,recurse(-1,0));
		//}
	//}
	ans=recurse(-1,0)-1;
	return ans;
	
}
int main()
{
	int n,i,s,q,j,k;
	char tmp[101];
	fin.getline(tmp,5);
	sscanf(tmp,"%d",&n);
	for(i=0;i<n;++i)
	{
		names.clear();
		v.clear();
		queries.clear();
		for(j=0;j<101;++j)
			for(k=0;k<1001;++k)
				memo[j][k]=-1;
		
		fin.getline(tmp,5);
		sscanf(tmp,"%d",&s);
		names.resize(s);
		for(j=0;j<s;++j)
		{
			
            fin.getline(tmp,101);
			names[j]=(string)tmp;
			//cout<<names[j]<<" "<<names[j].length()<<endl;
		}
		
		fin.getline(tmp,5);
		sscanf(tmp,"%d",&q);
		queries.resize(q);
		for(j=0;j<q;++j)
		{
			fin.getline(tmp,101);
			queries[j]=(string)tmp;
			//cout<<queries[j]<<" "<<queries[j].length()<<endl;
		}
		fout<<"Case #"<<(i+1)<<": "<<doit()<<endl;
	}
	return 0;
}
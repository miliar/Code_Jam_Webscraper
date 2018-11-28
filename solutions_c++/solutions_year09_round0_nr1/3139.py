#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std; 

int min(int a,int b) { if (a<b) return a; else return b;}
int l,d,n;
map<string,int> validSet;
vector<set<string> > cache(16);
//ostring = ordinary string
//bstring = bracketed string
vector<string> doit(string input)
{
  int start = input.find("(");
  int end = input.find(")");
	string ostring;
  if((start!=string::npos)&&(end!=string::npos))
	{
		if((int)start !=0)
			ostring = input.substr(0,start);
		else
			ostring = string("");

		string bstring = input.substr(start+1,end-start-1);
		vector<string> prefix(bstring.size());
		for(int i=0;i<bstring.size();i++)
		{
			prefix[i] = ostring;
			prefix[i].push_back(bstring[i]);
			////cout<<"\nprefix is "<<prefix[i];
		}
		if(end!=(input.size()-1))
		{
			vector<string>suffix = doit(input.substr(end+1,input.size()-end));
			vector<string>output;//(prefix.size()*suffix.size());
			int totalSize;
//			//cout<<"\ntotal size is "<<totalsize;
			for(int i=0;i<prefix.size();i++)
				for(int j=0;j<suffix.size();j++)
				{
					totalSize = prefix[i].size() + suffix[j].size();
					if(cache[totalSize].find(prefix[i]+suffix[j])!=cache[totalSize].end())
					{
						output.push_back(prefix[i]+suffix[j]);
						//cout<<"\nstring pushed is "<<prefix[i]+suffix[j];
					}
				}
			//cout<<"\noutput size is "<<output.size();
			return output;
		}
		else
		{
			//cout<<"\nprefix size is "<<prefix.size();
			return prefix;
		}
	}
	else
	{
		vector<string>output;
		output.push_back(input);
		//cout<<"\noutput size is "<<output.size();
//		for(int i=0;i<output.size();i++)
//			//cout<<"\n"<<output[i];
		return output;
	}
}

//fulllist flist
int compute(string input)
{
	int ans = 0;
	////cout<<"\ninside compute";
	map<string,int>::iterator it = validSet.begin();
	while(it!=validSet.end())
	{
		it->second = 0;
		it++;
	}
	vector<string> output = doit(input);
	for(int i=0;i<output.size();i++)
		//cout<<"\n"<<output[i];
	for(int i=0;i<output.size();i++)
	{
		if(validSet.find(output[i])!=validSet.end())
			validSet[output[i]] = 1;
	}

	it = validSet.begin();
	while(it!=validSet.end())
	{
		ans = ans + it->second;
		it++;
	}

	return ans;
}

int main()
{
	int ans =0;
	string valid,input;
	cin>>l>>d>>n;
	for(int i=0;i<d;i++)
	{
		cin>>valid;
		validSet[valid] = 0;
	}
	//cout<<"\nlog1 ";
	map<string,int>::iterator it = validSet.begin();
	for(int i=l;i>0;i--)
	{
		cache[i] = set<string>();
		it = validSet.begin();
		while(it!=validSet.end())
		{
			cache[i].insert((it->first).substr(l-i,i));
			it++;
		}
	}

	set<string>::iterator si ;
	for(int i=l;i>0;i--)
	{
		si = cache[i].begin();
		while(si!=cache[i].end())
		{
			//cout<<"\nl:str "<<i<<":"<<*si;
			si++;
		}
	}
	for(int i=0;i<n;i++)
	{
		cin>>input;
		ans = compute(input);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

}

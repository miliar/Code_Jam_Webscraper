#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	string gg = "gg";
	int t;
	cin>>t;
	for(int tt=0; tt<t; tt++)
	{
		map<string, string> tr;
		vector<string> vec;
		int n;
		cin>>n;
		string s;
		for(int i=0; i<n;i++)
		{
			cin>>s;
			gg[0] = s[0];
			gg[1] = s[1];
			tr[gg] = s[2];
			gg[0] = s[1];
			gg[1] = s[0];
			tr[gg] = s[2];
		}
		cin>>n;
		for(int i=0; i<n; i++)
		{
			cin>>s;
			vec.push_back(s);
			gg[0] = s[1];
			gg[1] = s[0];
			vec.push_back(gg);
		}
		cin>>n;
		cin>>s;
		string res = "";
		for(int i=0; i<s.length(); i++)
		{
			res+=s[i];
			if (res.length()>1)
			{
				if (tr.count(res.substr(res.length()-2,2)))
				{
					string temp = tr[res.substr(res.length()-2,2)];
					res = res.substr(0, res.length()-2) + temp;
				}
				for (int j=0; j<vec.size(); j++)
				{
					if (res=="") break;
					if (res[res.length()-1]==vec[j][0])
						for(int k=0; k<res.length()-1; k++)
							if (res[k]==vec[j][1])
							{
								res = "";
								break;
							}
				}
			}
		}
		cout<<"Case #"<<tt+1<<": [";
		for(int i=0; i<res.length(); i++)
		{
			cout<<res[i];
			if (i!=res.length()-1) cout<<", ";
		}
		cout<<"]"<<endl;
	}
	return 0;
}
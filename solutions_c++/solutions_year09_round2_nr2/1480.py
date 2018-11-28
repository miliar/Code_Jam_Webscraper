# include <iostream>
# include <vector>
# include <string>
# include <algorithm>
using namespace std;
int fact(int num)
{
	if(num==0 || num==1)
		return 1;
	else
		return num*fact(num-1);
}

int main()
{
	int t,caseg;
	string res;
	cin>>t;
	for(caseg=1;caseg<=t;caseg++)
	{
		string str,given,rev;
		vector<string>vecneed;
		cin>>str;
		given=str;
		sort(str.begin(),str.end());
		reverse(str.begin(),str.end());
		rev=str;
		sort(str.begin(),str.end());
		int cnt=0;
		int found=0;
		int last=0;
		do
		{
			if(given==rev)
			{
			 last=1;
			 break;
			}
			if(str==given)
			{
				next_permutation(str.begin(),str.end());
				res=str;
				found=1;
				break;
			}
			vecneed.push_back(str);
			cnt++;
		}while(next_permutation(str.begin(),str.end()));
		char ch='0';
		while(!found)
		{
			int i;
			sort(given.begin(),given.end());
			str.clear();
			for(i=0;i<given.size();i++)
			{
				if(given[i]=='0')
					continue;
				str+=given[i];
			}
			int need=(given.size()-str.size())+1;
			for(i=1;i<=need;i++)
			{
					str.insert(str.begin()+i,ch);
			}
			found=1;
			res=str;
		}
		cout<<"Case #"<<caseg<<": "<<res<<endl;
	}
	return 0;
}










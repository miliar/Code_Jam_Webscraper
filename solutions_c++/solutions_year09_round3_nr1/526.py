#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dig[] = {1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64};
int map[512];
bool used[512];
vector<int> num;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int cnt=0;

		memset(map,0,sizeof(map));
		memset(used,0,sizeof(used));
		
		string s;
		num.clear();
		cin>>s;
		
		for(int j=0;j<s.size();j++)
		{
			if(used[s[j]])
			{
				num.push_back(map[s[j]]);	
			}
			else
			{
				used[s[j]]=1;
				map[s[j]]=dig[cnt++];	
				num.push_back(map[s[j]]);
			}
		}
		
		unsigned long long base = dig[cnt];
		base = max(base,2ULL);
		unsigned long long ans=0;
		
		for(int j=0;j<num.size();j++)
		{
	//		cout<<num[j];
				ans*=base;
				ans+=num[j];
		}
	//	cout<<endl;
		cout<<"Case #"<<i<<": "<<ans<<endl;
		
	}	
	
}

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;
#define TEST 0

void Convert(long long Number,long long toBase,vector<int>& toRet )
{
	while(Number!=0)
	{
		toRet.insert(toRet.begin(),Number%toBase);
		Number/=toBase;
	}
}
int main()
{
	int T;
#if TEST == 0
	ifstream cin("A-small.in");
	ofstream cout("A-small.out");
#endif
	cin>>T;
	cin.get();
	for(int kk=1;kk<=T;kk++)
	{
		vector<int> bases;
		string str;
		getline(cin,str,'\n');
		stringstream strm(str);
		while(strm.peek()!=-1)
		{
			int tmp;
			strm>>tmp;
			bases.push_back(tmp);
		}
		int i;
		for(i=2;;i++)
		{
			bool flag2=true;
			for(int j=0;j<bases.size();j++)
			{
				long long num=i;
				bool flag=false;
				vector<long long> nums;
				
				while(1)
				{
					vector<int> tmp;
					nums.push_back(num);					
					Convert(num,bases[j],tmp);
					num=0;
					for(int k=0;k<tmp.size();k++)
						num+=tmp[k]*tmp[k];
					if(num==1)
					{
						flag=true;
						break;
					}
					else if(find(nums.begin(),nums.end(),num)!=nums.end())
					{	
						break;
					}
				}

				if(!flag)
				{
					flag2=false;
					break;
				}
			}
			if(flag2)
				break;
		}
		cout<<"Case #"<<kk<<": "<<i<<endl;
	}
	return 0;
}
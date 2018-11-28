#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
int casenum=1;
using namespace std;

bool taa()
{
vector<int> ta,tb,aa,ab;
	int turnaround;
	cin>>turnaround;
	int tempa,tempb,temp;
	cin>>tempa>>tempb;
	string s1,s2;
	for(int i=0;i<tempa;i++)
	{
		cin>>s1>>s2;
		temp=atoi(s1.substr(0,2).c_str())*60+atoi(s1.substr(3,2).c_str());
		ta.push_back(temp);
		temp=atoi(s2.substr(0,2).c_str())*60+atoi(s2.substr(3,2).c_str())+turnaround;
		ab.push_back(temp);

	}
	for(int i=0;i<tempb;i++)
	{
		cin>>s1>>s2;
		tempa=atoi(s1.substr(0,2).c_str())*60+atoi(s1.substr(3,2).c_str());
		tb.push_back(tempa);
		tempa=atoi(s2.substr(0,2).c_str())*60+atoi(s2.substr(3,2).c_str())+turnaround;
		aa.push_back(tempa);
	}
	sort(ta.begin(),ta.end());
	sort(tb.begin(),tb.end());
	sort(aa.begin(),aa.end());
	sort(ab.begin(),ab.end());
	for(int i=0;i<ta.size();i++)
	{
		for(int j=0;j<aa.size();j++)
		{
			if(ta[i]>=aa[j] && aa[j]!=-1 )
			{
				ta[i]=-1;
				aa[j]=-1;
				break;
			}
		}
	}
	int ret=0;
	for(int i=0;i<ta.size();i++)
	  if(ta[i]!=-1)
		  ret++;
	cout<<"Case #"<<casenum++<<": "<<ret<<" ";
	for(int i=0;i<tb.size();i++)
	{
		for(int j=0;j<ab.size();j++)
		{
			if(tb[i]>=ab[j]&& ab[j]!=-1 )
			{
				tb[i]=-1;
				ab[j]=-1;
				break;
			}
		}
	}
	ret=0;
	for(int i=0;i<tb.size();i++)
	  if(tb[i]!=-1)
		  ret++;
	cout<<ret<<endl;
return 1;
}
int main()
{
	int tt;
	cin>>tt;
	for(int i=0;i<tt;i++)
		taa();
	return 0;
}
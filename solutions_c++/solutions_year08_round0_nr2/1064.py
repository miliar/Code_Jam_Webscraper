#include<iostream>
#include<map>
#include<algorithm>
using namespace std;
map<int,int> tt1,tt2;
map<int,int>::iterator it;
struct trip
{
	int st;
	int en;
	int fs;
}tr[200];
bool lesss(trip a,trip b)
{
	if(a.st<b.st)return 1;
	return 0;
}
int main()
{
	int n,t,na,nb,i,res1,res2,flag=1;
	char temp[6];
	cin>>n;
	while(n--)
	{
		res1=res2=0;
		cin>>t>>na>>nb;
		for(i=0;i<na;i++)
		{
			cin>>temp;
			tr[i].st=(temp[0]-'0')*600+(temp[1]-'0')*60+(temp[3]-'0')*10+temp[4]-'0';
			cin>>temp;
			tr[i].en=(temp[0]-'0')*600+(temp[1]-'0')*60+(temp[3]-'0')*10+temp[4]-'0';
			tr[i].fs=1;
		}
		for(;i<nb+na;i++)
		{
			cin>>temp;
			tr[i].st=(temp[0]-'0')*600+(temp[1]-'0')*60+(temp[3]-'0')*10+temp[4]-'0';
			cin>>temp;
			tr[i].en=(temp[0]-'0')*600+(temp[1]-'0')*60+(temp[3]-'0')*10+temp[4]-'0';
			tr[i].fs=2;
		}
		sort(tr,tr+na+nb,lesss);
		tt1.clear();tt2.clear();
		for(i=0;i<na+nb;i++)
		{
			if(tr[i].fs==1)
			{
				if(tt1.size()==0||tt1.begin()->first>tr[i].st)
				{
					res1++;
				}
				else
				{
					if(tt1.begin()->second==1)tt1.erase(tt1.begin());
					else tt1.begin()->second--;
				}
				it=tt2.find(tr[i].en+t);
				if(it!=tt2.end())tt2[tr[i].en+t]++;
				else tt2[tr[i].en+t]=1;
			}
			else
			{
				if(tt2.size()==0||tt2.begin()->first>tr[i].st)
				{
					res2++;
				}
				else
				{
					if(tt2.begin()->second==1)tt2.erase(tt2.begin());
					else tt2.begin()->second--;
				}
				it=tt1.find(tr[i].en+t);
				if(it!=tt1.end())tt1[tr[i].en+t]++;
				else tt1[tr[i].en+t]=1;
			}
		}
		cout<<"Case #"<<flag++<<": "<<res1<<" "<<res2<<endl;
	}
	return 0;
}

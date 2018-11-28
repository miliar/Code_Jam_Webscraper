#include<iostream>
#include<vector>
using namespace std;
typedef pair<int,int> PI;
int conv(string s)
{
	int hr=(s[0]-'0')*10+s[1]-'0';
	int min=(s[3]-'0')*10+s[4]-'0';
	return hr*60+min;
}
int main()
{
	int t,Case=1;
	cin>>t;
	while(t--)
	{
		int time,na,nb,cnta=0,cntb=0;;
		cin>>time;
		vector<int> depta,deptb,arra,arrb;
		cin>>na>>nb;
		string temp;
		for(int i=0;i<na;i++)
		{	cin>>temp;
			depta.push_back(conv(temp));
			cin>>temp;
			int ttt=conv(temp)+time;
			arrb.push_back(ttt);
		}
		for(int i=0;i<nb;i++)
		{	cin>>temp;
			deptb.push_back(conv(temp));
			cin>>temp;
			int ttt=conv(temp)+time;
			arra.push_back(ttt);
		}
		sort(depta.begin(),depta.end());
		sort(arra.begin(),arra.end());
		sort(deptb.begin(),deptb.end());
		sort(arrb.begin(),arrb.end());
		vector<int>::iterator it;
		for(int i=0;i<na;i++)
		{	int req=depta[i];
			int found=0;
			for(it=arra.begin();!found && it!=arra.end();it++)
			{
				int s=*it;
				if(req>=s)
				{	found=1;
					arra.erase(it);
				}
			}	
			if (!found)	cnta++;
		}
		for(int i=0;i<nb;i++)
		{
			int req=deptb[i];
			int found=0;
			for(it=arrb.begin();!found && it!=arrb.end();it++)
			{
				int s=*it;
				if(req>=s)
				{	found=1;
					arrb.erase(it);
				}
			}	
			if (!found)	cntb++;
		}
		cout<<"Case #"<<Case++<<": "<<cnta<<" "<<cntb<<endl;
	}
}


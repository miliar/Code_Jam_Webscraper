#include<iostream>
#include<vector>
using namespace std;
int main()
{
	long n,p,r,t,bt,cnt=0,cur_jobO,cur_jobB,cur_posO,cur_posB,flag,i,cnt_c=0,fg;
	char c;
	vector<pair<long,long> > o,b;
       	cin>>t;
	while(t--)
	{
		cnt_c++;
		o.clear();
		b.clear();
		cnt=0;
		cin>>n;
		vector<long> chk;
		for(i=0;i<=n;i++)
			chk.push_back(i);
		while(n--)
		{
			cin>>c;
			cin>>bt;
			cnt++;
			if(c=='O')
			{
				o.push_back(make_pair(bt,cnt));
			//	cout<<"O "<<bt<<" "<<cnt<<endl;
			}
			else
			{
				b.push_back(make_pair(bt,cnt));
			//	cout<<"B "<<bt<<" "<<cnt<<endl;
			}
		}
		//input done
		cnt=0;
		cur_jobO=0;
		cur_jobB=0;
		cur_posO=1;
		cur_posB=1;
		while(1)
		{
			cnt++;
			fg=1;
			if(cur_jobO<o.size())
			{
			if(cur_posO==o[cur_jobO].first && chk[o[cur_jobO].second-1]==0)
			{
				chk[o[cur_jobO].second]=0;
				cur_jobO++;
				fg=0;
			//	cout<<"O completed "<<cur_jobO<<endl;
			}
			else if(cur_posO<o[cur_jobO].first)
			{
				cur_posO++;
			//	cout<<"O moved to "<<cur_posO<<endl;
			}
			else if(cur_posO>o[cur_jobO].first)
			{
				cur_posO--;
			}
			else if(cur_posO==o[cur_jobO].first && chk[o[cur_jobO].second-1]!=0)
			{
			//	cout<<"O staying at "<<cur_posO<<endl;
			}
			}
			//now for B
			if(cur_jobB<b.size())
			{
		
				if(cur_posB==b[cur_jobB].first && chk[b[cur_jobB].second-1]==0)
			{
				if(fg==1 || (fg==0 && o[cur_jobO-1].second>b[cur_jobB].second))
				{
				chk[b[cur_jobB].second]=0;
				cur_jobB++;
			//	cout<<"B completed "<<cur_jobB<<endl;
				}
			}
			else if(cur_posB<b[cur_jobB].first)
			{
				cur_posB++;
			//	cout<<"B moved to "<<cur_posB<<endl;
			}
			else if(cur_posB>b[cur_jobB].first)
			{
				cur_posB--;
			}
			else if(cur_posB==b[cur_jobB].first && chk[b[cur_jobB].second-1]!=0)
			{
			//	cout<<"B staying at "<<cur_posB<<endl;
			}
			}
			flag=0;
			for(i=0;i<chk.size();i++)
				if(chk[i]!=0)
					flag=1;
			if(flag==0)
				break;

		}
		cout<<"Case #"<<cnt_c<<": "<<cnt<<endl;
		
	}	
}

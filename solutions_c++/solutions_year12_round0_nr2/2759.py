#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	vector<int> ent,max;
	int m,out,t,n,s,p,j,i,val;
	cin>>t;
	j=0;
	while(j++<t)
	{
		cin>>n>>s>>p;
//		cout<<n<<" "<<s<<" "<<" "<<p<<" ";
		out=0;
		max.clear();
		ent.clear();
		while(n--)
		{
			cin>>val;
//			cout<<val<<" ";
			ent.push_back(val);
		}
		sort(ent.begin(),ent.end());
//		for(i=0;i<ent.size();i++)
//			cout<<ent[i]<<" ";
		for(i=0;i<ent.size();i++)
		{
			if(ent[i]%3==0)
			{
				m=ent[i]/3;
				if(m<9 && s>0 && m!=0)
				{
					if((m+1)>=p)
					{
						m+=1;
						s--;
					}
				}
			}
			else if(ent[i]%3==1)
			{
				m=(ent[i]-1)/3 +1;
			}
			else
			{
				m=(ent[i]-2)/3 + 1;
				if(m<10 && s>0)
				{
					if((m+1)>=p)
					{
						m++;
						s--;
					}
				}
			}
			if(m>=p)out++;
		}
		cout<<"Case #"<<j<<": "<<out<<"\n";
	}
	return 0;
}

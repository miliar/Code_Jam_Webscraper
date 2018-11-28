#include <fstream>
#include <stack>
#include <vector>
#include <map>
#include <cmath>
#define LL long long
using namespace std;
LL get_circle(map<LL,LL> &dp,map<LL,LL> &dpj,LL i,LL N)
{
	LL end=i;
	LL cnt=0;
	cnt=dp[i];
	i=(i+dpj[i])%N;
	while(i!=end)
	{
		cnt+=dp[i];
		i=(i+dpj[i])%N;
	}
	return cnt;
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	LL T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		LL R,k,N;
		cin>>R>>k>>N;
		vector<LL> g(N,0),t;
		map<LL,LL> str;
		map<LL,LL> num;
		for(LL i=0;i<N;i++)
		{
			cin>>g[i];
		}
		t=g;
		g.insert(g.end(),t.begin(),t.end());
		LL cnt=0;
		LL Tcnt;
		LL i_=0;
		map<LL,LL> dp,dpj,dpc;
		vector<LL> circle;
		int count=0;
		while(R)
		{
			count++;
			if(dp.find(i_)!=dp.end())
			{
				int tmp=count-dpc[i_];
				if(R/tmp==0)
				{
					cnt+=dp[i_];
					circle.push_back(cnt);
					i_=(i_+dpj[i_])%N;
					R--;
				}
				else
				{	
					cnt=cnt+R/tmp*get_circle(dp,dpj,i_,N);
					circle.push_back(cnt);
					R=R%tmp;
				}
			}
			else
			{
				Tcnt=0;
				LL j=0;
				for(;j<N;j++)
					if(Tcnt+g[i_+j]<=k)
					{
						Tcnt+=g[i_+j];
					}
					else break;
				cnt+=Tcnt;
				dp[i_]=Tcnt;
				dpj[i_]=j;
				dpc[i_]=count;
				i_=(i_+j)%N;
				circle.push_back(cnt);
				R--;	
			}
		}
		cout<<"Case #"<<ti<<": ";
		cout<<cnt<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}


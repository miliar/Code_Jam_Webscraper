#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;
typedef vector<int> vint;
typedef vector< pair<int,int>  > vint2;
int main()
{

	freopen("C-small-attempt2.in.txt","r",stdin);
	freopen("C-small-attempt2.txt","w",stdout);


	vint g;
	
	vint2 vtab1;

	map<int,int> vtab2;


	

	int N=0;
	int caseNow=0;
	cin>>N;
	while(N-->0)
	{
		caseNow++;
		int gainsum=0;
		vtab2.clear();
		vtab1.clear();
		g.clear();
		int R=0,k=0,nn=0;
		cin>>R>>k>>nn;
	
		for(int i=0;i<nn;++i)
		{
			int temp=0;
			cin>>temp;
			g.push_back(temp);
		}
		int pos=0;
	

		int circleRound=0;
		int circleGain=0;
		int circleStartRound=0;
		int circleStartGain=0;
		while (1)
		{
			int sum=0;
			int posOrg=pos;
			while (sum+g[pos] <=k)
			{
				sum+=g[pos++];
				if(pos>=g.size())
					pos%=g.size();

				if( (pos+g.size()-posOrg)% g.size()==0 )
				{
					break;
				}
				
			}
			vtab1.push_back(make_pair(pos,sum));
			circleRound++;
			
			circleGain+=sum;

			if(R==circleRound)
			{
				gainsum=circleGain;
				R=0;
				break;

			}

			if(vtab2.find(pos)==vtab2.end())
			{
				vtab2[pos]=vtab1.size()-1;
			}
			else
			{
				int circlestart=vtab2[pos];
				for(int i=0;i<=circlestart;++i)
				{
					circleStartRound++;
					circleRound--;
					circleStartGain+=vtab1[i].second;
					circleGain-=vtab1[i].second;
				}
				break;
			}
		}

		R-=circleStartRound;
		gainsum+=circleStartGain;
		int kk=R/circleRound;
		R%=circleRound;
		gainsum+=(kk*circleGain);
		for(int i=0;i<R;++i)
		{
			gainsum+=vtab1[(circleStartRound+i)%vtab1.size()].second;
		}

		cout<<"Case #"<<caseNow<<": "<<gainsum<<endl;
	}


}
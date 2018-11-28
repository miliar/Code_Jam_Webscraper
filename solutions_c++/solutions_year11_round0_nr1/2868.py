#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef pair<char,int> PCI;

const int MAXN=105;
int t,n;
vector<int> O,B;
vector<PCI> seq;
int dpo[MAXN],dpb[MAXN];

inline int ABS(int x) { return x>0?x:-x; }

void process()
{
	memset(dpo,0,sizeof(dpo));
	memset(dpb,0,sizeof(dpb));

	int o=1,b=1;
	int olast=0,blast=0;
	for(vector<PCI>::const_iterator itr=seq.begin() ;itr!=seq.end() ;
		itr++)
	{
		if(itr->first=='O')
		{
			dpo[itr->second]=dpo[o]+1;
			if(ABS(o-itr->second)>=blast)
			{
				dpo[itr->second]+=ABS(o-itr->second);
				olast+=ABS(o-itr->second)-blast;
			}
			else
			{
				dpo[itr->second]=dpb[b]+1;
			}
			
			olast++;
			blast=0;
			o=itr->second;
		}
		else 
		{
			dpb[itr->second]=dpb[b]+1;
			if(ABS(b-itr->second)>=olast)
			{
				dpb[itr->second]+=ABS(b-itr->second);
				blast+=ABS(b-itr->second)-olast;
			}
			else
			{
				dpb[itr->second]=dpo[o]+1;
			}
			
			olast=0;
			blast++;
			b=itr->second;
		}
	}
	//printf("seq.back().first = %d\n",seq.back().second);
	if(seq.back().first=='O')
		printf("%d\n",dpo[seq.back().second]);
	else
		printf("%d\n",dpb[seq.back().second]);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas=1;

	cin>>t;
	while(t--)
	{
		O.clear();
		B.clear();
		seq.clear();

		cin>>n;
		for(int i=0 ;i<n ;i++)
		{
			char hallway;scanf(" %c",&hallway);
			int pos;cin>>pos;

			seq.push_back(make_pair(hallway,pos));
			if(hallway=='O')
			{
				O.push_back(pos);
			}
			else
			{
				B.push_back(pos);
			}
		}
		printf("Case #%d: ",cas++);
		process();
	}
}
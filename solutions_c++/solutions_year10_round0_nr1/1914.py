#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
vector<int> plugs;
int main()
{ 
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
	int n;int k;
	int t;
	scanf("%d",&t);
	string plugs;
	bool owned;
	for(int i=0;i<t;i++)
	{
	  owned=false;
	  plugs.clear();
      scanf("%d %d",&n,&k);
	  int cur=1;
	  for(int j=0;j<n;j++)cur*=2;
	  n=n%(cur);
	  
	  while(k)
	  {
        plugs.push_back(k%2);
		k/=2;
	  }
	  if(plugs.size()<n)
	  {
		  printf("Case #%d: OFF\n",i+1);
		   owned=true;
		  continue;
	  }
	  else
	  {
        for(int j=0;j<n;j++)
		{
			if(plugs[j]==0)
			{
				printf("Case #%d: OFF\n",i+1);
				owned=true;
				break;
			}
		}
	  }
	  if(!owned)printf("Case #%d: ON\n",i+1);

	}
	

}
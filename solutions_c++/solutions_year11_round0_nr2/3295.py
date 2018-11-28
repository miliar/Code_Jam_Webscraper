#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>

#define PB push_back
#define M 100
#define N 100
#define LL long long


using namespace std;





int main()
{
	
	int tc,ti;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		int cc,oc,anslen,i,j,k,ilen,des;
		string ans;
		char combs[50][5],opps[50][5],input[200];
		char comb_array[256][256],opp_array[256][256],ch1,ch2,ch3,ch;
		memset(comb_array,0,sizeof(comb_array));
		memset(opp_array,0,sizeof(opp_array));
		scanf("%d",&cc);
		for(i=0;i<cc;++i)
		{
			scanf("%s",combs[i]);
			ch1=combs[i][0];
			ch2=combs[i][1];
			ch3=combs[i][2];
			comb_array[ch1][ch2]=ch3;
			comb_array[ch2][ch1]=ch3;
		}
		
		scanf("%d",&oc);
		for(i=0;i<oc;++i)
		{
		
		scanf("%s",opps[i]);
		ch1=opps[i][0];
			ch2=opps[i][1];
			
			opp_array[ch1][ch2]=1;
			opp_array[ch2][ch1]=1;
		}
		
		scanf("%d",&ilen);
		scanf("%s",input);
		
		ans="";
		ans+=input[0];
		anslen=1;
		for(i=1;i<ilen;++i)
		{
			ch1=ans[anslen-1];
			ch2=input[i];
			ch=comb_array[ch1][ch2];
			if(ch!=0)
			{
				ans[anslen-1]=ch;
				
			} else {
				des=0;
				for(j=0;j<anslen;++j)
				{
					ch1=ans[j];
					if(opp_array[ch1][ch2])
					{
						des=1;
						break;
					}
				}
				if(des)
				{
					ans="";
					anslen=0;
				} else {
					ans+=input[i];
					anslen++;
				}
			}
		}
		string format_ans="[";
		if(anslen!=0)
		{
			format_ans+=ans[0];
		}
		for(i=1;i<anslen;++i)
		{
			format_ans+=", ";
			format_ans+=ans[i];
		}
		format_ans+=']';
		
		cout<<"Case #"<<ti<<": "<<format_ans<<endl;
		
	}
	
	
	return 0;
}

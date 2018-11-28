#include<iostream>
#define MAXN 10
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
    	int n;
    	char s[MAXN][MAXN];	//schedule
    	float wp[MAXN],owp[MAXN],oowp[MAXN];
   		int played[MAXN];
   		int win[MAXN];
    	cin>>n;
    	for(int i=0;i<n;i++)
    	{
    		cin>>s[i];
    		win[i]=0;
    		played[i]=0;
    		for(int j=0;j<n;j++)
    		{
    			if(s[i][j]=='1')
    			{
    				win[i]++;
    				played[i]++;
    			}
    			else if(s[i][j]=='0')
    			{
    				played[i]++;
    			}
    		}
    		if(played[i]!=0)
    		{
    			wp[i]=(float)win[i]/played[i];
    			//cout<<"wp["<<i<<"] = "<<wp[i]<<endl;
    		}
    		else
    		{
    			wp[i]=0;
    			owp[i]=0;
    			oowp[i]=0;
    		}
    	}
    	//owp
   		float sum=0;
    	for(int i=0;i<n;i++)
    	{
    		sum=0;
    		owp[i]=0;
			if(played[i]!=0)
			{
				for(int j=0;j<n;j++)
				{
					if(s[j][i]=='1')
					{
						if(played[j]!=1)
							sum+=(float)(win[j]-1)/(played[j]-1);
					}
					else if(s[j][i]=='0')
					{
						if(played[j]!=1)
						sum+=(float)(win[j])/(played[j]-1);
					}
				}
				owp[i]=sum/played[i];
				//cout<<"owp["<<i<<"] = "<<owp[i]<<endl;
			}
    	}
    	//oowp
    	for(int i=0;i<n;i++)
    	{
    		sum=0;
    		oowp[i]=0;
			if(played[i]!=0)
			{
				for(int j=0;j<n;j++)
				{
					if(s[i][j]!='.')
					{
						sum+=owp[j];
					}
				}
				oowp[i]=sum/played[i];
				//cout<<"oowp["<<i<<"] = "<<oowp[i]<<endl;
			}
    	}
    	cout<<"Case #"<<x<<":\n";
    	for(int i=0;i<n;i++)
    	{
    		cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
    	}
    }
}

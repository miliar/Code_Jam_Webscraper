#include<iostream>
#include<vector>
using namespace std;

char datain[110][110];
double ans[110];
int main()
{
	int T;
	int n;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		cin>>n;
		for(int j=0;j<n;++j)
		{
			cin>>datain[j];
		}
		memset(ans,0,sizeof(ans));
		double WP[110],OWP[110],OOWP[110];
		for(int j=0;j<n;++j)
		{
			int a=0,b=0;
			for(int t=0;t<n;++t)
			{
				if(datain[j][t]=='1')
				{
					++a;
				}
				else if(datain[j][t]=='0')
				{
					++b;
				}
			}
			WP[j]=(double)a/(double)(a+b);
		}
		for(int j=0;j<n;++j)
		{
			vector<int> tmpIndex;
			for(int t=0;t<n;++t)
			{
				if(datain[j][t]!='.')
				{
					tmpIndex.push_back(t);
				}
			}
			//²»¼ÆjÁÐ
			double tmpWP[110];
			for(int k=0;k<tmpIndex.size();++k)
			{
				int a=0,b=0;
				for(int t=0;t<n;++t)
				{
					if(datain[tmpIndex[k]][t]=='1'&&t!=j)
					{
						++a;
					}
					else if(datain[tmpIndex[k]][t]=='0'&&t!=j)
					{
						++b;
					}
				}
				tmpWP[tmpIndex[k]]=(double)a/(double)(a+b);
			}
			OWP[j]=0;
			for(int k=0;k<tmpIndex.size();++k)
			{
				OWP[j]+=tmpWP[tmpIndex[k]];
			}
			OWP[j]/=tmpIndex.size();
		}
		//cout<<"**OWP"<<endl;
		//for(int j=0;j<n;++j)
		//{
		//	cout<<OWP[j]<<endl;
		//}
		//cout<<"*****"<<endl;
		//OOWP[1..n];
		memset(OOWP,0,sizeof(OOWP));
		for(int j=0;j<n;++j)
		{
			//OOWP[j];
			int count=0;
			for(int t=0;t<n;++t)
			{
				if(datain[j][t]!='.')
				{
					OOWP[j]+=OWP[t];
					++count;
				}
			}
			OOWP[j]/=count;
		}
		/*cout<<"**OOWP"<<endl;
		for(int j=0;j<n;++j)
		{
			cout<<OOWP[j]<<endl;
		}
		cout<<"*****"<<endl;*/
		for(int j=0;j<n;++j)
		{
			ans[j]=0.25*WP[j]+0.5*OWP[j]+0.25*OOWP[j];
		}
		printf("Case #%d:\n",i);
		for(int j=0;j<n;++j)
		{
			cout<<ans[j]<<endl;
		}

	}
	return 0;
}
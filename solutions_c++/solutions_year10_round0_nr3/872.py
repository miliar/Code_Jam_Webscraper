#include<iostream>
#include<vector>
#define pb push_back
#include<set>


using namespace std;
 int  main()
{
	long long int  t;
	//scanf("%d",&t);
	cin>>t;
	long long int  hehe=0;
	while(t--)
	{
		hehe++;
		long long int  r,k,n;
		cin>>r>>k>>n;
		vector<long long int >v;
		for(long long int  i=0;i<n;i++)
		{
			long long int  kk;
			cin>>kk;
			v.pb(kk);
		}
		long long int  ct=0;
		set<vector<long long int > >s;
		vector<vector<long long int > >vv;
		bool bb=0;
		long long int  R=r;
	//	s.insert(v);
		vv.pb(v);
		vector<long long int >anss;
		while(1)
		{
				long long int  sum=0;
				long long int  limit=0;
				while(1)
				{
					limit++;
					
					if(sum + v[0] > k)break;
					sum+=v[0];
					v.pb(v[0]);
					
					v.erase(v.begin());
					if(limit==v.size())break;
					
				}
				
				//cout<<"dsadas"<<endl;
			//cout<<v.size()<<endl;
				 int  kkk=(int )s.size();
					s.insert(v);
					
					vv.pb(v);
					anss.pb(sum);
					if(kkk==(int )s.size())
					{
					  
						bb=1;
						break;
					}	
					
					
				
				
		
		}
		
		if(bb==0)
		{
		 cout<<"Case #"<<hehe<<": "<<ct<<endl;
		}
		else
		{
		//cout<<vv.size()<<endl;
		//cout<<anss.size()<<endl;
		    long long int key=0;
		for(int i=0;i<vv.size();i++)
		{
			if(vv[i]==vv[vv.size()-1]){ key=i;break;}
		}	
			//cout<<"key  "<<key<<endl;
			
				vector<long long int>ans1;
				vector<long long int>ans2;
				for(int i=0;i<key;i++)
				{
					ans1.pb(anss[i]);
				}	
				for(int i=key;i<anss.size();i++)
				{
					ans2.pb(anss[i]);
				}	
				long long int ppp=0;
				//cout<<ans1.size()<<"  "<<ans2.size()<<endl;
				
				long long int ans=0;
				long long int yy=ans1.size();
				if(yy >=R)yy=R;
				 for(int i=0;i<yy;i++)ans+=ans1[i];
				 ppp=ans;
				if(R<=ans1.size())
				{
				 
				 cout<<"Case #"<<hehe<<": "<<ans<<endl;
				 }
				 else
				 {
				 R-=ans1.size();
;				long long int  qqq=0;
				for(long long int  i=0;i<ans2.size();i++)
				{
					qqq+=ans2[i];
				}
				
			long long int  k2=(R)/ans2.size();
		    long long int  k1=(R)%ans2.size();
			long long int  qq=0;
			for(long long int  i=0;i<k1;i++)
			{
			qq+=ans2[i];
			}
			cout<<"Case #"<<hehe<<": "<<qqq*k2 + qq + ppp<<endl;
			}
			}
				
		
		}
		
		
	return 0;
}	
		
				
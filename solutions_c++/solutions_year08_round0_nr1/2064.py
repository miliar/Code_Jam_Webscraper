#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 

int main()
{
	int t,q,s,cnt[101];
	string eng[101],qu[1001];
	cin>>t;
	FOR(tt,1,t)
	{
		cin>>s;
		getline(cin,eng[0]);
		FOR(i,0,s-1)
		{
			getline(cin,eng[i]);
		}
		cin>>q;
		getline(cin,qu[0]);
		FOR(i,0,q-1)
		{		
			getline(cin,qu[i]);
		}
	
		cout<<"Case #"<<tt<<": ";
		if(q==0)
		{
			cout<<"0";
			if(tt<(t))
				cout<<endl;
			continue;
		}
			
		int ans=0;
		int start=0,flag=0;
		int pos[101];
/*		while(1)
		{			
			int mmin=9999;
			int mn=0;
			FOR(i,0,s-1)
			{
				cnt[i]=0;
				FOR(j,start,q-1)
				{	
					if(eng[i]==qu[j])
						cnt[i]++;
				}	
				if(cnt[i]==0)
				{
					flag=1;
					break;
				}
				if(mmin>cnt[i])
				{
					mmin=cnt[i];
					mn=i;
				}
			}
			if(flag==1)
				break;
			FOR(i,start,q-1)
			{
				if(eng[mn]==qu[i])
				{
					start=i+1;
					break;
				}
			}
			ans++;
		}*/

		int mx=-1,prev=-1;
		while(1)
		{			
			int mmax=-1;
//			int mmin=9999;
//			int mn=0;
			FOR(i,0,s-1)
			{
				if(i!=prev)
				{
					pos[i]=-1;
					FOR(j,start,q-1)
					{	
						if(eng[i]==qu[j])
						{
							pos[i]=j;
							break;
						}
					}		
					if(pos[i]==-1)
					{
						flag=1;
						break;
					}
					if(mmax<pos[i])//cnt[i])
					{
						mmax=pos[i];
						mx=i;
					}
				}
			}
			if(flag==1)
				break;
/*			FOR(i,start,q-1)
			{
				if(eng[mn]==qu[i])
				{
					start=i+1;
					break;
				}
			}
*/			start=pos[mx]+1;
			prev=mx;
			ans++;
		}

		cout<<ans;
		if(tt<(t))
			cout<<endl;		
	}
	return 0;
}

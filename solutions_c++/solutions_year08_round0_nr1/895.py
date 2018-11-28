#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;


int main()
{
	int t,num=0;

	//cin>>t;
	scanf("%d\n",&t);	
	while (num++ < t)
	{		
		map<string,int> s1;
		int a[1002],ind[102],n,m,ans=0,ql=0,qr=0,cur_ind,cur_ser;
		vector<int>b[102];
		string s;
		
		memset(a,0,sizeof(a));
		memset(ind,0,sizeof(ind));
		for(int i=0;i<102;i++)
		{
			b[i].clear();
			b[i].push_back(-1);
		}

		//cin>>n;
		scanf("%d\n",&n);
		//deb(n);
		for(int i=0;i<n;i++)
		{
			getline(cin, s);
		//	deb(s);
			s1[s] = i;
		}
		//cin>>m;
		scanf("%d\n",&m);
		//deb(m);
		for(int i=0;i<m;i++)
		{
			getline(cin, s);
		//	deb(s);
			a[i]=s1[s];
		//	deb(a[i]);
			b[a[i]].push_back(i);
		}
		for(int i=0;i<n;i++)
		{
			b[i].push_back(m);
		}
		int best_next,next_ser;
		cur_ind=-1;
		cur_ser=-1;
		while(cur_ind!=m)
		{
			//deb(cur_ind);
			//deb(cur_ser);
			best_next=-1;
			for(int i=0;i<n;i++)
			{
				if(i==cur_ser)continue;
				while(ind[i]<b[i].size()&&b[i][ind[i]]<=cur_ind)
				{
					ind[i]++;
				}
				if(best_next<b[i][ind[i]])
				{
					best_next=b[i][ind[i]];
					next_ser=i;
				}
			}
			ans++;
			cur_ind=best_next;
			cur_ser=next_ser;
		}

		cout<<"Case #"<<num<<": "<<ans-1<<endl;
	}
	return 0;	
}

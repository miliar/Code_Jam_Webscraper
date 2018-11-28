//#include<iostream>
//#include<string>
//#include<vector>
//#include<algorithm>
//#include<cmath>
//#include<set>
//#include<fstream>
//#include<queue>
//#include<fstream>
//#include<map>
//#include<cstring>
//#include<sstream>
//#include<limits.h>
//#include<climits>
//
//using namespace std;
//
//int maxi;
//void calc(vector<int>& v,int s,int p,int ans,int index)
//{
//
//	for(int i=index;i<v.size();i++)
//	{
//		bool in=false;
//		if(s!=0)
//		{
//			int temp=v[i]/3;
//			for(int j=temp-1;j<=temp+1 && j<=10;j++)
//			{
//				if(j<0)
//					continue;
//				for(int q=j;q<=temp+1 && q<=10;q++)
//				{
//					int t=v[i]-(q+j);
//					if((abs(q-j)==2 || abs(q-t)==2 || abs(j-t)==2) && t>=0 && t<=10 && abs(q-j)<=2 && abs(q-t)<=2 && abs(j-t)<=2)
//					{
//						if(q>= p || j>= p || t>=p)
//						{
//							ans++;
//							s--;
//							calc(v,s+1,p,ans,i+1);
//							in=true;
//							break;
//						}
//
//					}
//				
//				}
//				if(in)
//					break;
//			}
//		}
//		if(!in)
//		{
//			bool go=false;
//			int temp=v[i]/3; 
//			for(int j=temp-1;j<=temp+1 && j<=10;j++)
//			{
//				if(j<0)
//					continue;
//				for(int q=j;q<=temp+1 && q<=10;q++)
//				{
//					int t=v[i]-(q+j);
//					if((abs(q-j)<=1 || abs(q-t)<=1 || abs(j-t)<=1) && t>=0 && t<=10 && abs(q-j)<=1 && abs(q-t)<=1 && abs(j-t)<=1)
//					{
//						if(q>= p || j>= p || t>=p)
//						{
//							ans++;
//							go=true;
//							break;
//						}
//
//					}
//				}
//				if(go)
//					break;
//			}
//
//		}
//	}
//	if(ans>maxi)
//		maxi=ans;
//}
//
//int main()
//{
//	//ifstream cin("B-small-attempt0.in");
//	//ofstream cout("B-small-attempt0.out");
//
//
//	int test;
//	cin>>test;
//	for(int q=0;q<test;q++)
//	{	
//		maxi=0;
//		int n,s,p;
//		cin>>n>>s>>p;
//		vector<int> v;
//		vector<int> sss;
//		for(int i=0;i<n;i++)
//		{
//			int x;
//			cin>>x;
//			v.push_back(x);
//			sss.push_back(0);
//		}
//
//		calc(v,s,p,0,0);
//		
//
//		cout<<"Case #"<<q+1<<": "<<maxi<<endl;
//	}
//
//	system("pause");
//	return 0;
//}
//
//


#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>
#include<cstring>
#include<sstream>
#include<limits.h>
#include<climits>

using namespace std;

bool recycle(string x,string y)
{

	for(int i=x.size()-1;i>0;i--)
	{
		
		x.insert(0,1,x[x.size()-1]);
		x.erase(x.size()-1,1);
		if(x==y && x[0]!='0')
			return true;
	}
	return false;
}


int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small-attempt0.out");


	int test;
	cin>>test;
	for(int q=0;q<test;q++)
	{	
		int ans=0;
		int a,b;
		cin>>a>>b;
		map<int,bool> used;
		for(int i=a;i<=b;i++)
		{
			//if(used[i])
			//	continue;
			//if(i%10==0)
			//	continue;
			stringstream ss;
			string x,y;
			ss<<i;
			ss>>x;
			
			int m1[10];
			for(int i=0;i<10;i++)
			{
				m1[i]=0;
			}
			int c=0;
			for(int i=0;i<x.size();i++)
			{
				m1[x[i]-'0']++;
			}
			for(int i=0;i<10;i++)
			{
				if(m1[i]!=0)
				{
					c++;
				}
			}
			if(c==1)
				continue;
			
			for(int j=i+9;j<=b;j+=9)
			{
				ss.str("");
				ss.clear();
				ss<<j;
				ss>>y;
				if(x.size()!=y.size())
					continue;
				int m2[10];
				for(int i=0;i<10;i++)
				{
					m2[i]=0;
				}
				for(int i=0;i<x.size();i++)
				{
					m2[y[i]-'0']++;
				}
				bool ok=true;
				for(int i=0;i<10;i++)
				{
					if(m1[i]!=m2[i])
					{
						ok=false;
						break;
					}
				}
				if(!ok)
					continue;

				
				if(recycle(x,y))
				{
					ans++;
					used[i]=true;
					used[j]=true;
					//break;
				}
				
			}
		}

		cout<<"Case #"<<q+1<<": "<<ans<<endl;
	}

	system("pause");
	return 0;
}




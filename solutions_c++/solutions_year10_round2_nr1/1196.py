//// a.cpp : 定义控制台应用程序的入口点。
////
//
//#include "stdafx.h"

#include <algorithm>

#include <iostream>
#include <math.h>
#include <string>
#include <set>
#include <float.h>
using namespace std;
int T,N,M,count1;

int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	string s,s1;
	set<string> set1;
	set<string>::iterator it;
	for (int i=0; i<T; i++)
	{
		cin>>N>>M;
		set1.clear();
		for (int j=0; j<N; j++)
		{
			cin>>s;
			s=s.substr(1,s.size()-1);
			int m=s.find('/',0);
			while ((m>=0)&&(m<s.size()))
			{
				s1=s.substr(0,m);
				set1.insert(s1);
				m=s.find('/',m+1);
			}
			set1.insert(s);
		}
		count1=0;
		for (int j=0 ;j<M; j++)
		{
			cin>>s;
			s=s.substr(1,s.size()-1);
			int m=s.find('/',0);
			while ((m>=0)&&(m<s.size()))
			{
				s1=s.substr(0,m);
				it=set1.find(s1);
				if (it==set1.end())
				{
					count1++;
					set1.insert(s1);
				}
				m=s.find('/',m+1);
			}
			it=set1.find(s);
			if (it==set1.end())
			{
				count1++;
				set1.insert(s);
			}
		}
		cout<<"Case #"<<i+1<<": "<<count1<<endl;
	}
}


//int T,D,I,M,N;
//int a[110];
//int b[110];
//int zero=0;
//#define MAX 9999999999
//
//int calc(int i)
//{
//	int j=zero;
//	if (i>=(N-1))
//	{
//		return 0;
//	}
//	if (abs(a[i]-a[i+1])<=M)
//	{
//		return calc(i+1);
//	}
//	else
//	{
//		//删自己
//		int count1,count2,count3,count4,count5;
//		if ((i>zero)&&(abs(a[i-1]-a[i+1])>M))
//		{
//			count1=MAX;
//		}
//		else
//		{
//			if (i>zero)
//			{
//				a[i]=a[i-1];
//			}
//			else
//				zero++;
//			count1=D+calc(i+1);
// 			zero=j;
//			a[i]=b[i];
//		}
//
//		//删下一个
//		if ((i<(N-2))&&(abs(a[i]-a[i+2])>M))
//		{
//			count2=MAX;
//		}
//		else
//		{
//			a[i+1]=a[i];
//			count2=D+calc(i+2);
//			a[i+1]=b[i+1];
//		}
//		//替换自己
//		if ((i>0)&&(abs(a[i-1]-a[i+1])>2*M))
//		{
//			count3=MAX;
//		}
//		else
//		{
//			int t1,t2;
//			if (i==zero)
//			{
//				t1=a[i+1]+M;
//				t2=a[i+1]-M;
//			}
//			else
//			{
//				t1=min(a[i-1]+M,a[i+1]+M);
//				t2=max(a[i-1]-M,a[i+1]-M);
//			}
//			if(abs(t1-a[i])<abs(t2-a[i]))
//			{
//				count3=abs(t1-a[i]);
//				a[i]=t1;
//			}
//			else
//			{
//				count3=abs(t2-a[i]);
//				a[i]=t2;
//			}
//			count3+=calc(i+1);
//			a[i]=b[i];
//		}
//		//替换下一个
//		if ((i<N-1)&&(abs(a[i]-a[i+2])>2*M))
//		{
//			count4=MAX;
//		}
//		else
//		{
//			int t1,t2;
//			if (i==N-1)
//			{
//				t1=a[i]+M;
//				t2=a[i]-M;
//			}
//			else
//			{
//				t1=min(a[i]+M,a[i+2]+M);
//				t2=max(a[i]-M,a[i+2]-M);
//			}
//			if (abs(t1-a[i+1])<abs(t2-a[i+1]))
//			{
//				count4=abs(t1-a[i+1]);
//				a[i+1]=t1;
//			}
//			else
//			{
//				count4=abs(t2-a[i+1]);
//				a[i+1]=t2;
//
//			}
//			count4+=calc(i+2);
//			a[i+1]=b[i+1];
//		}
//		//加一个数
//		if (abs(a[i]-a[i+1])>2*M)
//		{
//			count5=MAX;
//		}
//		else
//		{
//			int t1,t2,t3,t4;
//			t1=min(a[i]+M,a[i+1]+M);
//			t2=max(a[i]-M,a[i+1]-M);
//			count5=I;
//			a[i]=t1;
//			t3=calc(i+1);
//			a[i]=t2;
//			t4=calc(i+1);
//			count5+=min(t3,t4);
//		}
//		return min(min(min(min(count1,count2),count3),count4),count5);
//	}
//
//}
//
//int main()
//{
//	//freopen("A-large-practice.in.txt","r",stdin);
//	//freopen("output.txt","w",stdout);
//	cin>>T;
//	int n;
//	for (int i=0; i<T; i++)
//	{
//		cin>>D>>I>>M>>N;
//		for (int j=0; j<N; j++)
//		{
//			cin>>a[j];
//			b[j]=a[j];			
//		}
//		cout<<"Case #"<<i+1<<": "<<calc(0)<<endl;
//	}
//	return 0;
//}


//#include "stdafx.h"
//#include <iostream>
//#include <vector>
//using namespace std;
//
//
//int main()
//{
//	////freopen("C-small-attempt0.in.txt","r",stdin);
//	////freopen("output.txt","w",stdout);
//	//INT64 T,R,K,N,n;
//	////cin>>T;
//	//scanf("%I64d",T);
//	//vector<INT64> g;
//	//vector<INT64> getin;
//	//vector<INT64>::iterator git;
//	//INT64 total,local;
//	//for (INT64 i=0; i<T; i++)
//	//{
//	//	//cin>>R>>K>>N;
//	//	scanf("%I64d,%I64d,%I64d",R,K,N);
//	//	g.clear();total=0;
//	//	getin.clear();
//	//	for (INT64 j=0; j<N; j++)
//	//	{
//	//		//cin>>n;
//	//		scanf("%I64d",n);
//	//		g.push_back(n);
//	//	}
//	//	for (INT64 k=0; k<R; k++)
//	//	{
//	//		local=0;
//	//		git=g.begin();
//	//		while ((local+(*git))<=K)
//	//		{
//	//			n=(*git);
//	//			local+=n;
//	//			g.erase(git);
//	//			getin.push_back(n);	
//	//			if (g.size()==0)
//	//				break;
//	//			git=g.begin();
//	//		}			
//	//		total+=local;
//	//		g.insert(g.end(),getin.begin(),getin.end());
//	//		getin.clear();
//	//	}
//	//	//cout<<"Case #"<<i+1<<": "<<total<<endl;	
//	//	printf("Case #%I64d: %I64d/n",i+1,total);
//	//}
//	return 0;
//}
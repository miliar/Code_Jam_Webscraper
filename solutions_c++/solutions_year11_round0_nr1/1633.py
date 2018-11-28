// console.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <conio.h>
#include <iostream>

using namespace std;

	int num[500];

//int _tmain(int argc, _TCHAR* argv[])
//{
//	freopen("C:\\users\\lxy\\downloads\\A-large-practice.in","r",stdin);
//	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);
//	char str[512];
//	char* da[5000];
//	char* na[5000];
//
//	int l,d,n;
//	cin>>l>>d>>n;
//	for(int x=0;x<d;x++)
//	{
//		da[x]=new char[l+1];
//		cin>>da[x];
//	}
//	for(int x=0;x<n;x++)
//	{
//		na[x]=new char[l*28+1];
//		cin>>na[x];
//	}
//	for(int i=0;i<d;i++)
//	{
//		for(int x=0;x<n;x++)
//		{
//			int p=0;
//			bool b=true;
//			for(int y=0;y<l;y++)
//			{
//				if(na[x][p]=='(')
//				{
//					p++;
//					do
//					{
//						if(da[i][y]==na[x][p])
//						{
//							
//							while( na[x][p++]!=')');
//							if(y+1==l)
//								num[x]++;
//
//							goto xx2;
//						}
//					}
//					while( na[x][p++]!=')');
//					goto xxx;
//xx2:
//					continue;
//				}
//				else
//				{
//					if(da[i][y]!=na[x][p])
//						{
//							goto xxx;
//						}
//					else
//							if(y+1==l)
//								num[x]++;
//					p++;
//				}
//			}
//xxx:
//			;
//		}
//	}
//	for(int x=0;x<n;x++)
//		cout<<"Case #"<<x+1<<": "<<num[x]<<endl;
//
//
//	_getch();
//}

	int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("C:\\users\\lxy\\downloads\\A-large-practice.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\A-large.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);

	int t,n;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		char c,clast=0;
		int o=1,b=1,now,tto=0,ttb=0;
	//	int no=0,nb=0;
		cin>>n;
		for(int j=0;j<n;j++)
		{
			cin>>c;
			if(c=='O')
			{
				cin>>now;
				if(clast=='O'||clast==0)
				{
					tto+=abs(now-o)+1;
					o=now;
					clast='O';
				}
				else
				{
					tto+=abs(now-o)+1;
					o=now;
					//ttb+=nb;
					//nb=0;
					if(tto>ttb)
					{
						//tto+=1;
						//no=0;
					}
					else
					{
						tto=ttb+1;
						//no=0;
					}
					clast='O';
				}
			}
			else if(c=='B')
			{
				cin>>now;
				if(clast=='B'||clast==0)
				{
					ttb+=abs(now-b)+1;
					b=now;
					clast='B';
				}
				else
				{
					ttb+=abs(now-b)+1;
					b=now;
					//tto+=no;
					//no=0;
					if(ttb>tto)
					{
						//ttb+=1;
						//nb=0;
					}
					else
					{
						ttb=tto+1;
						//nb=0;
					}
					clast='B';
				}
			}
			else
				cout<<"wrong"<<endl;


		}
		//tto+=no;
		//ttb+=nb;
		if(tto>ttb)
			cout<<"Case #"<<i+1<<": "<<tto<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<ttb<<endl;

	}

	


	_getch();
}


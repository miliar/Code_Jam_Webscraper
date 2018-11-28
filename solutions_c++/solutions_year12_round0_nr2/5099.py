/*
 * second.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: dinesh
 */

#include<iostream>

using namespace std;


int main()
{
	int t;
	cin>>t;
	int n,s,p;
	int ans=0;
	int temp;
	for(int i = 0;i<t;i++)
	{
		cin>>n>>s>>p;
		ans = 0;
		for(int j = 0 ; j< n;j++)
		{
				cin>>temp;
				if((temp/3) >= p)
				{
					ans++;
				}
				else if( (temp%3) > 0 && (temp/3) + 1 >= p )
				{
					ans++;
				}
				else if(s>0 && (temp/3) > 0 && (temp%3)> 1)
				{
					if((temp/3) + 2 >= p)
					{
						ans++;
						s--;
					}
				}
				else if(temp%3  == 0 && s>0 && (temp/3) + 1 >= p)
				{
					if(temp == 0)
						continue;
					ans++;
					s--;
				}
				else
				{
					continue;
				}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;

	}
}

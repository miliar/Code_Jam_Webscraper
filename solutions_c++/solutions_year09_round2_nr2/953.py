#include <string>
#include <vector>
#include <cmath>

#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream> 

using namespace std;
int main()
{
	ofstream ofs; 
	ifstream ifs;
	ifs.open("d:\\Wraith\\B.in");
	ofs.open("d:\\Wraith\\b.out");
	int num;
	ifs>>num;
	for(int i=1;i<=num;i++)
	{				
		string a;
		ifs>>a;
	ofs<<"Case #"<<i<<": ";
		//cout<<"Case #"<<i<<": ";
		if(a.size()==1)a+="0";
		else
		{
			int j;
			for(j=a.size()-1;j>0;j--)
			{
				if(a[j]>a[j-1])
				{
					int flag=j;
					char min='9';
					for(int k=a.size()-1;k>=j;k--)
					{
						if(a[k]>a[j-1]&&a[k]<min){min=a[k];flag=k;}
					}
					swap(a[j-1],a[flag]);
					sort(a.begin()+j,a.end());
					j=-1;
				}
			}
			if(j!=-2)
			{
				a+="0";
				sort(a.begin(),a.end());
				int k=0;
				while(a[k]=='0')
				{k++;}
				swap(a[k],a[0]);
			}
		}
		ofs<<a<<endl;
		//cout<<a<<endl;
	}
	return 0;
}
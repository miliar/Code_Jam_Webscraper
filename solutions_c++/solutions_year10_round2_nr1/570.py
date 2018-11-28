#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <vector>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

ifstream is("i.txt");
ofstream os("o.txt");

int less1(int i1,int i2)
{
	return i1<i2?i1:i2;

}

int more1(int i1,int i2)
{
	return -less1(-i1,-i2);
}

int main()
{
	int ie2;
	is>>ie2;
	for(int ie=1;ie<=ie2;ie++)
	{
		cout<<"Starts processing case "<<ie<<endl;
		os<<"Case #"<<ie<<": ";

		//begin of processing
		int n,m;
		is>>n>>m;
		set<string> used;
		int cnt=0;
		for(int i=0;i<n+m;i++)
		{
			string path;
			is>>path;
			for(int i=0;i<path.length();i++)
				if(path[i]=='/')
					path[i]=' ';
			stringstream ss;
			ss<<path;
			int cur='0';
			string ct="";
			while(ss>>path)
			{
				path+=cur;
				cur++;
				ct+=path;
				path=ct;
				if(i<n)
					used.insert(path);
				else 
				{
					if(used.find(path)==used.end())
					{
						used.insert(path);
						cnt++;
					}
				}
			}
		}
		os<<cnt<<endl;
		//end of processing

		cout<<"Case "<<ie<<" finished. \n";
	}
	cout<<"done\n";
	return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
int main()
{
	int n,t,na,nb;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>n;
	for (int l=0;l<n;l++)
	{
		in>>t;
		char str[100];
		in>>na>>nb;
		vector <int> timeAA,timeAB,timeDA,timeDB;
		in.getline(str,100);
		int kla=0,klb=0;
		for (int i=0;i<na;i++)
		{
			in.getline(str,100);
			string a,arh,arm,dh,dm;
			a=str;
			arh=a.substr(0,a.find(":"));
			a.erase(0,a.find(":")+1);
			arm=a.substr(0,a.find(" "));
			timeAA.push_back(atoi(arh.c_str())*60+atoi(arm.c_str()));
			a.erase(0,a.find(" ")+1);
			dh=a.substr(0,a.find(":"));
			a.erase(0,a.find(":")+1);
			dm=a.substr(0,a.length());
			timeDB.push_back(atoi(dh.c_str())*60+atoi(dm.c_str())+t);
		}
		for (int i=0;i<nb;i++)
		{
			in.getline(str,100);
			string a,arh,arm,dh,dm;
			a=str;
			arh=a.substr(0,a.find(":"));
			a.erase(0,a.find(":")+1);
			arm=a.substr(0,a.find(" "));
			timeAB.push_back(atoi(arh.c_str())*60+atoi(arm.c_str()));
			a.erase(0,a.find(" ")+1);
			dh=a.substr(0,a.find(":"));
			a.erase(0,a.find(":")+1);
			dm=a.substr(0,a.length());
			timeDA.push_back(atoi(dh.c_str())*60+atoi(dm.c_str())+t);
		}
		int needa=0,needb=0;
		for (int i=0;i<24*60-1;i++)
		{
			for (int j=0;j<timeAA.size();j++)
				if (timeAA[j]==i)
					kla--;
			
			for (int j=0;j<timeAB.size();j++)
				if (timeAB[j]==i)
					klb--;
			for (int j=0;j<timeDA.size();j++)
				if (timeDA[j]==i)
					kla++;
			for (int j=0;j<timeDB.size();j++)
				if (timeDB[j]==i)
					klb++;
			needa=max(needa,-kla);
			needb=max(needb,-klb);

		}
	out<<"Case #"<<l+1<<": "<< needa<<" "<<needb<<endl;

	}
	return 0;
}
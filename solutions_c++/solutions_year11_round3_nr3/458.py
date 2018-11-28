#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;
int a[120];

main()
{
	ifstream fin;ofstream fout;
	fin.open("D:\\C-small-attempt0.in");
//    fin.open("D:\\C-large.in");
	fout.open("D:\\C-small.out");
//	fout.open("D:\\C-large.out");
	
	int tests;
	
	fin>>tests;
	
	for(int cas=1;cas<=tests;++cas)
	{
     int n,l,h;
     fin>>n>>l>>h;
     for(int i=0;i<n;++i)fin>>a[i];
     int ret;
     for(ret=l;ret<=h;++ret)
     {
      int yes=1;
      for(int i=0;i<n && yes;++i)
      {
       int x=ret;
       int y=a[i];
       if(y<x){ swap(x,y);}
       if(y%x!=0)yes=0;
      }
      if(yes)break;
     }
     if(ret>h)
     fout<<"Case #"<<cas<<": NO"<<endl;
     else
     fout<<"Case #"<<cas<<": "<<ret<<endl;
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}

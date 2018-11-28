#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int xo(int a,int b)
{
int base=1;
int ret=0;
while(a>=base || b>=base)
{
  ret+= ((a&base) != (b&base))?base:0;
  base<<=1;
}    
return ret;
}

main()
{
	ifstream fin;ofstream fout;
	fin.open("C:\\Data\\C-large.in");
//    fin.open("C:\\Data\\C-small.in");
//    fin.open("C:\\Data\\C-small-attempt0.in");
	fout.open("C:\\Data\\C-large.out");
//	fout.open("C:\\Data\\C-small.out");
	
	int tests;
	
	fin>>tests;
	
	for(int cas=1;cas<=tests;++cas)
	{
     int total=0,min=100000000;
     int ret=0;
     int N;
     fin>>N;
     for(int i=0;i<N;++i)
     {
      int temp;
      fin>>temp;        
      ret=xo(ret,temp);
      total+=temp;
      if(min>temp)min=temp;
     }
     if(ret==0)
      fout<<"Case #"<<cas<<": "<<total-min<<endl;
     else
      fout<<"Case #"<<cas<<": NO"<<endl;     
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}

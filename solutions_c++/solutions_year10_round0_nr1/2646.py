#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

 using namespace std;



 int lod[1000];
 int main()
 {
	 int t,pro,n,ka,cas=1,pro2,i,j;
	 //freopen("a1.out","w",stdout);
	 cin>>t;
	 while(t--)
	 {
		 cin>>n>>ka;
		 i=0;
		 while(ka!=0)
		 {
			 lod[i++] = ka%2;
			 ka/=2;
		 }
			int  flag = 0;
			for(j=0;j<n;j++)
			 {
				 if(lod[j]==0)
				{
					flag = 1;
					break;
				 }
			 }

		 if( !flag )
			 cout<<"Case #"<<cas++<<": ON"<<endl;
		 else
			 
			 cout<<"Case #"<<cas++<<": OFF"<<endl;
		 memset(lod,0,sizeof(lod));
	 }
	return 0;
 }

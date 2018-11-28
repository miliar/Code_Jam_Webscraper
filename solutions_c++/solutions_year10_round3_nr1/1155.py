#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;
typedef pair<int,int> PI;
vector<PI> v;
int main()
{

	int T,N,a_1,b_1,a_2,b_2,x=1;
	for(cin>>T;T>0;T--)
	{
		cin>>N;v.clear();
		/*if(N==1) { cin>>a_1>>b_1;cout<<"Case #"<<x++<<": "<<0<<endl;continue;}
		else if(N==2)
		{
			cin>>a_1>>b_1>>a_2>>b_2;
			if((a_1<a_2 && b_1>b_2)||(a_1>a_2 && b_1<b_2)) cout<<"Case #"<<x++<<": "<<1<<endl;
			else  cout<<"Case #"<<x++<<": "<<0<<endl;
		}
		else*/
		{
			int a,b,cnt=0;
			for(int i=0;i<N;i++) cin>>a>>b,v.push_back(PI(a,b));
			sort(v.begin(),v.end());// sorted in creasing order
			for(int i=0;i<N;i++)
			{
				int a_1=v[i].first,b=v[i].second;
				for(int j=i+1;j<N;j++) 
				 {
					if(v[j].second<b) cnt++;
				 }
			}
			cout<<"Case #"<<x++<<": "<<cnt<<endl;
		}
	}
}	

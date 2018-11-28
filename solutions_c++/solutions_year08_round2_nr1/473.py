#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
long long X[100004],Y[100004];
int main()
{
	long long A,B,C,D,x1,y1,M;
	int n,test;
	cin>>test;
	for(int i1=1;i1<=test;++i1)
	{
		cin>>n>>A>>B>>C>>D>>x1>>y1>>M;
		X[0]=x1;
		Y[0]=y1;
		for(int i=1;i<n;i++)
		{
			X[i]=(A*X[i-1]+B)%M;
			Y[i]=(C*Y[i-1]+D)%M;
		}
		
		int count=0;
		for(int i=0;i<n;++i)
			for(int k=i+1;k<n;++k)
				for(int j=k+1;j<n;++j)
					if((X[i]+X[k]+X[j])%3==0 && (Y[i]+Y[k]+Y[j])%3==0)
						count++;
		int a=i1;
		printf("Case #%i: %i\n",a,count);
	}
}

	
	

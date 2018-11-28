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
#define MAX 1000

using namespace std;
stringstream stream;
int A[MAX];
bool convertAndCom(int n,int base)
{
	int res=0;
	int i=0,j=0;
	int tempb=1;
	
	int num1=0;
	bool flag=true;

	int l=0;


	while(res!=1)
	{
		flag=false;
		num1=0;
		res=0;
		
		for(i=0;i<l;i++)
			if(A[i]==n)return false;
		A[l++]=n;

		
		while(tempb<=n)
		{
			tempb*=base;
		}
		tempb=tempb/base;

		while(n>=base)
		{
			int temp;
			temp=n/tempb;

			n=n-temp*tempb;
			tempb=tempb/base;
			res+=temp*temp;
		}
		res+=n*n;
	
		n=res;
	}
	return true;
}

int base[10];
int main()
{
	freopen("large1.in","r",stdin);
	freopen("large1.out","w",stdout);

	int Case=0;
	int i=0,j=0;
	int T=0;
	string s;


	getline(cin,s);
	stream<<s;
	stream>>T;
	
	
	while(Case<T)
	{

		getline(cin,s);
		stream.clear();
		stream.str(s);

		int baseNum=0;
		for(i=0;i<10;i++)
			base[i]=0;
		baseNum=0;
		while(stream>>base[baseNum])baseNum++;
		
		i=2;
		while(1)
		{
			for(j=0;j<baseNum;j++)
			{
				if(!convertAndCom(i,base[j]))
					break;
			}
			if(j==baseNum)break;
			else i++;
		}
		Case++;
		cout<<"Case #"<<Case<<": "<<i<<endl;

	}


	return 0;
}
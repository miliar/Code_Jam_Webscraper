#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;


int A,B,pairs=0;
vector <int> test;

int check_rotate(int *v,int pos,int len,int curr)
{
	int i,n=0;

	for (i = pos-1;i >= 0;i--)
	{
	    n = n*10+v[i];
	}
	for (i = len-1;i >= pos;i--) 
	{
		n = n*10+v[i];
	}
	if(n>curr && n<=B)
	{
		
		if(find(test.begin(),test.end(),n)==test.end())
		{
			test.push_back(n);
			pairs++;
			//cout<<curr<<" "<<n<<endl;
		}
	}
}


int main()
{
	int T,i,j,k,len,nr;
	cin>>T;
	int v[100];

	for(i=0;i<T;i++)
	{
		cin>>A>>B;
		pairs = 0;
		for(j=A;j<B;j++)
		{
			//if(seen[j]==0)
			{
				len =0;
				nr = j;
				while (nr)
				{
					v[len] = nr%10;
					len++;
					nr/=10;
    				}
				for(k=1;k<len;k++)
					check_rotate(v,k,len,j);
			}
			test.clear();
		}
		cout<<"Case #"<<i+1<<": "<<pairs<<endl;
	}
	
	
}
		
	

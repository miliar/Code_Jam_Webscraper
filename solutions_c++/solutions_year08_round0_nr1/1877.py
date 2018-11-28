
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

const int mys=102;
const int myq=1002;
int mydp[myq][mys];
string str[mys],que[myq];
bool flag[myq];
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/
	int N;
	cin>>N;
	for(int cases=1;cases<=N;cases++)
	{

		int s,q;
		cin>>s;
		
		string mytmp;
		getline(cin,mytmp);
		for(int i=0;i<s;i++)
		{
			getline(cin,str[i]);
			
		}
		cin>>q;
		getline(cin,mytmp);
		
		for(int i=0;i<q;i++)		
		getline(cin,que[i]);

		for(int i=0;i<s;i++)
		{
			mydp[0][i]=0;
		}

		for(int k=1;k<q;k++)
		{
			for(int m=0;m<s;m++)
			{
				if(que[k]!=str[m])
				{
					int minv=1000000,tmp;
					for(int j=0;j<s;j++)
					{
						
						if(que[k-1]!=str[j]){
							if(j!=m) tmp=mydp[k-1][j]+1;
							else tmp=mydp[k-1][j];
							minv=min(minv,tmp);}
					}
					mydp[k][m]=minv;
				}
			}
		}

		int minv=1000000;
		if(q==0) minv=0;
		else
			for(int i=0;i<s;i++)
			{
				if(que[q-1]==str[i]) continue;
				minv=min(minv,mydp[q-1][i]);
			}
			cout<<"Case #"<<cases<<": "<<minv<<endl;
	}
	return 0;
}



#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64

int main()
{
	int L,D,N;
	int fg = 1;
	cin>>L>>D>>N;
	int kk, k,i;
	vector<string> dic;
	string tock;
	for(k = 0;k<D;k++)
	{
		cin>>tock;
		dic.push_back(tock);
	}
	for(kk = 0;kk<N;kk++)
	{
		cin>>tock;
		vector<string> p;
		
		int j = 0;
		for(i = 0;i<L;i++)
		{
			
			string tmp;
			if(tock[j] == '(')
			{
				j++;
				while(tock[j]!=')')
					tmp+=tock[j++];				
			}
			else
				tmp+=tock[j];	
			j++;
			p.push_back(tmp);

		}
		int m,res = 0;
		for(i = 0;i<D;i++)
		{
			int got  = 0;
			for(m = 0;m<L;m++)
			{
				for(k = 0;k<p[m].size();k++)
					if(p[m][k] == dic[i][m])
					{
						got ++;
						break;
					}
			}
			if(got == L)
				res++;
		}
		printf("Case #%d: %d\n",fg++,res);

	}
	


	return 0;
}
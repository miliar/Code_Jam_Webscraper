#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<cstdio>
#include<queue>
#include<list>
#include<stack>
#include<utility>
#include<numeric>
#include<map>
#include<cctype>
#include<cstring>
#include<sstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define s scanf
#define p printf

#define INF 1000000000

pair<bool,string> C[20];
string A[5100],B;
int ans,l,d,n;

void rec(string k,int pos,int ctr)
{
	string tmp;
	string *tmp1;
	if(ctr==pos)
	{
		if(binary_search(A,A+d,k))
		{
				ans++;
				//cout<<k<<endl;
		}
		return;
	}
	else
	{
		if(C[pos].first==true)
		{
			F(i,C[pos].second.length())
			{
				tmp1=lower_bound(A,A+d,k+C[pos].second[i]);
				if(tmp1!=A+d)
					tmp=*tmp1;
				else
					tmp="00000000000000000000000000000000000000000000000000000000000000000";
				if(tmp.substr(0,k.length()+1)==k+C[pos].second[i])
					rec(k+C[pos].second[i],pos+1,ctr);
			}
		}
		else
		{
			rec(k+C[pos].second,pos+1,ctr);
		}
	}
}

int main()
{
	int j;
	s("%d%d%d",&l,&d,&n);
	F(i,d)
		cin>>A[i];
	sort(A,A+d);

	string pata;
	F(i,n)
	{
		F(k,20)
		{
			C[k]=make_pair(0,"");
		}
		pata="";
		cin>>B;
		j=0;
		F(k,B.length())
		{
			if(B[k]=='(')
			{
				C[j].first=true;
			}
			else if(B[k]==')')
			{
				//C[i][j].first=false;
				j++;
			}
			else
			{
				C[j].second+=B[k];
			}
		}
		if(B[B.length()-1]!=')')
			j++;

		ans=0;
		rec(pata,0,j);
		p("Case #%d: %d\n",i+1,ans);
	}

	return 0;
}

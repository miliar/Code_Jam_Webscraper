#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
set<string> dic[20];
string ss;
bool dentro = false;

int l,n,d;
int dfs(int i,string co)
{
	if (dic[co.size()].find(co) != dic[co.size()].end() )
	{
		if (co.size() == l)
		{
          //  cout<<co<<endl;
			return 1;
		}
		else
		{
			
			if (ss[i] == '(')
			{		
				int sum = 0;
				int fin = 0;
				for(fin = i+1; ss[fin] != ')'; fin++)	
				{}		
				dentro = true;
				i++;
				for(int j = i; j <fin;j++)
				{
                  ///  cout<<co<<" "<<ss[j]<<endl;    
					sum+= dfs(fin+1,co + ss[j]);
				}
				return sum;
				
			}
			else
			{				
				return dfs(i+1,co+ss[i]);
			}
		}
	}
	else
	{
       // cout<<"no "<<co<<endl;;    
    }
	return 0;
	
}
main()
{
	
	cin>>l>>d>>n;
	dic[0].insert("");
	forn(i,d)
	{
		string auxs;
		cin>>auxs;
		string aux;
		forn(j,auxs.size())
		{
			aux+=auxs[j];
			dic[j+1].insert(aux);			
		}		
	}
	forn(i,n)
	{		
		cin>>ss;
		int cont = dfs(0,"");
		cout<<"Case #"<<i+1<<": "<<cont<<endl;
	}
}


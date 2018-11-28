#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>
#include<cstdio>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define dforsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647

vector<string> fac;
string ss;
double dfs(int i)
{
	stringstream sst; 
	
	sst<<ss.substr(i+1, ss.size()); 
	double x;
	sst>>x;
	string ca;
	sst>>ca;
	if (ca == ")")
	  	{
              //                cout<<x<<endl;
						return x;
                    }
		
//	cout<<endl<<x<<" " <<ca<<endl;
	if (esta(ca,fac))
	{
                //       cout<<"1"<<endl;
		forsn(j,i+1,ss.size())
			if (ss[j] == '(')
				{
                      //        cout<<dfs(j)<<endl;
						return dfs(j)* x;
                    }
		
	}
	else
	{		
                        //        cout<<"2"<<endl;
		bool entro = false;
		int cont = 0;
		forsn(j,i+1,ss.size())
		{
                              
			if (ss[j] == '(')
			{
				cont++;
			  entro = true;
			}
			if (ss[j] == ')')
				cont--;
			if (entro && cont == 0)
				forsn(k,j+1,ss.size())
					if (ss[k] == '('){
                         //     cout<<x<<" "<<dfs(k)<<endl;
						return dfs(k)* x;
                    }
		}
		
	}
	return 0;
	

}

int main()
{
	int pp;
	cin>>pp;
//	cout<<pp;
	forn(cc,pp)
	{
		int xx;
		cin>>xx;
		ss = "";
		string auxs;
		getline(cin,auxs);
		forn(i,xx)
		{
			getline(cin,auxs);
			ss += auxs;
		}
//		cout<<ss<<endl;
		forn(i,ss.size())
		{
			if (ss[i] == '(' || ss[i] == ')')
			{
				if (i != 0)
					if (ss[i-1] != ' ')
					{
						ss = ss.substr(0,i) + " " + ss.substr(i,ss.size() - (i-1));
						i++;
                  }
				if (i != ss.size()-1)
					if (ss[i+1] != ' ')
						ss = ss.substr(0,i+1) + " " + ss.substr(i+1,ss.size()- (i+1));
				
			}
		//	cout<<ss<<endl;;
		}
	//		cout<<ss<<endl;;
		cout<<"Case #"<<cc+1<<":"<<endl;
		
		cin>>xx;
		forn(i,xx)
		{
			fac.clear();
			string auxs;
			int aa;
			cin>>auxs>>aa;
			forn(j,aa)
			{
				cin>>auxs;
				fac.pb(auxs);
			}
			double auxd = dfs(0);
		//	cout<<auxd<<endl;
			
			printf("%0.7f", auxd );
			cout<<endl;
		}
		cout<<endl;
	}
	
	return 0;
		
}

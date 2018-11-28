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
#define MAX2 9223372036854775807


int main()
{	
	int pp;
	cin>>pp;
//	cout<<pp;
	forn(cc,pp)
	{
		string ss;
		cin>>ss;
	//	cout<<ss;
	//	cout<<ss;
      	if(!next_permutation(all(ss)))
        {
            // ss = ss[0] + "0" + ss.substr(1,ss.size()-1);
//            string auxss = ss;
             ss = "0" +ss;  
             sort(all(ss)); 
             //cout<<ss; 
             forn(i,ss.size())
             {
                      if(ss[i] != '0')  
                      {
                               char auxs = ss[0];
                               ss[0] = ss[i];
                                ss[i] = auxs;
                                i = ss.size();
                    }
             }
           //   cout<<ss;                            
              //next_permutation(all(ss));                                     
        }
        
		cout<<"Case #"<<cc+1<<": "<<ss<<endl;
	}
	return 0;
		
}

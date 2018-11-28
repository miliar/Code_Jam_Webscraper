#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;
typedef long long ll;

int main()
{
    ifstream  in("B-large.in.txt",ios::in);
    ofstream  out("output.txt");
    int T,i=0;
	string N;
	in>>T;
	while(i++<T)
	{
       in>>N;
	   string tp=N;
	   next_permutation(N.begin(),N.end());
	   if(N>tp) out<<"Case #"<<i<<": "<<N<<endl;
	   else 
	   {
		   if(N[0]=='0')
		   for(int i=1;i<N.size();i++)
			   if(N[i]!='0')
			   {
				   N[0]=N[i];
				   N[i]='0';
				   break;
			   }
		   N.insert(N.begin()+1,1,'0');
		   out<<"Case #"<<i<<": "<<N<<endl;
	   }
	}
}
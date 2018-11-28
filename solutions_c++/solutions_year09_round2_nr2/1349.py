#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(){
   freopen("B-small-attempt1.in","r",stdin);
   freopen("ans.txt","w",stdout);
   int T, i;
   string str;
   for(cin>> T, i = 1; i <= T; i++)
   {
	    cout<<"Case #"<<i<<": ";
	    cin>>str;
		if(next_permutation(str.begin(), str.end() ))
		{
			cout<<str<<endl;
		}
		else
		{ 
			str  = "0" + str;
			while(str[0]=='0' && next_permutation(str.begin(), str.end() ) );
			cout<<str<<endl;
		}
   }
}
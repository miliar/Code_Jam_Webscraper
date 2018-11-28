#include<iostream>
#include<string>
using namespace std;

int main()
{
 	string s;
 	char m[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};//{'y','h','e','i','c','c','l','b','d','u','i','g','l','b','e','r','z','p','d','r','j','g','f','h','a','q'};
 	
 	int t;
 	cin>>t;
 	int c=1;
 	getchar();
 	while(t--)
 	{
	 		  getline(cin,s);
	 		cout<<"Case #"<<c++<<": ";   
	 		  for(int i=0;i<s.length();i++)
	 		  {
			   		  if(s[i]!=' ')
			   		  {
					   		cout<<m[s[i]-'a'];
							}
							else
							cout<<' ';
		       }
     cout<<endl;
	 }	
	 
	 return 0;
	 }
	 
	 	   
			   	   	 

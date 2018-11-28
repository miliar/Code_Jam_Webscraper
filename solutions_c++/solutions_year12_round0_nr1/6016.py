using namespace std;


#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<sstream>

#define MAX 

int main()
{
	
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("out.txt","wt",stdout);


	int T,c=1;
	
	cin>>T;

	cin.ignore(1024,'\n');
	while(c<=T)
	{
	

		char buf[]="yhesocvxduiglbkrztnwjpfmaq";
		string G,s;
		vector<string> vs;
	
		getline(cin,G);
		stringstream S(G);

		while(S>>s)
			vs.push_back(s);
		
		cout<<"Case #"<<c<<": ";
		for(int i=0;i<vs.size();i++)
		{
			for(int j=0;vs[i][j]!='\0';j++)
			{
				vs[i][j]=buf[ vs[i][j] - 97];
			}
				
			cout<<vs[i]<<" ";
		}
		cout<<endl;
		c++;
	}	
	
	return 0;
}			

	

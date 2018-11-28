#include<iostream>
#include<string>
#include <sstream>
using namespace std;
int noi,arr[101],len[101];
int main()
{
    int noi,g,ans,caseno=1,noiStore,k,i,n,s,p;
	string inputNo;
	getline(cin,inputNo);
	stringstream(inputNo) >> noi;
	noiStore=noi;
	k=0;
	i=0;
	
	while(noiStore>0)
	{
		i=0;
		ans=0;
		string token, str,mystr;
		
		getline(cin,str);
		istringstream iss(str);
		while ( getline(iss, token, ' ') )   //space is the token
		{

			istringstream (token.c_str()) >> arr[i++];
			
		}
		n=arr[0];
		s=arr[1];
		p=arr[2];
		for(g=3;g<=2+n;g++)
		{
			int val1=0,val2=0,flag=0,sub=0;
			val1=arr[g]-p;
			if(val1>=0)
			{
				sub=2*(p-1);
				val2=val1-sub;
				if(val2>=0)
				{
					ans++;
					continue;
					
				}
				else if(s>0)
				{
					sub=2*(p-2);
					val2=val1-sub;
					if(val2>=0)
					{
						ans++;
						s--;
						
					}
				
				}
				
				
				
			}
			
				
			
		
		}
		cout<<"Case #"<<caseno<<": "<<ans;
		if(caseno<noi)
			cout<<endl;
		caseno++;
				
		
		
		noiStore--;
	}
	return 0;
}

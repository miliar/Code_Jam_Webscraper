#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		string base="QWERASDF";
		
		int C;
		cin>>C;
		vector<string> a(C);
		for(int i=0;i<C;i++)
		cin>>a[i];
		int D;
		cin>>D;
		vector<string> b(D); 
		for(int i=0;i<D;i++)
		cin>>b[i];

		int sz;
		cin>>sz;
		string s;
		cin>>s;
		//Input parsing Finally Over!!! main part now starts :)
		
		string ret="";
		for(int i=0;i<sz;i++)
		{
			char c=s[i];
			//Check for non base element formation
			if(ret.size()==0)//First character no need to put scene in this
			{
				ret+=c;
				continue;
			}
				
				char p=ret[ret.size()-1];//prev char
				bool replaced=false;
				for(int j=0;j<C;j++)
				{
					if((a[j][0]==p && a[j][1]==c) || (a[j][1]==p && a[j][0]==c))
					{
						ret[ret.size()-1]=a[j][2];
						replaced=true;
					}
				}
				if(replaced==false) ret+=c;//append incase no formation occurs

			//	cout<<ret<<"................................"<<endl;

				//Now chack for opposing one

				c=ret[ret.size()-1];
				int flag=0;
				for(int j=0;j<ret.size()-1;j++)
				{
					p=ret[j];
					for(int k=0;k<D;k++)
					{
						
						if((b[k][0]==p && b[k][1]==c) || (b[k][1]==p && b[k][0]==c))
						{
							ret="";
							flag=1;
							break;
						}
					}
					if(flag==1) break;
				}
			//	cout<<ret<<"-----------------------"<<endl;

						
			
		}
			
		//Printing part
		cout<<"Case #"<<numCase<<": [";
		int len=ret.size();
		for(int i=0;i<len;i++)
		{
			if(i==(len-1))
				cout<<ret[i];
			else cout<<ret[i]<<", ";
		}
		cout<<"]"<<endl;

	}
	return 0;
}

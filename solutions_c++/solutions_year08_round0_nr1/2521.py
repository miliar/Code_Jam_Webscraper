#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	ifstream fout;
	fout.open("A-Large.in");
	int cas;
	fout>>cas;
	for(int i=0;i<cas;i++)
	{
		int search;
		fout>>search;
		fout.ignore();
		vector<string> vs(search);
		for(int j=0;j<search;j++)
		{
			string s;
			getline(fout,s);
			vs[j]=s;
		}
    
		int qu;
		fout>>qu;
		vector<string> query(qu);
		fout.ignore();
		for(int j=0;j<qu;j++) getline(fout,query[j]);
		
		int marker=0;
        int ret=0;
        bool flag=false;
        while(marker<qu && !flag)
        {
           int maxi=0; 
           int count;
           for(int j=0;j<vs.size();j++)
           {
              count=0; bool control=false;
              for(int k=marker;k<query.size();k++)
              {
                   if(vs[j]==query[k])
                   {
                       control=true;
                       if(count>maxi)
                       {
                         maxi=count;
                       }
                       break;
                   }
                   count++;
              }
              if(!control) { flag=true; break; }
           }
           marker+=maxi;
           ret++;
        }
		cout<<"Case #"<<i+1<<": ";
        if(ret>0) cout<<ret-1<<endl; 
        else cout<<ret<<endl;
	}
}

		
		
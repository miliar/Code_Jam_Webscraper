#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	int kase;
	fin>>kase;
	for(int i=0;i<kase;i++)
	{
		int ser;
		fin>>ser;
		fin.ignore();
		vector<string> vs(ser);
		for(int j=0;j<ser;j++)
		{
			string s;
			getline(fin,s);
			vs[j]=s;
		}
    
		int que;
		fin>>que;
		vector<string> query(que);
		fin.ignore();
		for(int j=0;j<que;j++) getline(fin,query[j]);
		
		int mark=0;
        int res=0;
        bool flag=false;
        while(mark<que && !flag)
        {
           int max=0; 
           int count;
           for(int j=0;j<vs.size();j++)
           {
              count=0; bool control=false;
              for(int k=mark;k<query.size();k++)
              {
                   if(vs[j]==query[k])
                   {
                       control=true;
                       if(count>max)
                       {
                         max=count;
                       }
                       break;
                   }
                   count++;
              }
              if(!control) { flag=true; break; }
           }
           mark+=max;
           res++;
        }
		cout<<"Case #"<<i+1<<": ";
        if(res>0) cout<<res-1<<endl; 
        else cout<<res<<endl;
	}
}

		
		
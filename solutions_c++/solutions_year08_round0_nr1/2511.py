#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	ifstream fout;
	fout.open("A-large.in");
	int kase;
	fout>>kase;
	for(int i=0;i<kase;i++)
	{
		int ser;
		fout>>ser;
		fout.ignore();
		vector<string> vs(ser);
		for(int j=0;j<ser;j++)
		{
			string s;
			getline(fout,s);
			vs[j]=s;
		}
    
		int que;
		fout>>que;
		vector<string> query(que);
		fout.ignore();
		for(int j=0;j<que;j++) getline(fout,query[j]);
		
		int mark=0;
        int result=0;
        bool flag=false;
        while(mark<que && !flag)
        {
           int maximum=0; 
           int count;
           for(int j=0;j<vs.size();j++)
           {
              count=0; bool control=false;
              for(int k=mark;k<query.size();k++)
              {
                   if(vs[j]==query[k])
                   {
                       control=true;
                       if(count>maximum)
                       {
                         maximum=count;
                       }
                       break;
                   }
                   count++;
              }
              if(!control) { flag=true; break; }
           }
           mark+=maximum;
           result++;
        }
		cout<<"Case #"<<i+1<<": ";
        if(result>0) cout<<result-1<<endl; 
        else cout<<result<<endl;
	}
}

//Output is generated in CYGWIN using the command g++.........
// then ./a.exe>output....this generate an output file directly..

		
		
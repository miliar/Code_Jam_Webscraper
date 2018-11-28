#include<iostream>
#include <fstream>
#include <string>
#include <sstream>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;
#define pb push_back

int DIS(int a, int b,int c)
{
	int d=abs(a-b);
	if(c>=d)
	return b;
	else 
	{	d=abs(d-c);
		return b-d;
	}
}

int main ()
 {	
    string line;
    long int T=0,i=0,j=0,N=0,O=0,B=0,bu=0;
    string n,cas,total,robot,button;
    ifstream myfile ("A-large.in");
    ofstream myfile1 ("large.out");
    getline (myfile,line);
    stringstream convert(line);
    convert>>T;
        for(i=0;i<T;i++)
		
	
        {	vector<int>sec,ora,bla;
			sec.clear();
			ora.clear();
			bla.clear();
			ora.push_back(1);
            bla.push_back(1);
			bu=0;
            getline (myfile,line);
            stringstream ss;
            ss<<line;
            ss>>n;
            stringstream convert1(n);
            convert1>>N;
			
            for(j=0;j<N;j++)
            {
                ss>>robot;
                ss>>button;
                stringstream convert2(button);
                convert2>>bu;
                if(robot=="O")
                {	sec.push_back(1);
                  	ora.pb(bu);
				//	  cout<<bu<<" is the num\n";
                   
                }
				
				else if(robot=="B")
                {	sec.push_back(2);
                   	bla.pb(bu);
                  //	ut<<bu<<" is the num\n";
                }
            }
        	int a=1,b=1,c,count=0;
		//	  cout<<sec.size()<<endl;
		//	  cout<<N<<endl;
		
		//	  for(j=0;j<sec.size();j++)
			//	  cout<<sec[j]<<" ";
		//	  cout<<endl;
			for(j=0;j<bla.size();j++)
				cout<<bla[j]<<" ";
			cout<<endl;
		
			for(j=0;j<ora.size();j++)
				cout<<ora[j]<<" ";
			cout<<endl;
		
		a=1,b=1,c,count=0;
		cout<<"N is "<<N<<endl;
			for(j=0;j<N;j++)
			{	cout<<sec[j]<<" ";
				if(sec[j]==1)
				{
				//cout<<ora[a]<<" ";
				
					c=abs(ora[a]-ora[a-1])+1;
					count+=c;a++;
				if(b!=bla.size())	 bla[b-1]=DIS(bla[b-1],bla[b],c);
					
					//cout<<count<<" -> ";
				}
			
				if(sec[j]==2)
				{
					c=abs(bla[b]-bla[b-1])+1;
					count+=c;b++;
				if(a!=ora.size())	ora[a-1]=DIS(ora[a-1],ora[a],c);
					
				
				//	  cout<<count<<" -> ";
				}
				
				cout<<c<<endl;
			
			
			}cout<<endl;
			//cout<<count<<endl;
			
			
			
            stringstream convert3;
            stringstream convert4;
            convert3<<i+1;
            convert4<<count;
            total=convert4.str();
            cas=convert3.str();
           myfile1<<"Case #"<<cas<<": "<<total<<"\n";
        }
    return 0;
 }


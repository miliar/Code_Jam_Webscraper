#define X 4
#define MAX 200
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;

int main()
{
 	ifstream filin;//("incs.txt",ios:in);
    filin.open("incs.txt",ios::in);

	int t;
	filin>>t;
	int i[100][200];
	int n;
	string out[200];
	for(int s=0;s<t;++s)
	{
		filin>>n;
		for(int p=0;p<n;++p)
				filin>>i[s][p];
		for(int p=n;p<MAX;++p)
				i[s][p]=-2;                
	}

	filin.close();
 
    ofstream fout;
    fout.open("outcs.txt",ios::out);
    for(int s=0;s<t;++s)
	{
		int w=1;
		int h=0;
		int res=0,p;
		h=i[s][0];
		w=0;

		w=1;
        	
		while(i[s][w]>-1)
		{
               //fout<<h<<" ";
               h^=i[s][w];
			  
			   w-=-1;                
		}
		//fout<<h<<"\n";
		if(h==0)
		{
		//success
			   p=0;while(i[s][p]>-1){p-=-1;}sort(i[s],i[s]+p);
			   res=0;for(int q=1;q<p;++q){res-=-i[s][q];}
			   stringstream ss;
               ss << res;
               ss >> out[s];//out[s]        
		}
		else
		{
		//fail
			  out[s]="NO";    
		}   
	}   
	
    
	for(int r=0;r<t;++r)
	{
			//r result
			fout<<"Case #"<<r+1<<": "<<out[r]<<"\n";
	}
	fout.close();

    return 0;	  
}

#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
#include<list>

using namespace std;
int c;
	char ser[1000];
		string serc[1000];
		char que[1000]; 
    	string quer[1000];
		int n,q;
		 int se[1000];
		 int qu[1000];
		 int ans;

int algo(int qu[],int se[],int q,int n)
{
	list<int> pos[100];
	list<int> ::iterator p,save;
	int max;
	int ans=0;
	char found;

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<q;j++)
		{
			if(qu[j]==i+1)
			{
				pos[i].push_back(j);
	
			}
			
		}
	}
 

	while(1)
	{


	found='n';

	for(int i=0;i<n;i++)
	{
		if(pos[i].size()<=0)
		{		
			found='y';
			break;
		}
	}
	
	if(found=='y')
		break;

	ans++;
	max=0;

	for(int i=0;i<n;i++)
	{
		p=pos[i].begin();
		
		if(*p>max)
			max=*p;
	}

	for(int i=0;i<n;i++)
	{
		
		p=pos[i].begin();
		
		while(p!=pos[i].end()&&*p<max)
		{
			pos[i].erase(p);
			p=pos[i].begin();
			
		}	
	
	}
	
	}
	return ans;
}
				
int main(void)
{	
	ifstream fin("a.in");
	ofstream fout("output.txt");
	fin>>c;


	for(int l=0;l<c;l++)
	{
      fin>>n;
	    for(int i=0;i<n;i++)
	       {
		   se[i]=i+1;
		    }
	     
		 fin.getline(&ser[0],100,'\n');

		 for(int i=0;i<n;i++ )
		 {
           	 fin.getline(&ser[0],100,'\n');
			
             serc[i]=ser;
		   }

	 fin>>q;


	 fin.getline(&que[0],100,'\n');

	for(int i=0;i<q;i++)
	{
		fin.getline(&que[0],100);
		quer[i]=que;
		
	}
	
		for(int i=0;i<q;i++)
	{
	
		for(int j=0;j<n;j++)
		{

		  if(serc[j]==quer[i])
		  {
			  qu[i]=j+1;
			 
			  break;
		  }
		 
		  
		  }
	}
	
	ans=algo(qu,se,q,n);
	

		fout<<"Case #"<<l+1 <<": "<<ans<<"\n";
	}
	getch();
	return 0;
	
}
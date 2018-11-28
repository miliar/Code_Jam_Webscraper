#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
#include<list>

using namespace std;
int c;
	char ser[100][100];
		string serc[100][100];
		char que[100][100]; 
    	string quer[100][100];
		int n[100],q[100];
		 int se[100][100];
		 int qu[100][100];
		 int ans[100];

int algo(int qu[],int se[],int q,int n)
{
	list<int> pos[10];
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
      fin>>n[l];
	    for(int i=0;i<n[l];i++)
	       {
		   se[l][i]=i+1;
		    }
	     
		 fin.getline(&ser[l][0],100,'\n');

		 for(int i=0;i<n[l];i++ )
		 {
           	 fin.getline(&ser[l][0],100,'\n');
             serc[l][i]=ser[l];
		   }

	 fin>>q[l];

fin.getline(&que[l][0],100);

	for(int i=0;i<q[l];i++)
	{
		fin.getline(&que[l][0],100);
		quer[l][i]=que[l];
		
	}
	}

	for(int l=0;l<c;l++)
	{
		for(int i=0;i<q[l];i++)
	{
	
		for(int j=0;j<n[l];j++)
		{

		  if(serc[l][j]==quer[l][i])
		  {
			  qu[l][i]=j+1;
			 
			  break;
		  }
		 
		  
		  }
	}
	
	ans[l]=algo(qu[l],se[l],q[l],n[l]);
	
	}
	for(int l=0;l<c;l++)
	{
		fout<<"Case #"<<l+1 <<": "<<ans[l]<<"\n";
	}
	getch();
	return 0;
	
}
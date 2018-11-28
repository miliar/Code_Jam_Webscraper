#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

vector <int> ast,bst,aend,bend,c,d;

void sortall()
{
	int n=c.size();
	int t;
	for(int i=0; i<n-1; i++)
	{
		for(int j=i+1; j<n; j++)
		{
			if(c[i]>=c[j])
			{
				t=c[i],c[i]=c[j],c[j]=t;
				t=d[i],d[i]=d[j],d[j]=t;
			}
			
		}
	}
	return;
}

int conv(string s)
{
	int a=0,b=0;
	a=(s[0]-'0')*10 + (s[1]-'0');
	b=(s[3]-'0')*10 + (s[4]-'0');
	a=a*60+b;
	return a;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	
	int n,na,nb,t;
	
	string s,s2;
	
	fin>>n;
	for(int cas=1; cas<=n; cas++)
	{
		ast.clear();
		bst.clear();
		aend.clear();
		bend.clear();
		c.clear();
		d.clear();
		
		fin>>t;
		fin>>na>>nb;
		
		for(int i=0; i<na; i++)
		{
			fin>>s>>s2;
			ast.push_back(conv(s));
			bend.push_back(conv(s2)+t);
		}
		
		for(int i=0; i<nb; i++)
		{
			fin>>s>>s2;
			bst.push_back(conv(s));
			aend.push_back(conv(s2)+t);
		}
		
		for(int i=0; i<na; i++)
		{
			c.push_back(ast[i]);
			d.push_back(0);
		}
		for(int i=0; i<nb; i++)
		{
			c.push_back(aend[i]);
			d.push_back(1);
		}
		
		sortall();
		
		int ansa=0,ansb=0,ctr=0;
		for(int i=0; i<na+nb; i++)
		{
			if(d[i]==0)
			{
				if(ctr==0)
					ansa++;
				else
					ctr--;
			}
			if(d[i]==1)
				ctr++;
		}
		
		//for b
		
		c.clear();d.clear();
		for(int i=0; i<nb; i++)
		{
			c.push_back(bst[i]);
			d.push_back(0);
		}
		for(int i=0; i<na; i++)
		{
			c.push_back(bend[i]);
			d.push_back(1);
		}
		
		sortall();
		
		ctr=0;
		for(int i=0; i<na+nb; i++)
		{
			if(d[i]==0)
			{
				if(ctr==0)
					ansb++;
				else
					ctr--;
			}
			if(d[i]==1)
				ctr++;
		}
		
		fout<<"Case #"<<cas<<": "<<ansa<<" "<<ansb<<"\n";
	}
	
	return 0;
	
}



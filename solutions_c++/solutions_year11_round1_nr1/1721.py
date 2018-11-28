#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;

	char c[1000];
	int tc;
	char *x;
	int i,j,k,n,pd,pg,d,l,l1,d1;

	ifile.open("in");
	ofile.open("out",ios::out);
	
	ifile.getline(c,1000,'\n');			

	tc=atoi(c);
	for(k=0;k<tc;k++)
	{
		d=100;

		ifile.getline(c,1000,'\n');
		x = strtok(c," ");
		n=atoi(x);
		x = strtok(NULL," ");
		pd=atoi(x);
		x = strtok(NULL," ");
		pg=atoi(x);
		
		cout<<n<<" "<<pd<<" "<<pg<<" "<<"\n";

		if(pd==0){d=1;}
		else
		{
			while(pd%5==0 && d%5==0){pd=pd/5;d=d/5;}
			while(pd%2==0 && d%2==0){pd=pd/2;d=d/2;}
			cout<<"pd="<<pd<<" d="<<d;
		}
		
		if(d>n){ofile<<"Case #"<<k+1<<": Broken\n";cout<<"*";}
		else
		{		
			l=d-pd;//pd win, l loss
			cout<<" initial win="<<pd<<" loss="<<l<<"\n";
			d1=100;
			if(pg==0){d1=1;}
			else
			{
				while(pg%5==0 && d%5==0){pg=pg/5;d1=d1/5;}
				while(pg%2==0 && d%2==0){pg=pg/2;d1=d1/2;}
				cout<<"pg="<<pg<<" d1="<<d1;
			}
			l1=d1-pg;cout<<" final win="<<pg<<" loss="<<l1<<"\n";
			if(l1==0 && l!=0){ofile<<"Case #"<<k+1<<": Broken\n";cout<<"*";}
			else if(pg==0 && pd!=0){ofile<<"Case #"<<k+1<<": Broken\n";cout<<"*";}
			else ofile<<"Case #"<<k+1<<": Possible\n";
			/*
			if(pd<=pg && l<=l1){ofile<<"Case #"<<k+1<<": Possible\n";cout<<"!";}
			else {ofile<<"Case #"<<k+1<<": Broken\n";cout<<"*";}*/
		}
		cout<<"\n*****************************\n\n";
		
	}
	
	ofile.close();
	ifile.close();

	return 0;
}

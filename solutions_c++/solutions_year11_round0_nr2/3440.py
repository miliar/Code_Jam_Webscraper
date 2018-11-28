#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;

	int tc,i,j,k,l;
	char c[37][3],d[29][2],n[101];int clen,flagc=0,flagd=0;
	int ci,cl,di,dl,nl;
	char ln[1000],*x;
	
	ifile.open("in");
	ofile.open("out",ios::out);
	
	ifile.getline(ln,10,'\n');////	
	tc=atoi(ln);
	for(k=0;k<tc;k++)
	{
		cout<<"\n***"<<k+1<<"\n";		
		ifile.getline(ln,1000,'\n');
		/////////////////////////////////////////////
		x=strtok(ln," ");
		cl=atoi(x);
		for(i=0;i<cl;i++)
		{
			x=strtok(NULL," ");
			c[i][0]=x[0];
			c[i][1]=x[1];
			c[i][2]=x[2];
		}
		cout<<"\narrays->\nc->";
		for(i=0;i<cl;i++)
			cout<<c[i][0]<<c[i][1]<<c[i][2]<<" ";
		////
		x=strtok(NULL," ");
		dl=atoi(x);
		for(i=0;i<dl;i++)
		{
			x=strtok(NULL," ");
			d[i][0]=x[0];
			d[i][1]=x[1];
		}
		cout<<"\nd->";
		for(i=0;i<dl;i++)
			cout<<d[i][0]<<d[i][1]<<" ";
		////
		x=strtok(NULL," ");
		nl=atoi(x);
		x=strtok(NULL,"\n");
		cout<<"\nx->";
		for(i=0;i<nl;i++)
			cout<<x[i]<<" ";
		cout<<"\n";
		/////////////////////////////////////////////
		
		clen=-1;flagc=0;flagd=0;
		
		for(i=0;i<nl;i++)//processing dynamically
		{
		 if(i==0){clen=0;n[clen]=x[i];}
		 else if(clen==-1){clen=0;n[clen]=x[i];}
		 else
		 {
			for(j=0;j<cl;j++)//check combine logic
			{
				if(x[i]==c[j][0])
					if(n[clen]==c[j][1])
					{
						flagc=1;
						n[clen]=c[j][2];
					}
				if(x[i]==c[j][1] && flagc!=1)
					if(n[clen]==c[j][0])
					{
						flagc=1;
						n[clen]=c[j][2];
					}
			}
			if(flagc!=1)
			{
			for(j=0;j<dl;j++)//check d(oppose) logic
			{
				if(x[i]==d[j][0])
				{
					for(l=0;l<=clen;l++)
						if(n[l]==d[j][1])
						{
							flagd=1;
							clen=-1;
							break;
						}
				}
				if(x[i]==d[j][1] && flagd!=1)
				{
					for(l=0;l<=clen;l++)
						if(n[l]==d[j][0])
						{
							flagd=1;
							clen=-1;
							break;
						}
				}
			}
			}
			
			if(flagc!=1 && flagd!=1)
			{
				clen++;
				n[clen]=x[i];
			}
			flagc=0;flagd=0;
		 }
		 cout<<"x[i]="<<x[i]<<" "<<"clen="<<clen<<"\n";
		}

		cout<<"\nn->";
			
		ofile<<"Case #"<<k+1<<": [";
		for(i=0;i<=clen;i++)
		{
			if(i==clen)ofile<<n[i];
			else ofile<<n[i]<<", ";
		}
		ofile<<"]\n";
	}
	
	ofile.close();
	ifile.close();

	return 0;
}

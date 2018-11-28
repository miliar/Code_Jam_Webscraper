#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;

	char c[1000],p[101];
	int o[101],b[101];
	int tc,oi=0,bi=0,pi=0,pl,ocp=1,bcp=1;
	char *x;
	int i,j,k;
	int opush=0,bpush=0;
	int counter=0;

	ifile.open("in");
	ofile.open("out",ios::out);
	
	ifile.getline(c,1000,'\n');			

	tc=atoi(c);
	for(k=0;k<tc;k++)
	{
		oi=0;bi=0;pi=0;

		ifile.getline(c,1000,'\n');
		x = strtok(c," ");
		pl=atoi(x);

		for(i=0;i<pl;i++)
		{
			x = strtok(NULL," ");
			if( strcmp(x,"B")==0 )p[pi]='B';
			else if( strcmp(x,"O")==0 )p[pi]='O';

			x = strtok(NULL," ");
			if(p[pi]=='B')b[bi++]=atoi(x);
			else if(p[pi]=='O')o[oi++]=atoi(x);
			
			pi++;
		}

		oi=0;bi=0;pi=0;ocp=1;bcp=1;counter=0;
		while(pi<pl)
		{
			if(p[pi]=='O')
			{
				if(ocp==o[oi])//push
				{
					opush=1;
					pi++;oi++;
				}
			}
			else if(p[pi]=='B')
			{
				if(bcp==b[bi])//push
				{
					bpush=1;
					pi++;bi++;
				}
			}
			if(opush!=1)
			{
				if(ocp<o[oi])ocp++;
				else if(ocp>o[oi])ocp--;
			}
			if(bpush!=1)
			{
				if(bcp<b[bi])bcp++;
				else if(bcp>b[bi])bcp--;
			}
			opush=0;bpush=0;
			counter++;cout<<"out pi="<<pi<<" oi="<<oi<<" bi="<<bi<<"\n";
		}
		ofile<<"Case #"<<k+1<<": "<<counter<<"\n";
	}
	
	ofile.close();
	ifile.close();

	return 0;
}

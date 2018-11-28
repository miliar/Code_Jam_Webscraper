#include <iostream>
#include <fstream>
using namespace std;

int main()
{
int T; //no of test cases
cin>>T;
ifstream ifile;
ifile.open("freecell-input.txt");
ofstream ofile;
ofile.open("freecell-output.txt");

for(int main =0 ; main<T ; main++)
{
double N=0, Pd = 0, Pg =0, P=0, G=0; // N-no of games played today
char chTemp;
//pd - % of games won today
//pg - % of games won overall
//P - games played today
//G - total games played till date

ifile>>N;
ifile.get(chTemp);
ifile>>Pd;
ifile.get(chTemp);
ifile>>Pg;
ifile.get(chTemp);

cout<<"\n Case :"<<main<<" N :"<<N<<" Pd :"<<Pd<<"Pg :"<<Pg;
double ptemp =0 , gtemp = 0, floattemp=0;
int temp=0;
bool bpfound = false;
bool bgfound = false;
bool bpossible = false;
for(int i=1;i<=N;i++)
{
	bpfound = false;
	bgfound = false;
	ptemp = (i*Pd)/100.0;
	cout<<"\n ptemp :"<<ptemp<<" i : "<<i;
	temp = (int)ptemp;
	floattemp = temp;
	if(floattemp == ptemp)
	{	
		bpfound = true;
		cout<<"\n bpfound temp : "<<temp<<" floattemp: "<<floattemp;
	}
	
	if(bpfound)
	{
		for(int j=N;;j++)
		{
			bpossible = false;
			bgfound = false;
			gtemp = (j*Pg)/100.0;
			cout<<"\n gtemp :"<<gtemp;
			temp = (int)gtemp;
			floattemp = temp;
			if(floattemp == gtemp)
			{
				bgfound = true;
				cout<<"\n bgfound temp : "<<temp<<" floattemp: "<<floattemp<<" j :"<<j<<" Pg :"<<Pg ;
			}
			
			if(Pg == 100 && Pd!= 100)
			{
				bpossible = false;
				break;
			}
			if(Pg==0 && Pd!=0)
			{
				bpossible = false;
				break;
			}
			
			if(bgfound)
			{
				if(gtemp>=ptemp)
				{
					cout<<"\n bpossible gtemp: "<<gtemp<<" ptemp : "<<ptemp<<"\n";
					bpossible = true;
					break;
				}
			}	
			
		}
	}	
if(bpossible)
	break;
}

if(bpossible && bpfound && bgfound)
	{
	ofile<<"\nCase #"<<main+1<<": Possible";
	cout<<"\n Possible \n";
	}

else
	{
	ofile<<"\nCase #"<<main+1<<": Broken";
	cout<<"\n broken \n";
	}
	


 	
}//end of main
ofile.close();
ifile.close();
}//end of program

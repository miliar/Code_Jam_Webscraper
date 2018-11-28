#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;

int max(int a,int b)
{
	return (a>b)?a:b;
}
int main()
{
 	int t,i=1;
	ifstream ifile ("smallA.txt");
	ofstream ofile ("output.txt");
	ifile>>t;
	int to,tb,stateO,stateB,n,dest;
	char ch;
	while(t)
	{
		to=tb=0;
		stateO = stateB = 1;		
		ifile>>n;
		while(n)
		{
			
			ifile>>ch;
			switch(ch)
			{
				case 'O': ifile>>dest;
					  if(to < tb)
					  {
						to += max(abs(dest-stateO),abs(tb-to));
					        to++;
						stateO = dest;
						
					  }
					  else
					  {
						to += abs(dest-stateO)+1;
						stateO = dest;
					  }
					  //cout<<"O :"<<to<<" "<<stateO<<"\n";
					  break;
				case 'B': ifile>>dest;
					  if(tb < to)
					  {
						tb += max(abs(dest-stateB),abs(tb-to));
					        tb++;
						stateB = dest;
					  }
					  else
					  {
						tb += abs(dest-stateB)+1;
						stateB = dest;
					  }
					  //cout<<"B :"<<tb<<" "<<stateB<<"\n";
					  break;
			}
			n--;
			
		}	
		ofile<<"Case #"<<i<<": "<<max(to,tb)<<"\n";
		t--;
		i++;
	}
	ifile.close();
	ofile.close();
	return 0;
}

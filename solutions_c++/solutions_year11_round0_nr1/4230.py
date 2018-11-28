#include<iostream>
#define SIZE 10
using namespace std;
void read();
class robot
{
	int orange[SIZE],blue[SIZE];
	int sec;
	int o,b;
	int sequence[2*SIZE];
	int oposition,bposition;//button number
	int onext,bnext;//index
	int buttons;
	public:
		void read();
		void calculate();
};
int main()
{
	int count,i;
	robot r;
     //	clrscr();
	cin>>count;
	for(i=0;i<count;i++)
	{
		r.read();
		cout<<"\nCase #"<<(i+1)<<": ";
		r.calculate();
	}
	return 0;
}
void robot::calculate()
{

	int next;
	oposition=1;
	bposition=1;
	onext=0;bnext=0;
	sec=0;
	int press;
//	cout<<"buttons"<<buttons;
	int binc,oinc;
	for(press=0;press<buttons;sec++)
	{
		if(oposition<orange[onext])
		{
			oinc=1;
		}
		else if(oposition>orange[onext])
			oinc=-1;
		else
			oinc=0;
		if(bposition<blue[bnext])
		{
			binc=1;
		}
		else if(bposition>blue[bnext])
			binc=-1;
		else
			binc=0;
	  /*	if(onext==o)
			oinc=0;
		if(bnext==b)
			binc=0;  */

  //		cout<<oinc<<":"<<binc<<"\t";
		if(sequence[press]>100)
			next=0;//ORANGE
		else
			next =1;//blue
		if(oposition!=orange[onext]&&bposition!=blue[bnext])
		{
    //			cout<<"o++ b++\n";
			oposition+=oinc;
			bposition+=binc;
		}
		else if(oposition!=orange[onext]&&bposition==blue[bnext])
		{
			if(next==1)
			{
      //				cout<<"b(press)";
				press++;
				bnext++;
			}

			oposition+=oinc;
		}
		else if(oposition==orange[onext]&&bposition!=blue[bnext])
		{
			if(next==0)
			{
  //				cout<<"o(press)";
				press++;
				onext++;
			}

			bposition+=binc;
		}
		else
		{
			if(next==0)
			{
				press++;
				onext++;
			}
			else
			{
				press++;
				bnext++;
			}
		}

	}
	cout<<sec;
	}
void robot::read()
{
	int o=0,b=0,count,i;
	char choice;
	for(i=0;i<SIZE;i++)
	{
		orange[i]=0;
		blue[i]=0;
	}
	sec=0;
	oposition=0;
	bposition=0;
	onext=0;
	bnext=0;
	cin>>count;
	buttons=count;
	for(i=0;i<count;i++)
	{
		cin>>choice;
		if(choice=='O')
		{
			cin>>orange[o];
			o++;
			sequence[i]=100+orange[o-1];
		}
		else if(choice=='B')
		{
			cin>>blue[b];
			b++;
			sequence[i]=blue[b-1];
		}

	}
	orange[o]=orange[o-1];
	blue[b]=blue[b-1];
      //	orange[0]=o-1;
      //	blue[0]=b-1;

  /*
	{
	 for(i=0;i<o;i++)
		cout<<orange[i];
	 for(i=0;i<b;i++)
		cout<<blue[i];
		cout<<"\n";
	for(i=0;i<count;i++)
		cout<<sequence[i]<<":";

	} */

}

#include <iostream>
using namespace std;
#include<fstream>
#include <string>
void main(){
	char ch;
	int xb [101],xo[101];
	int T1, T2;
	string infile,outfile;
	ifstream source;
	bool flago,flagb;
	ofstream target;
	infile = "A-large.in";
	outfile = "OutfileLarge.txt";
	int N;
	int T;
	int io ;
	int ib ;

	

	source.open(infile.c_str());
	target.open(outfile.c_str());
	
	source >>T;
	for ( int k =1; k<= T;k++)
{
		for ( int i =0; i<100;i++)
	{
		xo[i]=1;
		xb[i]=1;
		}
	flagb = false;
	flago = false;
	 io =1;
	 ib = 1;
	 T1 =0;
	 T2=0;

	source >> N;

for ( int j = 1; j <= N; j++)
{
	source >> ch;

if ( ch == 'O') 
{	
	source >> xo[io];
	if (!(flagb))
	{
		if (xo[io-1] == 0)
			T1 = xo[io];
		else
			if ( xo[io] > xo[io-1])
				T1 = T1 + (xo[io] - xo[io-1] +1);
			else
				T1 = T1 + (xo[io-1] - xo[io] +1);
	}
	else
	{
		if ( xo[io] > xo[io-1])
		{
		if ( xo[io]- xo[io-1]+T1 >= T2)
		{
			if ( xo[io] > xo[io-1])
				T1 = T1 + (xo[io] - xo[io-1] +1);
			else
				T1 = T1 + (xo[io-1] - xo[io] +1);
		}
		else
			T1 = T2 + 1;
		}
		else
		{
			if (  xo[io-1]-xo[io] + T1>= T2)
		{
			if ( xo[io] > xo[io-1])
				T1 = T1 + (xo[io] - xo[io-1] +1);
			else
				T1 = T1 + (xo[io-1] - xo[io] +1);
		}
		else
			T1 = T2 + 1;
		}
	}
	flago = true;
	flagb = false;
	io++;
}
else 
{
	source >> xb[ib];
	
	if (!flago)
	{if (xb[ib-1] == 0)
			T2 = xb[ib];
		else
			if( xb[ib] > xb[ib-1] )
				T2 = T2 + (xb[ib] - xb[ib-1] +1);
			else
				T2 = T2 + (xb[ib-1] - xb[ib] +1);
	}
	else
	{
		if( xb[ib] > xb[ib-1] ){
		if ( xb[ib]- xb[ib-1]+T2>=T1)
		{
			if( xb[ib] > xb[ib-1] )
				T2 = T2 + (xb[ib]- xb[ib-1] +1);
			else
				T2 = T2 + (xb[ib-1] - xb[ib] +1);
		}
		else
			T2 = T1 + 1;
		}
		else {
			if ( xb[ib-1]-xb[ib]+T2>=T1)
		{
			if( xb[ib] > xb[ib-1] )
				T2 = T2 + (xb[ib]- xb[ib-1] +1);
			else
				T2 = T2 + (xb[ib-1] - xb[ib] +1);
		}
		else
			T2 = T1 + 1;
		}
	}
	flago = false;
	flagb = true;
	ib++;
}

}



if (T1>T2)
	target <<"Case #" << k <<": " << T1 << endl;
else 
	target <<"Case #" << k <<": " << T2 << endl;


}

}


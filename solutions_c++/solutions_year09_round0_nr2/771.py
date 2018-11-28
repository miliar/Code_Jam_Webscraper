#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <conio.h>
//#include<>
using namespace std;


int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("B-large.in",ios::in);
    out.open("b.out",ios::out);
	int n,N,H,W,i,j,infty=1000000,ti,tj;
	char c,tc;
	bool sink;
    in >> N;
	int table[102][102];
	char ch[102][102];
	vector <int> si(0,0), sj(0,0);
    for (n=1;n<=N;n++)
    {
		for (i=0;i<102;i++) for (j=0;j<102;j++)
		{
			table[i][j]=infty;
			ch[i][j]='-';
		};
		in>>H>>W;
		for (i=1;i<=H;i++) for (j=1;j<=W;j++) 
		{
			in>>table[i][j];
		};
		tc='a';
		for (i=1;i<=H;i++) for (j=1;j<=W;j++)
		{

			if (ch[i][j]=='-')
			{
				si.clear();
				sj.clear();
				ti=i;
				tj=j;
				sink=false;
				do
				{
					if ( (table[ti-1][tj]<table[ti][tj])&&
						 (table[ti-1][tj]<=table[ti][tj-1])&&
						 (table[ti-1][tj]<=table[ti+1][tj])&&
						 (table[ti-1][tj]<=table[ti][tj+1]) )
						 {
							si.push_back(ti);
							sj.push_back(tj);
							ti=ti-1;
						 }
					else 
					if ( (table[ti][tj-1]<table[ti][tj])&&
						 (table[ti][tj-1]<=table[ti][tj+1])&&
						 (table[ti][tj-1]<=table[ti+1][tj])&&
						 (table[ti][tj-1]<=table[ti-1][tj]) )
						 {
							si.push_back(ti);
							sj.push_back(tj);
							tj=tj-1;
						 }
					else
					if ( (table[ti][tj+1]<table[ti][tj])&&
						 (table[ti][tj+1]<=table[ti][tj-1])&&
						 (table[ti][tj+1]<=table[ti+1][tj])&&
						 (table[ti][tj+1]<=table[ti-1][tj]) )
						 {
							si.push_back(ti);
							sj.push_back(tj);
							tj=tj+1;
						 }
					else
					if ( (table[ti+1][tj]<table[ti][tj])&&
						 (table[ti+1][tj]<=table[ti][tj-1])&&
						 (table[ti+1][tj]<=table[ti-1][tj])&&
						 (table[ti+1][tj]<=table[ti][tj+1]) )
						 {
							si.push_back(ti);
							sj.push_back(tj);
							ti=ti+1;
						 }
					else {sink=true;};
						 					
				} while ((!sink)&&(ch[ti][tj]=='-'));
				if (ch[ti][tj]!='-')
				{
					c=ch[ti][tj];
				}
				else
				{
					c=tc;				
					tc++;
					si.push_back(ti);
					sj.push_back(tj);

				};
				while (!si.empty())
				{
					ti=si.back();
					tj=sj.back();
//					cout<<ti<<" "<<tj<<" "<<c<<"\n";
					si.pop_back();
					sj.pop_back();
					ch[ti][tj]=c;
//				    getch();
				};			
			};
		};
		out<<"Case #"<<n<<":\n";
		for (i=1;i<=H;i++)
		{
			for (j=1;j<=W;j++) out<<ch[i][j]<<" ";
			out<<"\n";
		};
	};
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}

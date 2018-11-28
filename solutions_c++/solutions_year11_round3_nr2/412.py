#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
#include <algorithm>
#include<iomanip>
using namespace std;

double result=0;//****************************************
int N,C,L;
double t;
struct node{
	double len;
	int n;
};
node Lst[1003]={0};

int cmp( const node &a, const node &b ){
    if( a.len > b.len )
       return 1;
    else
       return 0;
}


int main()
{
ifstream in;
ofstream out;
in.open("B-large.in");
out.open("OUTPUT.txt");


int T;
double left;
in>>T;


for(int Case=1;Case<=T;Case++){
	double sum=0;
	double total=0;
	double f=0;
	in>>L>>t>>N>>C;
	for(int i=0;i<C;i++){
		in>>Lst[i].len;
		Lst[i].n=0;
		sum+=Lst[i].len;
	}
	int j=0;
	for(i=0;i<N;i++){
		f+=Lst[j].len;
		Lst[j].n++;
		j++;
		j=j%C;
	}
	total+=t;
	t/=2;
	
	int done=floor(t/sum);
	int over=0;
	for(i=0;i<C;i++){
	Lst[i].n-=done;
	if(Lst[i].n<0)over=1;
	}
	if(over==1)
	{	

		out<<"Case #"<<Case<<": "<<fixed<<setprecision(0)<<2*f<<endl;			
		continue;

	}
	t-=done*sum;
	double dst=0;
	for(i=0;dst<=t;i++){
		i=i%C;
		dst+=Lst[i].len;
		if(dst>t){dst-=Lst[i].len;
			Lst[i].n--;
			break;
		}
		Lst[i].n--;
		
	}
	left=Lst[i].len-t+dst;
	Lst[C].len=left;

	Lst[C].n=1;
	sort(Lst,Lst+C+1,cmp);
	int k=0;
	for( i=0;i<C+1;i++){
		k=k+Lst[i].n;
		if(k<=L)total+=Lst[i].len*Lst[i].n;
		else if(k>L&&k-Lst[i].n<L)total+=Lst[i].len*(L-k+Lst[i].n)+2*Lst[i].len*(k-L);
		else total+=Lst[i].len*Lst[i].n*2;

	}
	out<<"Case #"<<Case<<": "<<fixed<<setprecision(0)<<total<<endl;	



}

in.close();
out.clear();
out.close();
return 0;
}
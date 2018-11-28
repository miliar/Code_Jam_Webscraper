#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>


using namespace std;

int abs(int a)
{if (a<0) return -a;
else return a;}

int max(int a , int b)
{ if (a>b) return a;
else return b;}
int min(int a , int b)
{if (a<b) return a;
else return b;}




int main(){
	ifstream input;
	input.open("prueba.dat");
	ofstream output;
	output.open("output.dat");

	long long l,t,n,c,tmax,temp;



	input>>tmax;


	vector<long long> num,tiempos,tiemp,index;

	for (int s=1; s<=tmax;s++)
	{
		l=0; t=0; n=0; c=0;
		input>>l>>t>>n>>c;		num.clear();
		for (int i=0; i<c;i++)
		{
			input>>temp;
			num.push_back(temp);
		}
		
		for (int i=0; i<(n-c);i++)
		{
			num.push_back(num[i-c*(i/c)]);
		}
		
		tiempos.clear();
		tiempos.push_back(2*num[0]);
		for (int i=1; i<n;i++)
		{
			tiempos.push_back(tiempos[i-1] + 2*num[i]);
		}
		
		tiemp.clear();
		if (t < tiempos[0]) tiemp.push_back(tiempos[0]-t);
		else tiemp.push_back(0);

		
		for (int i=1; i<n;i++)
		{
			if (t < tiempos[i-1]) tiemp.push_back(2*num[i]);
			else {
				if (t < tiempos[i]) 
				tiemp.push_back(2*num[i]+(tiempos[i-1]-t));
				else tiemp.push_back(0);}
		}
		
		index.clear();
		if (l>0)
		{
		index.push_back(0);
		for (int j=0;j<n;j++)
			{ if (tiemp[j]>tiemp[index[0]]) index[0]=j;}}
		
		if (l==2)
		{index.push_back(0);
			for (int j=0;j<n;j++)
			{ if (tiemp[j]>tiemp[index[1]] and j!=index[0]) index[1]=j;}}
		
		for (int j=0;j<n;j++)
			{ if (l>0 and j==index[0]) tiempos[n-1]-=tiemp[index[0]]/2;
			if (l== 2 and j==index[1]) tiempos[n-1]-=tiemp[index[1]]/2;}

		output<<"Case #"<<s<<": "<<tiempos[n-1]<<"\n";
		

		
	}
	
	output.close();
	input.close();
	
	return 0;
					

}

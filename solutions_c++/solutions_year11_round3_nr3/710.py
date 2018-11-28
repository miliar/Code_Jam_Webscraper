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

static int EuclidesMCD(int a, int b) {
   int iaux; //auxiliar
   a = abs(a); //tomamos valor absoluto
   b = abs(b);
   int i1=max(a,b); //i1 = el más grande
   int i2=min(a,b); //i2 = el más pequeño
   do
   {
      iaux = i2;  //guardar divisor
      i2 = i1 % i2; //resto pasa a divisor
      i1 = iaux;  //divisor pasa a dividendo
   } while (i2 != 0);
   return i1; //ultimo resto no nulo
}

static int EuclidesMCM(int a, int b)
{
    return (a / EuclidesMCD(a, b)) * b;
}


int main(){
	ifstream input;
	input.open("prueba.dat");
	ofstream output;
	output.open("output.dat");

	int t,n,l,h,temp,mcm;
	bool pos;
	int j;

	input>>t;

	vector<int> num;

	for (int s=1; s<=t;s++)
	{
		mcm=1;
		input>>n>>l>>h;
		num.clear();
		for (int i=0; i<n;i++)
		{
			input>>temp;
			num.push_back(temp);
		}

		pos=true;
		output<<"Case #"<<s<<": ";
		for (int i=l; i<=h;i++)
		{	temp=0;
			for (int k=0; k<n; k++)
			{j=num[k];
				if (i>j and ((i/j)*j-i)==0) temp++;
				if (i<=j and ((j/i)*i-j)==0) temp++;}
		if (temp==n) {output<<i<<"\n"; i=h+1;pos=false;}
		}

		if (pos) output<<"NO\n";
		

		
	}
	
	output.close();
	input.close();
	
	return 0;
					

}

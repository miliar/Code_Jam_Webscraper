// CodeJam 2011 - Qualification Round - Candy Splitting
#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;


string decbin(int n)
{
   string bin;
   while(n>0)
   {
	bin.insert(0, 1, (n%2)+48);
	n /= 2;
   }
   return bin;
}
string doublebin(double n)
{
   string bin;
   while(n>0.0)
   {
	bin.insert(0, 1, (int)(fmod(n,2))+48);
	if(n < 10)
	   n = (int)(n/2);
	else
	   n /= 2;
   }
   return bin;
}
int bindec(string bin)
{
   int dec = 0, t = 0;
   while(bin.size())
   {
	dec += pow(2,t++)*(bin.at(bin.size()-1)-48);
	bin.resize(bin.size()-1);
   }
   return dec;
}
double bindouble(string bin)
{
   double dec = 0;int t = 0;
   while(bin.size())
   {
	dec += pow(2,t++)*(bin.at(bin.size()-1)-48);
	bin.resize(bin.size()-1);
   }
   return dec;
}
string patrick_add(string num1, string num2)
{
   string result;
   while(num1.size() && num2.size())
   {
	result.insert(0,1, ((num1.at(num1.size()-1)-48 + num2.at(num2.size()-1)-48)%2)+48);
	num1.resize(num1.size()-1); num2.resize(num2.size()-1);
   }
   while(num1.size())
   {
	result.insert(0,1, num1.at(num1.size()-1));
	num1.resize(num1.size()-1);
   }
   while(num2.size())
   {
	result.insert(0,1, num2.at(num2.size()-1));
	num2.resize(num2.size()-1);
   }
   return result;
}


int main()
{
   int T, N, *elem, i, j, tmp, max;
   bool flag;
   ifstream infile("C-small-attempt0.in");
   ofstream outfile("C-small.out");

   infile >> T;
   for(i=1; i<=T; i++)
   {
	infile >> N;
	elem = new int[N];
	for(j=0; j<N; j++)
	{
	    infile >> tmp;
	    elem[j] = tmp;
	}

	max = -1; flag = false;
	string part_denote;
	part_denote.insert(0, N, '0');
	while((bindouble(part_denote)+1) < pow(2,N))
	{
		if(!flag)
		{
		   flag = true;
		}
		else
		{
		   part_denote = doublebin(bindouble(part_denote) + 1);
		   part_denote.insert(0, N-part_denote.size(), '0');
		}
		string multiplier;
		multiplier.insert(0, N-1, '0'); multiplier.insert(0,1,'1');
		int ti = 0;
		int sum_sean = 0, sum_patrick = 0, sum_p_sean = 0;
		while(ti < N)
		{
		   int bw = (int)(part_denote.at(ti)-48) * (int)(multiplier.at(ti)-48);
		   // Scheme 1 => 1-Sean, 0-Patrick
		   if(bw) // Goes to Sean
		   {
		   	sum_sean += elem[ti];
			sum_p_sean = bindec(patrick_add(decbin(sum_p_sean), decbin(elem[ti])));
		   }
		   else
			sum_patrick = bindec(patrick_add(decbin(sum_patrick), decbin(elem[ti])));

		   multiplier = doublebin(bindouble(multiplier)/2);
		   multiplier.insert(0, N-multiplier.size(), '0');
		   ti++;
		}
		if(sum_p_sean == sum_patrick && sum_patrick>0 && sum_sean > max)
		   max = sum_sean;

		multiplier = "0";
		multiplier.insert(0, N-2, '0'); multiplier.insert(0,1,'1');
		ti = 0; sum_sean = 0; sum_patrick = 0; sum_p_sean = 0;
		while(ti < N)
		{
		   int bw = (int)(part_denote.at(ti)-48) * (int)(multiplier.at(ti)-48);
		   // Scheme 2 => 0-Sean, 1-Patrick
		   if(!bw) // Goes to Sean
		   {
		   	sum_sean += elem[ti];
			sum_p_sean = bindec(patrick_add(decbin(sum_p_sean), decbin(elem[ti])));
		   }
		   else
			sum_patrick = bindec(patrick_add(decbin(sum_patrick), decbin(elem[ti])));
		   
		   multiplier = doublebin(bindouble(multiplier)/2);
		   multiplier.insert(0, N-multiplier.size(), '0');
		   ti++;
		}
		if(sum_p_sean == sum_patrick && sum_patrick>0 && sum_sean > max)
		   max = sum_sean;
	}
	
	if(max == -1)
		outfile << "Case #" << i << ": NO" << endl;
	else
		outfile << "Case #" << i << ": " << max << endl;
	delete[] elem;
   }
   infile.close();
   outfile.close();
   return 0;
}


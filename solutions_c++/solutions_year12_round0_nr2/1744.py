#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main()
	 {
		 	ifstream in;
	   in.open("B-large.in");
	   ofstream out;
  out.open ("Answer.txt");
	   int T;
	   int N;
	   int p;
	   int s;
	   int result =0;
	   vector <int> scores;
	   string line;
	   in>>T;
	   getline (in,line);
for(int i=0;i<T;i++)
{
	out<<"Case #"<<i+1<<": ";
	in>>N;
	in>>s;
	in>>p;
	for(int x=0;x<N;x++)
	{   int temp;
		in>>temp;
		scores.push_back(temp);
	}
	sort(scores.begin(),scores.end());
	for(int x=0;x<scores.size();x++)
	{
		if(s!=0)
		{   
			int one;
		    int two;
			int remain = scores[x]-p;
			if(remain>=0)
			{
			if(remain%2==1)
			{
				one=remain/2;
				two=one+1;
				if(p-one<=2)
				result++;
			    if(p-one==2)
					s--;
			}
			else
			{
			  one=two=remain/2;
			  if(p-one<=2)
				  result++;
			  if(p-one==2)
					s--;
			}
			}
		}
		else
		{
			int one;
		    int two;
			int remain = scores[x]-p;
			if(remain>=0)
			{
			if(remain%2==1)
			{
				one=remain/2;
				two=one+1;
				if(p-one<2)
				result++;
			}
			else
			{
			  one=two=remain/2;
			 
			  if(p-one<2)
				  result++;
			}
			}
		}
	}
	if(i!=T-1)
	{
	out<<result<<endl;
	result=0;
	scores.erase(scores.begin(),scores.end());
	}
	else
		out<<result;


}

	return 0;

  
     }
  

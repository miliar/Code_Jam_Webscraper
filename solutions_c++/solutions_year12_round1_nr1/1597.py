#include <stdio.h>
#include <iostream>
#include <iterator>
#include<fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <sstream>


using namespace std;



int main(int argc, char *argv[])
{

	ifstream infile;
	infile.open("input.in",ifstream::in);
	ofstream outfile;
	outfile.open("output.in",ofstream::out);
	int t;

		infile>>t;




		for (int tt=0;tt<t;tt++)
			{
			int A,B;
			vector<float>prob;
			infile>>A>>B;
			float pr_no=1;
			float avg[1000000];
			for(int aa=0;aa<A;aa++)
			{
				float temp;
				infile>>temp;
				prob.push_back(temp);
				pr_no=pr_no*temp;

			}
			int backstrok=1;
			avg[0]=((B-A+1)*pr_no)+((2*B-A+2)*(1-pr_no));
			for(vector<float>::reverse_iterator rit=prob.rbegin();rit<prob.rend();rit++)
			{
				pr_no=pr_no/(*rit);
				avg[backstrok]=((B-A+1+2*backstrok)*pr_no)+((2*B-A+2+2*backstrok)*(1-pr_no));
				backstrok++;

			}
			float avg2=B+2;
			float mins=99999999999;
			float mini=0;
			for(int i=0;i<A;i++)
			{
				if(avg[i]<mins)
				{
					mins=avg[i];
					mini=i;
				}
			}
			outfile.precision(6);

			if(mins>avg2) outfile<<"Case #"<<tt+1<<": "<<avg2<<'\n';
			else outfile<<"Case #"<<tt+1<<": "<<mins<<'\n';









			}// end of tt
}





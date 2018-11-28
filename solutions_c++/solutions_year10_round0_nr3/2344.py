#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	string fn = "C-small-attempt0.in";
	
	ifstream input;
	input.open(fn.c_str());
	if(input.fail())
	{
		cerr<<"File failed\n";
		return -1;
	}
	
	
	int T,N;
	long long k,R;
	long long group;
	
	input>>T;
	
	long long bit;
	ofstream output;
	fn = fn.substr(0,fn.length()-2)+"out";
	output.open(fn.c_str());
	long long total_cost =0;
	
	for(int i=1; i<=T; i++)
	{
		total_cost =0;
		input>>R>>k>>N;
	
		int* groups = new int[N];
		for(int j=0; j<N; j++)
		{
			input>>groups[j];
		}
		int inc= 0;
		int begin; 
		
		long long total_money = 0;
		for(int r= 1; r<=R; r++)
		{
			total_cost = 0;
			begin = inc;
			bool back_to_begin = false;
			while(total_cost<=k && !back_to_begin)
			{
				
				
				total_cost += groups[inc];
				inc++;
				
				
				
			
				if(inc == N)
					inc=0;
				
				if(inc == begin)
				{
					back_to_begin=true;
				}
				
				
			}
			
			if(!back_to_begin || total_cost>k)
			{
			
				if(inc ==0)
					inc = N-1;
				else 
				{
					inc--;
				}
				
				total_money += (total_cost-groups[inc]); 	
			}
			else
			{
				total_money += total_cost;
			}
			//cout<<total_money<<endl;
		
		}
		//cout<<endl;
		delete [] groups;
		output<<"Case #"<<i<<": "<<total_money<<endl;
	}

	input.close();
	output.close();
	
	return 0;
}

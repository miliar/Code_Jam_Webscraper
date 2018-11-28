#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
ifstream fin;
ofstream fout; 
fin.open("C-small-attempt0.in");
fout.open("test.out");

int tc_count;
int R, k ,N; 
int total_mount=0;
int val[1000];
int now_ptr; 
int n =0;
int m =0; 

fin>>tc_count;
while(n < tc_count)
{
	now_ptr=0; 
	total_mount=0;

	fin>>R>>k>>N;
	//cout<<"R:"<<R<<endl;
	//cout<<"k:"<<k<<endl;
	//cout<<"N:"<<N<<endl;
	m=0;
	//cout<<"1"<<endl;
	while (m<N)
	{
	fin>>val[m]; 
	m++;
	}

	m=0; 
	//cout<<"2"<<endl;
	while(m<R)
	{
	int temp_val=0; 
	int first = now_ptr;
		while(1)
		{
			
			temp_val += val[now_ptr];

			if(temp_val<= k)
				now_ptr++;
			else
				break;

		if(now_ptr==N)
			now_ptr=0;

		if(first==now_ptr)
			break;
		}
		if(first==now_ptr)
		total_mount += temp_val;
		else
			total_mount += temp_val-val[now_ptr];
		
	m++;
	}
	 
	

	
		fout<<"Case #"<<n+1<<": "<<total_mount<<endl;
	
n++; 
}
//cout<<"3"<<endl;
	

return 0;
}
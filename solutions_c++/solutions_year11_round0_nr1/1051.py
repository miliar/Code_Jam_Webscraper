#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	int n;
	char r;
	int b;

	int O=1;
	int B=1;
	int dt=0;;
	int time=0;
	in>>n;
	char cur;
	for (int i=0; i<n; i++)
	{
		int k;
		in>>k;
		out<<"Case #"<<i+1<<": ";
		time=0;
		B=1;
		O=1;
		dt=0;
		for (int j=0; j<k; j++)
		{
			in>>r>>b;
			if (time==0 && dt==0) cur=r; 
			if (r=='O')
			{
				if (cur==r)
				{
					//time+=dt;
				dt += abs(b-O)+1;
				O=b;
				
				}
				else
				{
					cur=r;
					time+=dt;
					if (dt>=abs(b-O))
					{
						O=b;
						dt=1;
					}
					else 
					{
						dt=abs(dt-abs(b-O))+1;
						O=b;
					}
				}
			}
			else 
			{
				if (cur==r)
				{
				
				dt += abs(b-B)+1;
				B=b;
				
				}
				else
				{
					cur=r;
					time+=dt;
					if (dt>=abs(b-B))
					{
						B=b;
						dt=1;
					}
					else 
					{
						dt=abs(dt-abs(b-B))+1;
						B=b;
					}
				}
			}
		}
		
		time+=dt;
		

		out<<time<<endl;
	}


	in.close();
	out.close();
	return 0;
}
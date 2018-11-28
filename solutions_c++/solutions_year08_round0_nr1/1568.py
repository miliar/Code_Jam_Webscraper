// stu.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	ifstream in_stream;
	ofstream out_stream;

	in_stream.open("A-small.in");
	out_stream.open("A-small.out");

	//in_stream.open("A-large.in");
	//out_stream.open("A-large.out");
	
	int number_of_cases;
	int number_of_servers;
	int number_of_queries;
	int i,j,k,l;

	int servers_found;
	bool server_found[100];
	char servers[100][100];
	char query[100];
	bool flag;

	int switches;

	in_stream>>number_of_cases;
	for(i=0;i<number_of_cases;++i)
	{
		in_stream>>number_of_servers;
		in_stream.get();
		for(j=0;j<number_of_servers;++j)
		{
			in_stream.getline(servers[j],100,'\n');
		}
		in_stream>>number_of_queries;
		in_stream.get();
		switches=0;
		for(j=0;j<number_of_servers;++j)
		{
			server_found[j]=false;
		}
		servers_found=0;
		flag=true;
		for(j=0;j<number_of_queries;++j)
		{	
			if(flag)
			{
				in_stream.getline(query,100,'\n');
			}
			flag=true;
			for(k=0;k<number_of_servers;++k)
			{
				if(server_found[k]==false)
				{
					if(!strcmp(servers[k],query))
					{
						server_found[k]=true;
						servers_found++;
						if(servers_found==number_of_servers)
						{
								switches++;
								flag=false;
								j--;
							
							for(l=0;l<number_of_servers;++l)
							{
								server_found[l]=false;
							}
							servers_found=0;
						}
						break;
					}
				}
			}
		}
		out_stream<<"Case #"<<i+1<<": "<<switches<<endl;
	}

	return 0;
}


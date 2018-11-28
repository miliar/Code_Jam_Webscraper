// GoogleJam1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
void main()
{
	char temp1[1024];
	char* token;
	fstream input,output;
	input.open("D://1.txt");
	input.getline(temp1,1024);
	output.open("D://2.txt");
	int count=atoi(temp1),Case=1;
	while(count--)
	{
		char temp[1024];
		input.getline(temp,1024);
		int N=atoi(strtok(temp," "));
		int S=atoi(strtok(NULL," "));
		int P=atoi(strtok(NULL," "));
		token=strtok(NULL," ");
		int total,max=0;
		while(token)
		{
			total=atoi(token);
			token=strtok(NULL," ");
			int pass=0;
			if(total<P ||( (3*P)-2>total&&S==0)) continue;
			for(int best=P;((3*best)-2)<=total;best++)
			{
				if(total == 3*best ||total == (3*best)-1 || total == (3*best)-2)
				{
					max++;
					pass++;
					break;
				}
			}
			if(S>0 && pass==0)
			{	
				for(int best=P;((3*best)-4)<=total;best++)
				{
					if(total == 3*best ||total == (3*best)-1 || total == (3*best)-2 || total == (3*best)-3  || total == (3*best)-4 )
					{
						max++;
						pass++;
						break;
					}
				}
				if(pass==1) S--;
			}
		}
		if(max>N) max=N;
		output<<"Case #"<<Case++<<": "<<max<<endl;
	}
	output.close();
}


#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>


using namespace std;


void main()
{
	string line;
	string num;

	std::freopen("output_DanceL.txt", "w", stdout);
	ifstream file("B-large.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	int count=0;
	
	int N, S, p, c=0;
	file>>num;
	c=atoi(num.c_str());
	
	//while(!file.eof())
	for(int x=0;x<c;x++)
	{
		cout<<"Case #"<<x+1<<": ";

		//getline(file,line,'\n');
		
		count=0;
		int loop=3;;
		
		file>>num;
		N=atoi(num.c_str());

		file>>num;
		S=atoi(num.c_str());

		file>>num;
		p=atoi(num.c_str());
		
		int* t;
		t=new int[N];

		for(int i=0;i<N;i++)
		{
			file>>num;
			t[i]=atoi(num.c_str());
			
			if(t[i]>=3*p-2&&t[i]>=p/*&&t[i]<=3*p+2*/)
				count++;
		}

		
		for(int j=0;j<N&&S>0;j++)
		{
			if(t[j]<3*p-2&&t[j]>=3*p-4&&t[j]>=p)
			{
				count++;
				S--;
			}

		}
		cout<<count<<endl;
		getline(file,num,'\n');
		
	}
	getch();
}
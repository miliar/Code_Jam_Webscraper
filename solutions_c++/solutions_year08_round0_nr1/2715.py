#include<iostream>
#include<fstream>								
#include<string>
#include<math.h>

using namespace std;

void main()
{
	ifstream inputfile;
	ofstream outputfile;
	inputfile.open("A-small.in");
	outputfile.open("A-small.out");
	int Nos, n=1;
	inputfile >> Nos;
	while(Nos>0)
	{
		int no_engines,no_queries;
		string search_engines[10];
		string qurerys[100];
		char useless='0';
		string tem;
		inputfile>>no_engines;
		for (int numb=0; numb<no_engines; numb++)
		{
			inputfile>>search_engines[numb];
			inputfile.get(useless);
			for (;useless == ' ';)
			{
				inputfile>>tem;
				search_engines[numb] = search_engines[numb] + " " + tem;
				inputfile.get(useless);
			}
		}
		inputfile >> no_queries;
		for (numb=0; numb<no_queries; numb++)
		{
			inputfile >> qurerys[numb];
			inputfile.get(useless);
			for (;useless == ' ';)
			{
				inputfile >> tem;
				qurerys[numb] = qurerys[numb] + " " + tem;
				inputfile.get(useless);
			}
		}
		int swich=0;
		int plant = 100000000;
		for (int index=0; index<no_queries;)
		{
			int index_arr[10]={0};

			for (numb=index; numb<no_queries; numb++)
			{
				for (int numb1=0; numb1<no_engines; numb1++)
				{
					if (qurerys[numb] == search_engines[numb1])		
						index_arr[numb1]++;
				}
			}

			
			int min_no = 1000000;
			int min = 1000000;

			for (numb=0; numb<no_engines; numb++)
			{
				if (min > index_arr[numb] && plant != numb)
				{
					min = index_arr[numb];					
					min_no = numb;
				}
			}
			if (min == 0)
				break;
			for (numb=0; numb<no_engines; numb++)
			{
				if (min == index_arr[numb] && min_no!=numb && plant != numb)
				{
					for (int col1=index; col1<=no_queries; col1++)
						if (qurerys[col1] == search_engines[min_no])
							break;

					for (int col2=index; col2<=no_queries; col2++)
						if (qurerys[col2] == search_engines[numb])
							break;
						
					if (col2>col1)
						min_no = numb;
				}
			}
			int small=-2;
			for (numb=index; numb<=no_queries; numb++)
			{
				if (search_engines[min_no] == qurerys[numb])
				{
					small=numb;									
					break;
				}
			}
			for (int var=0; var<10; var++)
				index_arr[var]=0;

			for (numb=index; numb<=small; numb++)
			{
				for (int numb1=0; numb1<no_engines; numb1++)
				{
					if (qurerys[numb] == search_engines[numb1])			 
						index_arr[numb1]++;
				}
			}
			min = 100000;
			for (numb=0; numb<no_engines; numb++)
			{
				if (min > index_arr[numb] && plant != numb)
				{
					min = index_arr[numb];						
					min_no = numb;
				}
			}
			for (numb=0; numb<no_engines; numb++)
			{
				if (min == index_arr[numb] && min_no!=numb && plant != numb)
				{
					for (int col1=index; col1<=no_queries; col1++)
					{
						if (qurerys[col1] == search_engines[min_no])
							break;
					}

					for (int col2=index; col2<=no_queries; col2++)
					{
						if (qurerys[col2] == search_engines[numb])
							break;
					}
						
					if (col2>col1)
						min_no = numb;
				}
			}
			for (numb=index; numb<no_queries; numb++)
			{
				if (search_engines[min_no] == qurerys[numb])			
				{
					index = numb+1;
					break;
				}
			}
			swich++;
			plant = min_no;
		}
		outputfile<<"Case #"<<n<<": ";
		if(no_queries<=no_engines || swich == -1)
			outputfile << "0" <<endl;
		else 
			outputfile << swich <<endl;
		n++;
		Nos--;
	}
}
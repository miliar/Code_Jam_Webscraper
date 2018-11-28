#include<iostream>
#include<fstream>								
#include<string>
#include<math.h>

using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("A-small.in");
	outfile.open("A-small.out");
	int num, n=1;
	infile >> num;

	while(num>0)
	{
		outfile<<"Case #"<<n<<": ";
		int No_of_engines,No_of_queries;
		string engines[10];
		string queries[100];
		char no_use='0';
		string tem;

		infile>>No_of_engines;

		for (int count=0; count<No_of_engines; count++)
		{
			infile>>engines[count];
			infile.get(no_use);
			for (;no_use == ' ';)
			{
				infile>>tem;
				engines[count] = engines[count] + " " + tem;
				infile.get(no_use);
			}
		}

		infile >> No_of_queries;

		for (count=0; count<No_of_queries; count++)
		{
			infile >> queries[count];
			infile.get(no_use);
			for (;no_use == ' ';)
			{
				infile >> tem;
				queries[count] = queries[count] + " " + tem;
				infile.get(no_use);
			}
		}
		
		int change=0;
		int checkin = 100000000;
		for (int index=0; index<No_of_queries;)
		{
			int index_arr[10]={0};

			for (count=index; count<No_of_queries; count++)
			{
				for (int count1=0; count1<No_of_engines; count1++)
				{
					if (queries[count] == engines[count1])		
						index_arr[count1]++;
				}
			}

			
			int min_no = 1000000;
			int min = 1000000;

			for (count=0; count<No_of_engines; count++)
			{
				if (min > index_arr[count] && checkin != count)
				{
					min = index_arr[count];					
					min_no = count;
				}
			}

			if (min == 0)
				break;

			for (count=0; count<No_of_engines; count++)
			{
				if (min == index_arr[count] && min_no!=count && checkin != count)
				{
					for (int col1=index; col1<=No_of_queries; col1++)
						if (queries[col1] == engines[min_no])
							break;

					for (int col2=index; col2<=No_of_queries; col2++)
						if (queries[col2] == engines[count])
							break;
						
					if (col2>col1)
						min_no = count;
				}
			}
			int small=-2;
			for (count=index; count<=No_of_queries; count++)
			{
				if (engines[min_no] == queries[count])
				{
					small=count;									
					break;
				}
			}

			for (int var=0; var<10; var++)
				index_arr[var]=0;

			for (count=index; count<=small; count++)
			{
				for (int count1=0; count1<No_of_engines; count1++)
				{
					if (queries[count] == engines[count1])			 
						index_arr[count1]++;
				}
			}

			min = 100000;

			for (count=0; count<No_of_engines; count++)
			{
				if (min > index_arr[count] && checkin != count)
				{
					min = index_arr[count];						
					min_no = count;
				}
			}
			for (count=0; count<No_of_engines; count++)
			{
				if (min == index_arr[count] && min_no!=count && checkin != count)
				{
					for (int col1=index; col1<=No_of_queries; col1++)
					{
						if (queries[col1] == engines[min_no])
							break;
					}

					for (int col2=index; col2<=No_of_queries; col2++)
					{
						if (queries[col2] == engines[count])
							break;
					}
						
					if (col2>col1)
						min_no = count;
				}
			}
			for (count=index; count<No_of_queries; count++)
			{
				if (engines[min_no] == queries[count])			
				{
					index = count+1;
					break;
				}
			}
			change++;
			checkin = min_no;
		}

		if(No_of_queries<=No_of_engines || change == -1)
			outfile << "0" <<endl;
		else 
			outfile << change <<endl;
		n++;
		num--;
	}
	return 0;
}
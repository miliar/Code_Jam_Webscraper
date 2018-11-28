#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define MAX_TRIPS 20

struct trainInfo
{
	int departure;
	int arrival;
	bool isValid;
};

class TrainTimeTable
{
private:
	void sort(trainInfo list[], int size)
	{
		trainInfo buf;
		int j;

		for(int i = 1;i < size;++i)
		{
			buf = list[i];
			for(j = i;j > 0 && list[j - 1].arrival > buf.arrival;--j)
				list[j] = list[j - 1];

			list[j] = buf;
		}
	}
	void sort2(trainInfo list[], int size)
	{
		trainInfo buf;
		int j;

		for(int i = 1;i < size;++i)
		{
			buf = list[i];
			for(j = i;j > 0 && list[j - 1].departure > buf.departure;--j)
				list[j] = list[j - 1];

			list[j] = buf;
		}
	}
	int make_time_to_minutes(char* time)
	{
		int hour, minute;

		hour = atoi(time);
		minute = atoi(time + 3);

		return hour * 60 + minute;
	}
public:
	void make_result(char* input_file_name)
	{
		int number_of_case;
		int turnaround_time;
		int number_of_AtoB;
		int number_of_BtoA;
		bool checker = false;
		int trains_AtoB = 0;
		int trains_BtoA = 0;
		trainInfo* list_AtoB;
		trainInfo* list_BtoA;
		ifstream fin;
		ofstream fout;
		char buf[6];

		fin.open(input_file_name);
		if(fin.fail())
			exit(1);
		fout.open("output.txt");

		fin >> number_of_case;

		for(int i = 0;i < number_of_case;++i)
		{
			fin >> turnaround_time;
			fin >> number_of_AtoB;
			fin >> number_of_BtoA;
			list_AtoB = new trainInfo[number_of_AtoB];
			list_BtoA = new trainInfo[number_of_BtoA];

			for(int a = 0;a < number_of_AtoB;++a)
			{
				list_AtoB[a].isValid = true;
				fin >> buf;
				list_AtoB[a].departure = make_time_to_minutes(buf);
				fin >> buf;
				list_AtoB[a].arrival = make_time_to_minutes(buf) + turnaround_time;
			}
			for(int a = 0;a < number_of_BtoA;++a)
			{
				list_BtoA[a].isValid = true;
				fin >> buf;
				list_BtoA[a].departure = make_time_to_minutes(buf);
				fin >> buf;
				list_BtoA[a].arrival = make_time_to_minutes(buf) + turnaround_time;
			}

			sort(list_BtoA, number_of_BtoA);
			sort2(list_AtoB, number_of_AtoB);
			/*for(int a = 0;a < number_of_AtoB;++a)
			{
				cout << list_AtoB[a].departure << "  " << list_AtoB[a].arrival << endl;
			}
			cout << endl << endl;
			for(int a = 0;a < number_of_BtoA;++a)
			{
				cout << list_BtoA[a].departure << "  " << list_BtoA[a].arrival << endl;
			}*/
			if(number_of_AtoB > 0)
			{for(int a = 0;a < number_of_AtoB;++a)
			{
				for(int b = 0;b< number_of_BtoA;++b)
				{
					if(list_BtoA[b].isValid && list_AtoB[a].departure >= list_BtoA[b].arrival)
					{
						checker = true;
						list_BtoA[b].isValid = false;
						break;
					}
				}

				if(!checker)
				{
					trains_AtoB++;
				}
				else
					checker = false;
			}
			}
			checker = false;

			sort2(list_BtoA, number_of_BtoA);
			sort(list_AtoB, number_of_AtoB);
			if(number_of_BtoA > 0)
			{
			for(int a = 0;a < number_of_BtoA;++a)
			{
				for(int b = 0;b < number_of_AtoB;++b)
				{
					if(list_AtoB[b].isValid && list_BtoA[a].departure >= list_AtoB[b].arrival)
					{
						checker = true;
						list_AtoB[b].isValid = false;
						break;
					}
				}

				if(!checker)
				{
					trains_BtoA++;
				}
				else
					checker = false;
			}
			}
			fout << "Case #" << i + 1 << ": " << trains_AtoB << " " << trains_BtoA << endl;
			trains_AtoB = 0;
			trains_BtoA = 0;
			delete [] list_AtoB;
			delete [] list_BtoA;
		}
		fin.close();
		fout.close();
	}
};

void main()
{
	TrainTimeTable a;
	a.make_result("B-large.in");
	//a.make_result("input.txt");
}
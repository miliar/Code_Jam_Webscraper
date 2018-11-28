// Googlerese.cpp : Defines the entry point for the console application.
//

#include "DancingGooglers.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in_file;
	ofstream out_file;
	int num_cases = 0;
	RankFinder* rfinder = new RankFinder();

	in_file.open("B-large.in");
	if(!in_file.fail())
	{
		out_file.open("out.txt");
		if(!out_file.fail())
		{
			in_file >> num_cases;
			string in_string = "";
			getline(in_file,in_string);
			int i = 1;

			while(i <= num_cases)
			{
				in_file >> rfinder->num_goog;
				in_file >> rfinder->num_surprising;
				in_file >> rfinder->min_rank;

				int num_best_over_p = rfinder->find_num_p(&in_file);
				getline(in_file,in_string);

				out_file << "Case #" << i << ": " << num_best_over_p << "\n";
				in_string = "";
				i++;
			}
		}
		out_file.close();
	}
	in_file.close();
	cin >> num_cases;
	delete(rfinder);
	return 0;
}

int RankFinder :: find_num_p(ifstream* in_file)
{
	//int ratings[max_goog];
	cout << "\nnew group: " << min_rank << "\n";
	int rating = 0;
	int num_p = 0;
	for(int i = 0; i < num_goog; i++)
	{
		*in_file >> rating;
		cout << "checking rating: " << rating;
		if(rating >= min_rank)
		{
			if(is_normal(rating))
			{
				num_p++;
				cout << " = normal";
			}
			else if(num_surprising > 0 && is_surprising(rating))
			{
				num_p++;
				num_surprising--;
				cout << " = surprising";
			}
		}
		cout << "\n";
	}
	
	return num_p;
}

bool RankFinder :: is_normal(int rating)
{
	int abs_min = max((min_rank - 1),0);
	cout << "(" << min_rank << " " << (min_rank - 1) << " " << (min_rank - 1) << " (" << (min_rank + 2*(abs_min)) << "))";
	return rating >= (min_rank + (2*(abs_min)));
}

bool RankFinder :: is_surprising(int rating)
{ 
	int abs_min = max((min_rank - 2),0);
	cout << "(" << min_rank << " " << (min_rank - 2) << " " << (min_rank - 2) << " (" << (min_rank + 2*(abs_min)) << "))";
	return rating >= (min_rank + (2*(abs_min)));
}

RankFinder :: RankFinder()
{
}

RankFinder :: ~RankFinder()
{

}
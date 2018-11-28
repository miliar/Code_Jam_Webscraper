#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	
	unsigned T;
	input >> T;

	for(unsigned t=0; t<T; ++t)
	{
		unsigned N;
		input >> N;
		vector<string> liste;

		for(unsigned n=0; n<N; ++n)
		{
			string line_in;
			input >> line_in;
			liste.push_back(line_in);
		}
				
		vector<double> WP;
		vector<double> OWP;
		vector<double> OOWP;

		for(unsigned i=0; i<N; ++i)
		{
			double zero_count = 0, one_count = 0;

			unsigned size = liste[1].size();
			string current_line = liste[i];

			for (unsigned l=0; l<size; ++l)
			{
				if(current_line[l] == '1')
					one_count++;
				else if (current_line[l] == '0')
					zero_count++;
			}

			WP.push_back(one_count/(one_count+zero_count));
		}

		for(unsigned i=0; i<N; ++i)
		{
			double accum = 0;
			double played = 0;

			string check_list = liste[i];

			for(unsigned j=0; j<N; ++j)
			{
				if(i==j)
					continue;

				if(check_list[j] == '.')
					continue;

				played++;
				
				double zero_count = 0, one_count = 0;

				unsigned size = liste[1].size();
				string current_line = liste[j];

				for (unsigned l=0; l<size; ++l)
				{
					if(i==l)
						continue;

					if(current_line[l] == '1')
						one_count++;
					else if (current_line[l] == '0')
						zero_count++;
				}

				accum += one_count/(one_count+zero_count);
			}

			OWP.push_back(accum/played);
		}

		for(unsigned i=0; i<N; ++i)
		{
			double accum = 0;
			double played = 0;

			string check_list = liste[i];

			for(unsigned j=0; j<N; ++j)
			{
				if(i==j)
					continue;

				if(check_list[j] == '.')
					continue;

				played++;

				accum += OWP[j];
			}

			OOWP.push_back(accum/played);
		}


		output << "Case #" << t+1 << ": " << endl;

		for(unsigned i=0; i<N; ++i)
		{
			output << 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i] << endl;
		}

	}
	
	input.close();
	output.close();
	return 0;
}
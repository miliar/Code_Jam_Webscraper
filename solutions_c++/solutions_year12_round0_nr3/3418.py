#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

std::string convertInt(int number)
{
   std::stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main(int argc, char** argv)
{
	std::string line;
	std::ifstream inputFile ("C-small-attempt0.in");
	std::ofstream outputFile ("output.txt");
	int A = 0;
	int B = 0;
	int n = 0,m = 0;
	std::string temp_string = "";
	int answer_row = 0;
	int flag = 0;

	int no_of_cases = 0;
	if (inputFile.is_open())
	{
		// this line gives us the number of test cases
		getline (inputFile,line);
		no_of_cases = atoi(line.c_str());
		std::string strSeq = "";
		for (int counter = 1; counter <= no_of_cases; counter++)
		{
			// read line by line
			getline (inputFile,line);
			std::istringstream iss(line);
			
			// get A
			iss >> temp_string;
			A = atoi(temp_string.c_str());

			// get B
			iss >> temp_string;
			B = atoi(temp_string.c_str());
			answer_row = 0;

			std::vector<int> cyclic;

			for (int i = A; i <= B;i++)
			{
				strSeq = convertInt(i);
				n = i;
				cyclic.clear();
				for (int j = 1;j<strSeq.length();j++)
				{
					// handle single character
					strSeq = strSeq.substr(1, strSeq.length()-1)  + strSeq [0];
					m = atoi(strSeq.c_str());
					
					if (A <= n && n < m && m <= B)
					{
						flag = 0;
						for (int l = 0;l<cyclic.size();l++)
						{
							if (cyclic[l]==m)
							{
								flag = 1;
								break;
							}
						}
						if (flag == 0)
						{
							//std::cout<<A<<"  "<<n<<"  "<<m<<"  "<<B<<std::endl;
							answer_row++;
							cyclic.push_back(m);
						}
					}
				}
			}
			outputFile <<"Case #"<<counter<<": "<<answer_row<<std::endl;
		}
		inputFile.close();
		outputFile.close();
	}
	else 
		std::cout << "Unable to open file"; 
	return 0;
}
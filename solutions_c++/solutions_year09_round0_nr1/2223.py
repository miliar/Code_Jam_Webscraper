#include<iostream>
#include<fstream>
#include<string>

int main()
{
	int length = 0;
	int words = 0;
	int test = 0;
	std::ifstream ifs( "test.txt" );
	std::ofstream ofs( "output.txt" );

	ifs >> length >> words >> test;
	std::string* strWord = new std::string[words]; 
	std::string* strTest = new std::string[test]; 

	for(int i = 0; i < words; ++i)
	{
		ifs >> strWord[i];
	}
	for(int i = 0; i < test; ++i)
	{
		ifs >> strTest[i];
	}
	std::cout << strWord[0].length() <<std::endl;

	for(int i = 0; i < test; ++i)
	{
		int count = 0;

		for(int j = 0; j < words; ++j)
		{
			int indexWord = 0;
			int indexTest = 0;

			while(indexWord < length)
			{
				if(strTest[i].at(indexTest) == strWord[j].at(indexWord))
				{
					indexTest++;
					indexWord++;
					continue;
				}
				else if(strTest[i].at(indexTest) == '(')
				{
					indexTest++;

					while(1)
					{
						if(strTest[i].at(indexTest) == ')')
						{
							break;
						}
						else if(strTest[i].at(indexTest) == strWord[j].at(indexWord))
						{
							indexWord++;
							do
							{
								indexTest++;
							}while(strTest[i].at(indexTest) != ')');
							indexTest++;

							break;
						}
						else
						{
							indexTest++;
						}
					}
				}
				else
				{
					break;
				}
			}
			if((strTest[i].length() == indexTest) && (strWord[j].length() == indexWord))
			{
				count++;
			}
		}

		ofs << "Case #" << i + 1 << ": " << count << std::endl;
	}

	delete[] strWord;
	delete[] strTest;

	return 0;
}
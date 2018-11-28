#include <iostream>
#include <fstream>
#include <string>

char alphabet[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(int argc, char *argv[])
{
  if (argc==2)
  {
    std::ifstream input_file(argv[1]);
    std::ofstream output_file;
    std::string line;
    output_file.open("output.out");
    if (input_file.is_open())
    {
      int caseCount; //number of inputs
      input_file>>caseCount; //Number of 
      char x;
      getline(input_file, line);
      for (int i=0;i<caseCount;i++)
      {
	getline(input_file, line);
	std::cout<<"X: "<<line<<std::endl;
	//std::cout<<"L: "<<line.length()<<std::endl;
	for(int j=0;j<line.length();j++)
	{
	  if((char)line[j]>96)
	  {
	    line[j]=alphabet[(char)line[j]-97];//97+(((char)line[j]-97)+number)%(122-97);
	  }
	}
	output_file<<"Case #"<<i+1<<": "<<line<<std::endl;
      }
    }
    output_file.close();
    return 0;
  }
}
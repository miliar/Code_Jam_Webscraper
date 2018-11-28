#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

#define IO_ERROR_CODE 10
#define SUCCESS_EXIT 0

//#define _DEBUG

//using namespace std;

unsigned int ScenariosNum;

unsigned int string2int(std::string s)
{      
      std::stringstream w;
      unsigned int i;
      w << s;
      w >> i;
      return i;
}

unsigned int ReadNumData(std::ifstream& DataFile)
{
  std::string TextLine;
  getline(DataFile,TextLine);
  return string2int(TextLine);
}

unsigned int ParseScenarioFile(std::ifstream& DataFile)
{
     std::string Query("");
     std::map<std::string, unsigned int> SearchEngines;
     unsigned int SearchEnginesNum;
     unsigned int TotalQueriesNum;
          
     SearchEnginesNum = ReadNumData(DataFile);

#ifdef _DEBUG         
         std::cout << "Total number of search engines: " << SearchEnginesNum << std::endl;
         std::cout << "---------------------------------------------------" << std::endl;
#endif               
         for (int j=0; j<SearchEnginesNum; j++)
         {
             std::string SearchEngineName;
             getline(DataFile,SearchEngineName);
#ifdef _DEBUG         
             std::cout << "The " << j << " search engine name is:" << SearchEngineName << "." << std::endl;
#endif
             SearchEngines[SearchEngineName]=0;
         }

         TotalQueriesNum = ReadNumData(DataFile);

#ifdef _DEBUG                  
         std::cout << "Total number of search queries: " << TotalQueriesNum << std::endl;
         std::cout << "---------------------------------------------------" << std::endl;
#endif
                  
         unsigned int Switchovers=0;
         unsigned int Marker=1;
         unsigned int Tracker=0;

         for (int j=0; j<TotalQueriesNum; j++)
         {             
             getline(DataFile,Query);

#ifdef _DEBUG                      
             std::cout << "The " << j << " search query is:" << Query << "." << std::endl;
             std::cout << "Marker is " << SearchEngines[Query] << std::endl;
#endif 

             if (SearchEngines[Query] < Marker) { 
                                                   if (Tracker + 1 == SearchEnginesNum) {
                                                                                          Tracker=0;
                                                                                          Switchovers++; Marker++;
                                                                                         }
                                                    SearchEngines[Query] = Marker; 
                                                    Tracker++; 
                                                   }
         }

#ifdef _DEBUG
         std::cout << "====================================================" << std::endl;
         std::cout << "The solution should be " << Switchovers << std::endl;
         std::cout << "====================================================" << std::endl;         
#endif
         return Switchovers;

}


int main(void)
{
    std::ifstream InputFile;
    std::ofstream OutputFile;
    InputFile.open("data.txt");
    OutputFile.open("results.txt");
    if (!InputFile.good()) return IO_ERROR_CODE;
    if (!OutputFile.good()) return IO_ERROR_CODE;    

    ScenariosNum = ReadNumData(InputFile);

#ifdef _DEBUG    
     std::cout << "Total scenarios: " << ScenariosNum << std::endl;
     std::cout << "---------------------------------------------------" << std::endl;
#endif
     for (int i=0; i<ScenariosNum; i++)
     {
       unsigned int ScenarioSolution = ParseScenarioFile(InputFile);
       OutputFile << "Case #" << i+1 << ": " << ScenarioSolution << std::endl;
//       system("pause");
     }
     return SUCCESS_EXIT;
}

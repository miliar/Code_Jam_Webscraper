#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>

#define IO_ERROR_CODE 10
#define SUCCESS_EXIT 0

//#define _DEBUG

//using namespace std;

//--------------------------------------------------------------------------
struct Train
{
  std::list<unsigned int> Departure;
  std::list<unsigned int> Arrival;
  unsigned int TrainNumber;
  unsigned int TimetableEntries;
  unsigned int Turnaround;
};
//--------------------------------------------------------------------------
unsigned int string2int(std::string s)
{      
      std::stringstream w;
      unsigned int i;
      w << s;
      w >> i;
      return i;
}
//--------------------------------------------------------------------------
void NextLine(std::ifstream& DataFile)
{
  std::string TextLine;
  getline(DataFile,TextLine);
}
//--------------------------------------------------------------------------
unsigned int Convert2Min(std::string HH_MM) // converts HH:MM format into minutes
{
  unsigned int min = string2int(HH_MM.substr(0,2)) * 60; // get the HH from the time
  min += string2int(HH_MM.substr(3,2));                  // get the minutes
  return min;
}
//--------------------------------------------------------------------------
void GetTrainSchedule(std::ifstream& DataFile, Train& T)
{     
   for (int i=0;i < T.TimetableEntries; i++)
     {
         std::string Depart, Arrive;
         DataFile >> Depart >> Arrive;
         T.Arrival.push_back(Convert2Min(Arrive));
         T.Departure.push_back(Convert2Min(Depart));
         NextLine(DataFile);
         
#ifdef _DEBUG
       std::cout << "Departure: " << Depart << ", arrival: " << Arrive << std::endl;
#endif                  
     }
  T.Arrival.sort();
  T.Departure.sort();

}
//--------------------------------------------------------------------------
void LoadTimetable (std::ifstream& DataFile, Train& A, Train& B)
{
     DataFile >> A.Turnaround;
     B.Turnaround = A.Turnaround;
     
     NextLine(DataFile);
     
     DataFile >> A.TimetableEntries >> B.TimetableEntries;
     NextLine(DataFile);
     
     GetTrainSchedule(DataFile, A);
     GetTrainSchedule(DataFile, B);

#ifdef _DEBUG
       std::cout << "Train turnaround time: " << A.Turnaround << std::endl;
       std::cout << "Total Entries for AB train: " << A.TimetableEntries << std::endl;
       std::cout << "Total Entries for BA train: " << B.TimetableEntries << std::endl;
       std::cout << "====================================================" << std::endl;
#endif     
     
 }
//-------------------------------------------------------------------------- 
void ProcessTimetable(Train& A, Train& B)
{
   std::list<unsigned int>::iterator it1;
   std::list<unsigned int>::iterator it2;   

   for (it1=A.Arrival.begin(); it1!=A.Arrival.end(); ++it1)
   {
       for (it2=B.Departure.begin(); it2!=B.Departure.end(); ++it2)
       {
           if (*it1 + A.Turnaround <= *it2) {
                                             it2 = B.Departure.erase(it2);
                                             break;
                                            }
       }
       
   }
     
 }
//--------------------------------------------------------------------------
void PrintResults(std::ofstream& OutFile, Train A, Train B, int ScenarioID)
{

     OutFile << "Case #" << ScenarioID << ": " << (int)A.Departure.size() << " " << (int)B.Departure.size() << std::endl;

#ifdef _DEBUG         
     std::cout << "========================================================" << std::endl;
     std::cout << "Required trains in A:" << (int)A.Departure.size() << std::endl;
     std::cout << "Required trains in B:" << (int)B.Departure.size() << std::endl;
     std::cout << "========================================================" << std::endl;     
#endif

 }
 
//--------------------------------------------------------------------------
//--------------------------------------------------------------------------
//--------------------------------------------------------------------------
int main(void)
{
    unsigned int ScenariosNum;              // Number of scenarios
    
   
    std::ifstream InputFile;
    std::ofstream OutputFile;
    
    InputFile.open("data.txt");
    OutputFile.open("results.txt");
    if (!InputFile.good()) return IO_ERROR_CODE;
    if (!OutputFile.good()) return IO_ERROR_CODE;
    
    InputFile >> ScenariosNum;
    NextLine(InputFile);

#ifdef _DEBUG    
     std::cout << "Total scenarios: " << ScenariosNum << std::endl;
     std::cout << "---------------------------------------------------" << std::endl;
#endif
    
    for (int CaseID=1; CaseID<=ScenariosNum; CaseID++)
    {
      Train AB,BA;  
      LoadTimetable(InputFile,AB,BA);
      ProcessTimetable(AB,BA);
      ProcessTimetable(BA,AB);      
      PrintResults(OutputFile,AB,BA,CaseID);

#ifdef _DEBUG          
     std::cout << "---------------------------------------------------" << std::endl;      
#endif     
    }

    OutputFile.close();

#ifdef _DEBUG        
    system("pause");
#endif

    return SUCCESS_EXIT;    
}

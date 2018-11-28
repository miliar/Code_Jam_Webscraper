#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;
#define DEBUG 0

int main(){

      int number_of_test = 0;  
      int number_of_combine_rules = 0;
      int number_of_oppose_rules = 0;                       
      int seq_length = 0;

      ifstream inputFile;
      inputFile.open("B-large.in");
      
      if (!inputFile)
      {
            cout << "input file error, check file name and path!" <<endl;
      }
      
      inputFile >> number_of_test;
   //   cout << "total number of test cases is:  " << number_of_test <<endl;
   //   cin.get();
      
      ofstream outputFile;
      outputFile.open("Magicka_output.txt");

      for (int tc = 1; tc <= number_of_test; tc++)
      {
         //   cout << "currently process test case number: " << tc <<endl;
         //   cin.get();

            map<pair<char, char>, char> combineRule;
            pair<char, char> chpair;
            pair<char, char>rchpair;
            map<pair<char, char>, int> opposeRule;
            
            char first = '#';
            char second = '#';
            char third = '#';

            vector<char> result; //stores the final result
            result.push_back(' ');

            inputFile >>number_of_combine_rules;
        //    cout << "number of combine rules" <<number_of_combine_rules << endl;

            //read c number of strings, combine rules
            for (int j = 0; j < number_of_combine_rules; j++)
            {
                  inputFile>>first >> second >> third;
                  chpair = std::pair<char, char>(first, second);
                  combineRule[chpair] = third;
            }

            inputFile >>number_of_oppose_rules; 
        //    cout << "number of oppose rules" <<number_of_oppose_rules <<endl;

            //read d number of strings, oppose rules
            for (int k = 0; k < number_of_oppose_rules; k++)
            {
                  inputFile>>first >> second;
                  chpair = std::pair<char, char>(first,second);
                  opposeRule[chpair] = k+1;
            }


#ifndef DEBUG
            //print out combination rule and oppose rule for debug
            map<pair<char, char>, char>::iterator combineIt;
            map<pair<char, char>,int>::iterator opposeIt;
            for (combineIt=combineRule.begin(); 
                   combineIt != combineRule.end(); ++combineIt)
            {
                  cout << combineIt->first.first << combineIt->first.second << combineIt->second <<endl;
            }

            for (opposeIt =opposeRule.begin(); 
                   opposeIt != opposeRule.end(); ++opposeIt)
            {
                  cout << opposeIt->first.first << opposeIt->first.second << opposeIt->second <<endl;
            }

            cin.get();
#endif

            inputFile >>seq_length;
         //   cout << "to process string length" <<seq_length <<endl;
            char str = '#';
            
            for (int k = 0; k <seq_length; k++)
            {
                  inputFile >>str ; 
                 
                  //decide based on combine rules and oppose rule, update the result stack
                  chpair = std::pair<char, char>(str, result[result.size()-1]);
                  rchpair = std::pair<char, char>(result[result.size()-1], str);
                  bool flag = false;

                  if( !(combineRule.find(chpair ) == combineRule.end())) 
                  {
                        result[result.size() -1] = combineRule[chpair];
                        flag=true;
                  }
                  else if ( !(combineRule.find(rchpair ) == combineRule.end()))
                  {
                        result[result.size()-1] = combineRule[rchpair];
                        flag=true;
                  }
                  else {
                        for(int i=0;i<result.size();i++)
                        {
                              chpair=std::pair<char, char>(str, result[i]);
                              rchpair = std::pair<char, char>(result[i], str);
                              if( !(opposeRule.find(chpair ) == opposeRule.end())) 
                              {
                                    result.clear();
                                    result.push_back(' ');
                                    flag=true;
                                    break;
                              }
                              else if ( !(opposeRule.find(rchpair ) == opposeRule.end()))
                              {
                                    result.clear();
                                    result.push_back(' ');
                                    flag=true;
                                    break;
                              }
                        }
                  }
                  
                  if(!flag)
                  {
                        result.push_back(str);
                  }
            }//EndForCurSeq
            
            //start process the string with length N
            outputFile <<"Case #"<< tc<<": ";
            outputFile<< "[" ;
            for (int k = 1; k < result.size()-1; k++ )  //first one is space, do not print to output file
            {
                 outputFile <<result.at(k)<<", ";
            }
            if (result.size() >1)
            {
                  outputFile<<result.at(result.size()-1) ;
            }
            outputFile <<"]"<<endl;


      }//EndForAllTestCases
      outputFile.flush();
      outputFile.close();
     // cin.get(); 
      return 0;
}
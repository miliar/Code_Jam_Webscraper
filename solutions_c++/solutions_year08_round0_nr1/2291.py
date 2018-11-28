#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char* argv[]){
  size_t caseAmount;
  vector<vector<string> > searchEngines;
  vector<vector<string> > queries;
  if(argc != 3){
    cout << "Requires input and output file parameters, and that alone\n";
  }
  ifstream inputFile(argv[1], ifstream::in);
  if(inputFile.is_open()){
    size_t i, j, k;
    
    string caseAmtStr;
    getline (inputFile,caseAmtStr);
    istringstream caseAmtStream(caseAmtStr);
    if(!(caseAmtStream >> caseAmount))
    {
      cout << "Problem with input\n";
      return -1;
    }
    for(j = 0; j < caseAmount; j++){
      size_t seAmount;
      vector<string> se;
      string seAmtStr;
      if(inputFile.eof()){
        cout << "Sudden end of file here!\n";
        return -1;
      }
      getline(inputFile, seAmtStr);
      istringstream seAmtStream(seAmtStr);
      if(!(seAmtStream >> seAmount))
      {
        cout << "Problem with input\n";
        return -1;
      }
      for(i = 0; i < seAmount; i++)
      {
        string tempSE;
        if(inputFile.eof())
        {
          cout << "Sudden end of file here!\n";
          return -1;
        }
        getline(inputFile, tempSE);
        se.push_back(tempSE);
      }
      searchEngines.push_back(se);
      
      size_t queryAmount;
      vector<string> query;
      string queryAmtStr;
      if(inputFile.eof()){
        cout << "Sudden end of file here!\n";
        return -1;
      }
      getline(inputFile, queryAmtStr);
      istringstream queryAmtStream(queryAmtStr);
      if(!(queryAmtStream >> queryAmount))
      {
        cout << "Problem with input\n";
        return -1;
      }
      for(i = 0; i < queryAmount; i++)
      {
        string tempQuery;
        if(inputFile.eof())
        {
          cout << "Sudden end of file here!\n";
          return -1;
        }
        getline(inputFile, tempQuery);
        query.push_back(tempQuery);
      }
      queries.push_back(query);
    }
    inputFile.close();
    
    vector<int> switches;
    for(i = 0; i < searchEngines.size(); i++){
      vector<string> seList = searchEngines.at(i);
      vector<string> queryList = queries.at(i);
      vector<int> occurences;
      size_t count = 0;
      int switchesMade = 0;
      vector<size_t> firstFound;
      for(j = 0; j < seList.size(); j++){
        firstFound.push_back(queries.at(i).size() + 1);
      }
      while(count != queries.at(i).size()){
        bool allFound = true;
        for(j = 0; j < seList.size(); j++){
          if(queries.at(i).at(count) == seList.at(j) && firstFound.at(j) == queries.at(i).size() + 1){
            firstFound.at(j) = count;
          }
        }
        for(j = 0; j < firstFound.size(); j++){
          if(allFound && firstFound.at(j) == queries.at(i).size() + 1){
            allFound = false;
          }
        }
        if(allFound){
          switchesMade++;
          for(j = 0; j < firstFound.size(); j++){
            if(firstFound.at(j) != count){
              firstFound.at(j) = queries.at(i).size() + 1;
            }
          }
        }
        count++;
      }
      switches.push_back(switchesMade);
    }
    ofstream outputFile(argv[2]);
    for(i = 0; i < switches.size(); i++){
      outputFile << "Case #" << i + 1 << ": " << switches.at(i) << "\n";
    }
    outputFile.close();
  }else{
    cout << "Couldn't open input file\n";
  }
}

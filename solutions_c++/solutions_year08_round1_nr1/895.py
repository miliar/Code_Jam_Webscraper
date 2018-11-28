#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

main(){
 
  char buf[256];
  ifstream inputFile("input.txt");
  ofstream outFile("output.txt");
  if(!inputFile.is_open()){
    cout<<"Error opening file\n"; exit(1);
  }

  if(!outFile.is_open()){
    cout<<"Error opening file\n"; exit(1);
  }

  if(!inputFile.eof())
    inputFile.getline(buf,256);
  int num = atoi(buf);
  cout<<num<<endl;
  for(int i=1; i <= num; i++){
    inputFile.getline(buf,256);
    int xnum = atoi(buf); 
    char buf1[10000];
    inputFile.getline(buf1,10000);
    vector<int> v1;
    cout<<buf1<<endl;
    char *pch = strtok(buf1," ");
    for(int j=0; j< xnum;j++){
       v1.push_back(atoi(pch));   
       cout<<atoi(pch)<<endl;
       pch = strtok(NULL," "); 
    }
 
    inputFile.getline(buf1,10000);
    vector<int> v2;
    cout<<buf1<<endl;
    pch = strtok(buf1," ");
    for(int j=0; j< xnum;j++){
       v2.push_back(atoi(pch));   
       cout<<atoi(pch)<<endl;
       pch = strtok(NULL," "); 
    }
    sort(v1.begin(),v1.end());
    sort(v2.begin(),v2.end());
    reverse(v2.begin(),v2.end());
    int sum = 0;
    for(int k=0; k< xnum; k++){
      sum = sum + v1[k] * v2[k]; 
    }   
    outFile<<"Case #"<<i<<": "<<sum<<endl;
  }
   
}

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int getSecs(char *t){
  char *pch = strtok(t,":");
  int hr = atoi(pch);
  pch = strtok(pch,":");
  int min = atoi(pch);
  return (60 * hr + min); 
}

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
    cout<<buf<<endl;
    int turnTime = atoi(buf);
    inputFile.getline(buf,256);
    cout<<buf<<endl;
    char *pch = strtok(buf," ");
    int A2B = atoi(pch);
    pch=strtok(NULL, " ");
    int B2A = atoi(pch);
    vector<int> depA2B; 
    vector<int> arrA2B;
    vector<int> depB2A;
    vector<int> arrB2A;

    for(int j=0; j < A2B; j++){
      
       int hr1=0,min1=0,hr2=0,min2=0;
       inputFile.getline(buf,256);
       sscanf(buf,"%d:%d %d:%d",&hr1,&min1,&hr2,&min2);
       depA2B.push_back(hr1*60+min1);
       arrA2B.push_back(hr2*60+min2); 
    }
    
    for(int j=0; j < B2A; j++){
       int hr1=0,min1=0,hr2=0,min2=0;
       inputFile.getline(buf,256);
       sscanf(buf,"%d:%d %d:%d",&hr1,&min1,&hr2,&min2);
       depB2A.push_back(hr1*60+min1);
       arrB2A.push_back(hr2*60+min2); 
    }
    cout<<"sorting stuff"<<endl;
    sort(depA2B.begin(), depA2B.end());
    sort(arrA2B.begin(),arrA2B.end());
    sort(depB2A.begin(), depB2A.end());
    sort(arrB2A.begin(),arrB2A.end());
    int numA2B = 0, numB2A=0, k = 0; 
    for(int j=0; j < A2B; j++){
      if(k < arrB2A.size()){
         cout<<"arr time is "<<arrB2A[k]<<" " <<depA2B[j]<<endl;
         if ((arrB2A[k]+turnTime) <=depA2B[j]){
            k++; continue;
         }
      }
      numA2B++; 
    } 
    k=0; 
    for(int j=0; j < B2A; j++){
      if(k < arrA2B.size()){
         if ((arrA2B[k]+turnTime) <=depB2A[j]){
            k++; continue;
         }
      }
      numB2A++; 
    }

     
    outFile<<"Case #"<<i<<": "<<numA2B<<" "<<numB2A<<endl;
  }
   
}

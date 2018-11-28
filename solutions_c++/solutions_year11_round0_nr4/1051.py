//Gorosort
//expected is number incorrect
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


int main(){
    
int cases,num;
ifstream inf;
ofstream fout;
char fileName[100];
char fileOut[100];
vector<int> list;
int a, slot;
int swaps=0;
int temp,n;

//input data
inf.clear();
cout<<"enter file name: ";
cin>>fileName;
cout<<"enter out name: ";
cin>>fileOut;

inf.open(fileName);
if(!inf.good()){
   cout<<"ERROR";
   system("pause");
   }
   
fout.clear();
fout.open(fileOut);
                
inf>>cases;

for( int i=0;i<cases;i++){

     inf>>num;
     list.clear();
     
     for(int j=0;j<num;j++){
             inf>>a;
             list.push_back(a);
             }
     
     n=num;
     for(int j=0;j<num;j++){
             if(list[j]==j+1)
                n--;
                     }

     
     
     //output
     fout<<"Case #"<<i+1<<": ";
     fout<<n<<endl;
     
   }
      
 return 0;   
}


#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;



string dec2bin(unsigned n)
{
    const size_t size = sizeof(n) * 8;
    char result[size];

    unsigned index = size;
    do {
        result[--index] = '0' + (n & 1);
    } while (n >>= 1);

    return string(result + index, result + size);
}


string badAdd(string& a, string& b){
       string result;
       int sizeS, sizeL;
       
       string* sm;
       string* la;
       
       if(a.size()>b.size()){
          sizeL=a.size();
          sizeS=b.size();
          la=&a;
          sm=&b;
          }
       else{
          sizeL=b.size();
          sizeS=a.size();
          la=&b;
          sm=&a;
          }
       
       result.resize(sizeL);
       
       for(int i=0;i<sizeS;i++){
               if( (*la)[sizeL-i-1]!=(*sm)[sizeS-i-1] )
                   result[sizeL-i-1]='1';
               else
                   result[sizeL-i-1]='0';
               
               }

        for(int i=sizeS;i<sizeL;i++){
               result[sizeL-i-1]= (*la)[sizeL-i-1];
               }       

        return result;

       }
       





int main(){
    
int cases,num, small, sum, a;
ifstream inf;
ofstream fout;
string badSum, b;
char fileName[100];
char fileOut[100];

bool work=false;

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
     //improper add all, if 0's subtract smallest
     inf>>num;
     
     small=2000000000;
     badSum.clear();
     sum=0;
     if(num>0)
       {
        inf>>a;
        badSum.assign( dec2bin(a) );
        sum+=a;
        if(a<small)
           small=a;
       }
     
     for(int j=1;j<num;j++){
             inf>>a;
             b.assign( dec2bin(a) );
             
             badSum.assign(badAdd(badSum,b));

             sum+=a;
             
             if(a<small)
                small=a;

             
             }
     
     work=true;
     for(int j=0;j<badSum.size();j++){
             if(badSum[j]!='0')
                work=false;
             
             }
     if(num<2)
        work=false;
     
     if(work){
              //output
              fout<<"Case #"<<i+1<<": ";
              fout<<sum-small<<endl;

              }
     else{
              //output
              fout<<"Case #"<<i+1<<": ";
              fout<<"NO"<<endl;

              } 
     
     
   }
      
 return 0;   
}




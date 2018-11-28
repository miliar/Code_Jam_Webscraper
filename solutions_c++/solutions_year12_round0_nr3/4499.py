#include <stdio.h>
#include <stdint.h>
#include <map>
#include <fstream>
#include <cstdlib>

using namespace std;
using std::ifstream;

int getbase(int digit){
  if(digit==1) return 1;
  else if(digit==2) return 10;
  else if(digit==3) return 100;
  else if(digit==4) return 1000;
  else if(digit==5) return 10000;
  else if(digit==6) return 100000;
  else return 0;
}


int shift(int num, int digit, int nofromleft){
  int res=num%(getbase(nofromleft+1));
  res=res*getbase(digit-nofromleft+1);
  res=(num/(getbase(nofromleft+1)))+res;
  return res;
}


int find_no_of_digits(int A){
int digits=1;
int temp=A;

while(temp!=0){
 temp=temp/10;
 digits++;
}

return digits-1;
}



int main(){

multimap<int, int> recycle_pair;
multimap<int, int>::iterator it;
int A=0, B=0;
int digit=0, idigit=0, i=0, count=0, temp=0;

ifstream indata; 

indata.open("input.txt"); // opens the file
if(!indata) { 
  printf("\nCould not open file input.txt");
  exit(1);
}

/* read first line..i.e No of iterations */
int Noiterations=0;
indata >>Noiterations;
int tNoiterations=Noiterations;

while(Noiterations > 0){

/* read and parse file for inputs A and B */
indata >> A;
indata >> B;

/* if n digits then be ready for n-1 something. */
digit= find_no_of_digits(A);
idigit=0;

i=0;
count=0;

for(i=A; i<B; i++)
{
   temp=0; 
   for(idigit=1;idigit<=digit;idigit++){
 
       temp=shift(i,digit,idigit);
       if((temp>i) && (temp!=i) && (temp<=B) && (temp>=A))
        { 
           //printf("\n num is %d ",i);
           it=recycle_pair.find(temp); 
           if(it->second != i) recycle_pair.insert(std::pair<int,int>(temp,i)); 
        }

    }

}

//printf("\n count is %d \n",(int)recycle_pair.size());
printf("\n Case #%d: %d",tNoiterations-Noiterations+1, (int)recycle_pair.size());

/* Clear stl maps */
recycle_pair.clear();

Noiterations--;
}

printf("\n");
return 0;
}




#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main() {



    string filename= "candy.txt";
     ifstream fin(filename.c_str());
     ofstream fout("candyout.txt");
     
vector <int> A(0);

int buffer;
int testcase=0;
int n=0;
fin>>testcase;



vector <int> number(0);
vector <int> binary(0);

for(int j=0; j<testcase;j++) {

fin>>n;
number.clear();

for(int i=0;i<n;i++) 
{
        fin>>buffer;
        number.push_back(buffer);
        
        }
int buff=0; int sum=0;
int min=number[0];
int aa=0;

for(int i=0;i<number.size();i++) 
{       aa=number[i];
        if(aa<min) 
        min=aa;

        buff=buff^number[i];
     
        sum+=number[i];
}


sum=sum-min;
if(buff==0) 

fout<<"Case #"<<j+1<<": "<<sum<<endl;

else
fout<<"Case #"<<j+1<<": NO"<<endl;


}




}




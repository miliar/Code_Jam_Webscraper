#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main() {



    string filename= "magic.txt";
     ifstream fin(filename.c_str());
     ofstream fout("magicout.txt");
     
vector <char> magic(0);
vector <char> list(0);
int testcase=0;
fin>>testcase;

for(int l=0;l<testcase;l++) 
{
       

list.clear();
magic.clear();
int number=0;
int combine=0;
int gone=0;
char a=' ';
char b=' ';
char c=' ';
char d=' ';
char e=' ';
fin>>combine;
if(combine!=0)
{
fin>>a;
fin>>b;
fin>>c;
}
fin>>gone;
if(gone!=0)
{
fin>>d;
fin>>e;
}

fin>>number;

char buff;
for(int i=0;i<number;i++) 
{
        
fin>>buff;
magic.push_back(buff);
}

int counter=0;
for(int i=0;i<number;i++) 
{


if(i==0)
{
list.push_back(magic[i]);
continue;
}




if( (magic[i]==a && list.back()==b )||(magic[i]==b && list.back()==a) && list.size()!=0 ) 
{
   
list.back()=c;
continue;
}
int k1=0;
int k2=0;
       
 
 
     
if( magic[i]==d)
{
  
 
for(int j=0;j<list.size();j++) 
{
     

if(list[j]==e)
{
                            

list.clear();
counter=-1;
k1=1;
}
}
if(k1==0)
{         
list.push_back(magic[i]);
}

continue;
}



if( magic[i]==e)
{
   

for(int j=0;j<list.size();j++) 
{
        

 
if(list[j]==d)
{
list.clear();

k2=1;
}
}
if(k2==0)
{
list.push_back(magic[i]);

}
continue;
}

list.push_back(magic[i]);


 
}



fout<<"Case #"<<l+1<<": [";
for(int i=0;i<list.size();i++) 
{
if(i!=list.size()-1)
fout<<list[i]<<", ";
}
if(list.size()!=0) 
fout<<list[list.size()-1]<<"]"<<endl;
else
fout<<"]"<<endl;

}


// system("PAUSE");

}







#include <string>

#include <fstream>

#include<stdio.h>

#include <math.h>


#include <algorithm>

#include <set>

#include <dos.h>

#include <sstream>


#include<iostream>



#include <vector>

#include <cstdio>

using namespace std;

 int main()
   {
     long long a;
     long long q=0,noushy=0;
     long long n=0;
     lonb long s=0;
     long long b,c;
   

   string str="",buf;




   //stringstream ss(str);
   //calucating 

     for(int jadu=0;jadu<45;jadu++)  // for loop
    {
     jadu++;
}   









vector <long long> tokens;

    ifstream file("C:\\a.in");
    getline( file, str );
    n=atoi(str.c_str());

        for (int i=0;i<n;i++){
   noushy=0;
   getline( file, str );
istringstream ss(str);
ss>>a>>b>>c;


//code gener......




for(int jadhu=0;jadhu<45;jadhu++)  // for loop
    {
     jadhu++;
}   


   getline( file, str );
   stringstream ss1(str);

  while (ss1 >> buf)
    tokens.push_back(atoi(buf.c_str()));

sort(tokens.rbegin(),tokens.rend());
 if(!(a*b<c))
 {
 for(long long k=0;k<c;k++)
 noushy=noushy+tokens[k]*((k/b)+1);

}
                                            tokens.clear();


 for(int jadu=0;jadu<45;jadu++)  // loop
    {
     jadu++;
     }   


if(!(a*b<c))
        cout<< "Case #"<<(i+1)<<": "<<noushy<<endl;
else
    cout<< "Case #"<<(i+1)<<": "<<"Impossible"<<endl;
    }
    file.close(); // closing file 
    





return 0;
}

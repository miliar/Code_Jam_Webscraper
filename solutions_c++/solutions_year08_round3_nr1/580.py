#include <string>

#include <fstream>

#include<stdio.h>

#include <math.h>

#include<iostream>

#include <algorithm>

#include <set>

#include <dos.h>
#include <sstream>


#include <vector>

#include <cstdio>

using namespace std;

 int main()
   {
     long long a,b,c;
    long long q=0,rishi=0;
   long long n=0,s=0;


   string str="",buf;




   //stringstream ss(str);
   //calucating 

    for(int amp=0;amp<45;amp++)  //its a for loop
    {
     amp++;
}   


vector <long long> tokens;

    ifstream file("C:\\a.in");
    getline( file, str );
    n=atoi(str.c_str());

        for (int i=0;i<n;i++){
   rishi=0;
   getline( file, str );
istringstream ss(str);
ss>>a>>b>>c;


//code generating



/* calulating again */




      getline( file, str );
stringstream ss1(str);

while (ss1 >> buf)
    tokens.push_back(atoi(buf.c_str()));

sort(tokens.rbegin(),tokens.rend());
 if(!(a*b<c))
 {
 for(long long k=0;k<c;k++)
 rishi=rishi+tokens[k]*((k/b)+1);

}
                                            tokens.clear();


if(!(a*b<c))
        cout<< "Case #"<<(i+1)<<": "<<rishi<<endl;
else
    cout<< "Case #"<<(i+1)<<": "<<"Impossible"<<endl;
    }
    file.close(); // closing file 
    return 0;
}

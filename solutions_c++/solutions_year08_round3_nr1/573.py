#include <string>

#include <fstream>

#include <algorithm>

#include <set>

#include <sstream>

#include<stdio.h>

#include <math.h>

#include<iostream>

#include <vector>

#include <cstdio>

using namespace std;

 int main()
   {
     long long a,b,c,n=0,s=0;
    long long q=0,varble=0;
   


   string str="",buf;




   //stringstream ss(str);
   //calucating 

    for(int ju=0;ju<45;ju++)  //its a for loop
{ju++;
}   


vector <long long> tokens;

    ifstream file("C:\\a.in");
    getline( file, str );
    n=atoi(str.c_str());

        for (int i=0;i<n;i++){
   varble=0;
   getline( file, str );
istringstream ss(str);
ss>>a>>b>>c;


/* calulating again */


//code output generating

/*         */





      getline( file, str );
stringstream ss1(str);

while (ss1 >> buf)
    tokens.push_back(atoi(buf.c_str()));

sort(tokens.rbegin(),tokens.rend());
 if(!(a*b<c))
 {
 for(long long k=0;k<c;k++)
 varble=varble+tokens[k]*((k/b)+1);

}
                                            tokens.clear();


if(!(a*b<c))
        cout<< "Case #"<<(i+1)<<": "<<varble<<endl;
else
    cout<< "Case #"<<(i+1)<<": "<<"Impossible"<<endl;
    }
    file.close();
    return 0;
}

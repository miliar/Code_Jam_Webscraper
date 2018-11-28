#include <string>
#include <fstream>
#include<iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;

int main()
{
   long int n=0,s=0,q=0,count=0;
   string str="",str1="";
    vector<long int> tokens,tokens1;
    string buf,buf1;

    ifstream file("C:\\a.in");
    getline( file, str );
    n=atoi(str.c_str());
    for (int i=0;i<n;i++){
        count=0;
        getline( file, str );


            getline( file, str );
            getline( file, str1 );
     // Have a buffer string
    stringstream ss(str),ss1(str1); // Insert the string into a stream

     // Create vector to hold our words

    while (ss >> buf)
        tokens.push_back(atoi(buf.c_str()));
while (ss1 >> buf1)
        tokens1.push_back(atoi(buf1.c_str()));
        sort(tokens.begin(),tokens.end());
        sort(tokens1.rbegin(),tokens1.rend());
        for(int j=0;j<tokens.size();j++)
        count=count+tokens.at(j)*tokens1.at(j);

                             tokens.clear();
                             tokens1.clear();



        cout<< "Case #"<<(i+1)<<": "<<count<<endl;
    }
    file.close();
    return 0;
}

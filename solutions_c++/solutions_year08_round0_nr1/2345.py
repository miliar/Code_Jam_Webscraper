#include<vector>
#include<stack>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<map>
#include<iostream>
using namespace std;

int main()
{
int cases, iterate=0;
cin>>cases;
while(cases--)
{
iterate = iterate + 1;
int numstrs, numquers, x, y; string abc;
cin>>numstrs;
map<string,int> map2int;
cin.ignore();
for(x=0; x<numstrs; x++)
{
getline(cin, abc);
map2int[abc]=0;
}
map<string,int> map2check;
cin>>numquers;
int theAnswer=0;
cin.ignore();
while(numquers--)
{
getline(cin,abc);
if(map2int.count(abc) != 0)
{
if(map2check.count(abc) == 0)
{
map2check[abc] = 1;
}
if(map2check.size() == numstrs)
{
theAnswer = theAnswer + 1;
map2check.clear();
map2check[abc]=1;
}
}
}// end while
cout<<"Case #"<<iterate<<": "<<theAnswer<<"\n";
}//end test cases
return 0;
}//end main


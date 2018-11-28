#include<stack>
#include<cmath>
#include<vector>
#include<map>
#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
int a, b, num2count, num2case;
cin>>num2case;
num2count =1;
for(b=1; b<=num2case; b++)
{
map<string,int> chunkMap;
int strs;
int quers;
int x;
int y;
int chunkans=0;
string chunkstr;
cin>>strs;
cin.ignore();
for(a=1; a<=strs; a++)
{
getline(cin, chunkstr);
chunkMap[chunkstr]=0;
}
cin>>quers;
map<string,int> mapchunk;
cin.ignore();
for(a=1; a<=quers; a++)
{
getline(cin,chunkstr);

if( chunkMap.count(chunkstr) && ! mapchunk.count(chunkstr))
{
mapchunk[chunkstr] = 1;
}
if( chunkMap.count(chunkstr) && mapchunk.size() == strs)
{
chunkans++; // increment the answer here
mapchunk.clear();
mapchunk[chunkstr]=1;
}

}// end while
cout<<"Case #"<<num2count<<": "<<chunkans<<"\n";
}//end test cases
return 0;
}//end main


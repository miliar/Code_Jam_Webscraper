#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
#include<list>

using namespace std;
ifstream infile;
ofstream outfile;

int main(){

infile.open("B-large.in");
outfile.open("out.out");
int tc;
infile>>tc;

for(int tcc=1; tcc<=tc; tcc++){
int N,S,p,total=0;
infile>>N>>S>>p;
for(int i=0; i<N; i++){
int num;
infile>>num;
if(num<p)continue;
if(((num+2)/3)>=p)total++;
else if((S>0)&&(((num+4)/3)>=p)){S--;total++;}
}

outfile<<"Case #"<<tcc<<": "<<total<<endl;
}

return 0;
}

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <ctype.h>
#include <algorithm>
using namespace std;

string filename= "problem1in.txt";
ifstream fin(filename.c_str());
ofstream fout("problem1out.txt");

int main() {
int T;
fin>>T;
int row;
int coloumn;

for(int t=0;t<T;t++){

fin>>row;
fin>>coloumn;
char position[row][coloumn];


int vacancy[row][coloumn];
for(int i=0;i<row;i++){
for(int j=0;j<coloumn;j++) {
fin>>position[i][j];
vacancy[i][j]=0;
}
}

int counter1=0;int counter2=0;
for(int i=0;i<row;i++) {
for(int j=0;j<coloumn;j++) {

if(vacancy[i][j]==1) continue;
if(i!=row-1 && j!=coloumn-1){
if(position[i][j]=='#' && position[i+1][j]=='#' && position[i][j+1]=='#' &&  position[i+1][j+1]=='#' )
{
position[i][j]='/';
position[i][j+1]='\\';
position[i+1][j+1]='/';
position[i+1][j]='\\';
vacancy[i][j]=1;
vacancy[i][j+1]=1;
vacancy[i+1][j+1]=1;
vacancy[i+1][j]=1;
}
}

}


}
fout<<"Case #"<<t+1<<":"<<endl;
int cunter=0;
for(int i=0;i<row;i++) {
for(int j=0;j<coloumn;j++) {
    if(position[i][j]=='#') cunter++;
    }
    }

if(cunter==0)

for(int i=0;i<row;i++) {
for(int j=0;j<coloumn;j++) {
fout<<position[i][j];
}
fout<<endl;}
else
fout<<"Impossible"<<endl;
}

}
















































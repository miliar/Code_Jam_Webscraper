#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <conio.h>
#include <climits>
#include <queue>
#include <cmath>

using namespace std;

#define dv(vectName) for(int ii=0;ii<vectName.size();ii++) cout<<vectName[ii]<<' '; cout<<endl;
#define d1da(arrayName,size) for(int ii=0;ii<size;ii++) cout<<arrayName[ii]<<' '; cout<<endl;
#define d2da(arryName,row,col) for(int ii=0;ii<row;ii++){ for(int jj=0;jj<col;jj++) cout<<arryName[ii][jj]<<' '; cout<<endl; } cout<<endl; 

#define miii map<int,int>::iterator
#define mici map<int,char>::iterator
#define mcii map<char,int>::iterator
#define vii vector<int>::iteartor

#define pb(vectName,value) vectName.push_back(value);
#define mi(mapName,keyType,valType,key,val) mapName.insert(pair<keyType,valType>(key,val));



fstream inp("d-small.in",ios::in);
//FILE *out;
fstream out("d-small.out",ios::out);

void solve(int testCaseNo){
     int N;
     inp>>N;
     vector<int> X(N),Y(N),R(N);
     for(int i=0;i<N;i++){
             inp>>X[i]>>Y[i]>>R[i];
     }
     out<<"Case #"<<testCaseNo<<": ";
     if(N==1) {out<<R[0]<<endl;return;}
     if(N==2) {              
              int rad = max(R[0],R[1]);
              out<<rad<<endl;              
              return;
     }
     double dist1,dist2,dist3,mindist,rad;
     dist1=pow(double((X[0]-X[1])*(X[0]-X[1]) + (Y[0]-Y[1])*(Y[0]-Y[1])),0.5)+R[0]+R[1];
     mindist=dist1;rad=R[2];
     dist2=pow(double((X[0]-X[2])*(X[0]-X[2]) + (Y[0]-Y[2])*(Y[0]-Y[2])),0.5)+R[0]+R[2];
     if(dist2<mindist) {mindist=dist2;rad=R[1];}
     dist3=pow(double((X[1]-X[2])*(X[1]-X[2]) + (Y[1]-Y[2])*(Y[1]-Y[2])),0.5)+R[1]+R[2];
     if(dist3<mindist) {mindist=dist3;rad=R[0];}
     cout<<dist1<<' '<<dist2<<' '<<dist3<<endl;
     
     //fprintf(out,"Case #%d: ",testCaseNo);
     if((double)rad <= mindist/2) out<<mindist/2<<endl;//fprintf(out,"%lf\n",mindist/2);
     else out<<rad<<endl;//fprintf(out,"%lf\n",rad);
     
     
     
}


int main(void){
    //out=fopen("d-small.out","w");
    int C;
    inp>>C;
    for(int i=1;i<=C;i++)
            solve(i);
    getch();
    return 0;
}

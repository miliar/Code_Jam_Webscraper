#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <conio.h>
#include <climits>
#include <queue>

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



fstream inp("c-small.in",ios::in);
fstream out("c-small.out",ios::out);

int calc(vector<int> temp,int P){
    int answer=P-1;
    vector<int> empty(P+1,1);
    empty[temp[0]]=0;
    for(int i=1;i<temp.size();i++){
            int c=temp[i]-1;
            while(true){
                        if(empty[c]==0 || c==0)break;
                        else {answer++;c--;}
                        
            }
            c=temp[i]+1;
            while(true){
                        if(empty[c]==0 || c==P+1)break;
                        else {answer++;c++;}
            }
            empty[temp[i]]=0;
    }
    return answer;
}

void solve(int testCaseNo){
     int P,Q;
     inp>>P>>Q;
     vector<int> pos(Q);
     for(int i=0;i<Q;i++){
             inp>>pos[i];
     }
     vector<int> temp(pos);
     int answer=INT_MAX;
     do{
                 next_permutation(temp.begin(),temp.end());
                 int o=calc(temp,P);
                 //cout<<"current permutation is ";
                 //dv(temp);
                 //cout<<" and the answer is "<<o;
                 if(answer > o) answer=o;
                 
     }while(!equal(temp.begin(),temp.end(),pos.begin()));
     out<<"Case #"<<testCaseNo<<": "<<answer<<endl;
}


int main(void){
    int N;
    inp>>N;
    for(int i=1;i<=N;i++)
            solve(i);
    getch();
    return 0;
}

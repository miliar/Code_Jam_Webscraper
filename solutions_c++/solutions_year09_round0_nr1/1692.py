#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
#define MAXD 5001
#define MAXL 16
ifstream fin("A-large_1.in");
ofstream fout("A-large_1.out");
//ifstream fin("ALILAN.IN");

char C[MAXD][MAXL];
int l,d,T;
/* d: so tu alien
   l: do dai cac tu alien
   T: so test
*/

bool CheckInP(int d,int c,vector<char> P[]){
    for(vector<char>::iterator it=P[c].begin();it<P[c].end();it++)
        if(*it==C[d][c])
            return true;
    return false;
}

void proccess(int t){
    vector<char> P[MAXL];//mang cac tu trong ngoac
    int i=0,j,n=0,kq=0;
    bool found;
    string str;
    getline(fin,str);
    while(i<str.length()){
        if(str[i]=='('){
            ++n;
            for(j=i+1;str[j]!=')';j++)
                P[n].push_back(str[j]);
            i=j;   
        }
        else
            P[++n].push_back(str[i]);
        ++i;
    }
    //n = l
    for(i=1;i<=d;i++){//kiem tra tung tu
        found=true; 
        for(j=1;j<=l;j++)
           if(!CheckInP(i,j,P)){
               found=false;
               break;
           }
        if(found)
           ++kq;
    }
    fout<<"Case #"<<t<<": "<<kq<<endl;
}

int main(){
    int i,j;
    fin>>l>>d>>T;
    for(i=1;i<=d;i++)
        for(j=1;j<=l;j++)
           fin>>C[i][j];
    fin.ignore();
    for(int t=1;t<=T;t++)
        proccess(t);
    //system("pause");
    return 0;
}

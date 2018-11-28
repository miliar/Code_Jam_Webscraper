
#include <cstdlib>
#include <cstring>
#include <iostream>
#define REP(i,t) for(i=0;i<t;i++)

using namespace std;
int main(void){

int nCases, i, j, k, s;
int C, D, N;
char c[37][4], d[29][3];
int a, acho;
string n;
string result;
cin >> nCases;

REP(i,nCases){

cin >> C;
REP(j,C)
cin >> c[j];
cin >> D;
REP(j,D)
cin >> d[j];
cin >> N;

cin >> n;

REP(j,N){
acho = 0;









    REP(k,C){
        if(n[j]==c[k][0] || n[j]==c[k][1]){
            a = (n[j]==c[k][0]) ? 1 : 0;

                if(!acho && j-1>=0)
                    if(n[j-1] == c[k][a]){acho =1;
                    //cout << c[k][a] << " i " << endl;
                    n = n.substr(0, j-1)+c[k][2]+n.substr(j+1,n.size()-j+1); N = n.size();
                       // cout << j << " # " << n << endl;
                        j--;
                    }



        }//fim da procura por substituicao



    }// fmi da busca



            REP(k, D)
          if(!acho && j>0){//cout << n[j] << endl;
                if(n[j] == d[k][0] || n[j] == d[k][1]){
                a = n[j] == d[k][0] ? 1 : 0;
                    s = n.find_last_of(d[k][a], j-1);

                    if(s!=-1){
                    n = n.substr(j+1, n.size()-j-1);
                    N = n.size();

                  //cout << n << " - "<<j <<" - " <<d[k][a] << endl;
                    j = 0;
                    }

                }



        }//fim dos del



}

result = '[';
REP(j, N-1){
result.insert(result.end(),n[j]);
result.push_back(',');
result.push_back(' ');
//cout << "asd" << (n.at(j))+"kkk" <<endl;
}
if(N>0)
result.insert(result.end(), n[j]);
result.push_back(']');

cout << "Case #" << i+1 << ": "<<result << endl;
}


}

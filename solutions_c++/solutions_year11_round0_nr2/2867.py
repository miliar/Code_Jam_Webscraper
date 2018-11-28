#include<iostream>
#include<fstream>
#include<vector>
#include<stdlib.h>
#include<sstream>
#include<string>
#include<iterator>
#include<queue>

//#define ONLINE
using namespace std;

int main(){
    #ifndef ONLINE
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out","wt",stdout);
    #endif
    string line;
    getline(cin,line);
    int nCase = atoi(line.c_str());
    for(int i=0;i<nCase;i++){
        getline(cin,line);
        stringstream iss(line);
        int nC;
        iss>>nC;
        vector<string> C;
        C.reserve(30);
        for(int j=0;j<nC;j++){
            string cElements;
            iss>>cElements;
            C.push_back(cElements);
        }
        int nD;
        iss>>nD;
        vector<string> D;
        D.reserve(30);
        for(int j=0;j<nD;j++){
            string dElements;
            iss>>dElements;
            D.push_back(dElements);
        }
        int nN;
        iss>>nN;
        queue<char> N;
        for(int j=0;j<nN;j++){
            char nElement;
            iss>>nElement;
            N.push(nElement);
        }
        vector<char> E;
        E.reserve(100);
        for(int j=0;j<nN;j++){
            char popE=N.front();
            N.pop();
            if(E.size()>0){
                /*check combined list*/
                bool isCombine =false;
                for(int k=0;k<C.size();k++){
                    char one = C[k][0];
                    char two = C[k][1];
                    bool isSameCase1 = ((E.back()==one)&&(popE==two));
                    bool isSameCase2 = ((E.back()==two)&&(popE==one));
                    if(isSameCase1||isSameCase2){
                        E.pop_back();
                        E.push_back(C[k][2]);
                        isCombine =true;
                        break;
                    }
                }
                if(isCombine) continue;
                /* check opposed list */
                bool isOppose = false;
                for(int k=0;k<D.size();k++){
                    if(popE==D[k][0]){
                        for(int l=0;l<E.size();l++){
                            if(E[l]==D[k][1]){
                                E.clear();
                                isOppose =true;
                                break;
                            }
                        }
                    }else if(popE==D[k][1]){
                        for(int l=0;l<E.size();l++){
                            if(E[l]==D[k][0]){
                                E.clear();
                                isOppose=true;
                                break;
                            }
                        }
                    }
                    if(isOppose) break;
                }
                if(isOppose) continue;
                E.push_back(popE);
            }else{
                E.push_back(popE);
            }
        }
        cout<<"Case #"<<i+1<<": "<<"[";
        for(int j=0;j<E.size();j++){
            if(j==E.size()-1) cout<<E[j];
            else cout<<E[j]<<", ";
        }
        cout<<"]"<<endl;
    }

    return 0;
}


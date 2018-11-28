/* 
 * File:   p3.cpp
 * Author: snehasish
 *
 * Created on May 7, 2011, 4:02 PM
 */

#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

/*
 * 
 */

int main(int argc, char** argv) {
    char bases[] = {'A','S','D','F','Q','W','E','R'};
    map<char,int> base2Index;
    base2Index['A']=0;
    base2Index['S']=1;
    base2Index['D']=2;
    base2Index['F']=3;
    base2Index['Q']=4;
    base2Index['W']=5;
    base2Index['E']=6;
    base2Index['R']=7;
    int T;
    cin>>T;
    
    for(int i=1;i<=T;i++){
        char fusion[8][8];
        char difussion[8][8];
        for(int j=0;j<8;j++){
            memset(fusion[j],'0',8*sizeof(char));
            memset(difussion[j],'0',8*sizeof(char));
        }
        int C;
        cin>>C;
        string fusionInput;
        while(C--){
            cin>>fusionInput;
            char c1=fusionInput[0];
            char c2=fusionInput[1];
            char c3=fusionInput[2];

            fusion[base2Index[c1]][base2Index[c2]]=c3;
            fusion[base2Index[c2]][base2Index[c1]]=c3;
        }

        int D;
        cin>>D;
        string difInput;
        while(D--){
            cin>>difInput;
            char c1=difInput[0];
            char c2=difInput[1];

            difussion[base2Index[c1]][base2Index[c2]]='Y';
            difussion[base2Index[c2]][base2Index[c1]]='Y';
        }

        int N;
        cin>>N;
        string invoke;
        cin>>invoke;

        int basePresenceCount[8];
        memset(basePresenceCount,0,sizeof(int)*8);

        vector<char> answer;
        answer.push_back(invoke[0]);
        basePresenceCount[base2Index[invoke[0]]]++;
        
        for(int j=1;j<N;j++){
            const char c=invoke[j];
            if(answer.size()==0){
                answer.push_back(c);
                basePresenceCount[base2Index[c]]++;
                continue;
            }
            const char cl = answer[answer.size()-1];
            char r;
            if(base2Index.find(cl) != base2Index.end() && (r=fusion[base2Index[c]][base2Index[cl]]) !='0' ){
                basePresenceCount[base2Index[cl]]--;
                answer.pop_back();
                answer.push_back(r);
            } else{
                bool conflicted=false;
                for(int k=0;k<8;k++){
                    char conflict=difussion[base2Index[c]][k];
                    if( conflict == 'Y' && basePresenceCount[base2Index[bases[k]]]>0 ){
                        answer.clear();
                        memset(basePresenceCount,0,8*sizeof(int));
                        conflicted = true;
                        break;
                    }
                }
                if(!conflicted){
                    answer.push_back(c);
                    basePresenceCount[base2Index[c]]++;
                }
            }
            /*
            cout<<"Case #"<<i<<": [";

            for(int j=0;j<answer.size();j++){
                cout<<answer[j];
                if(j!=answer.size()-1){
                    cout<<", ";
                }
            }

            cout<<"]"<<endl;
            */
            
        }

        cout<<"Case #"<<i<<": [";

            for(int j=0;j<answer.size();j++){
                cout<<answer[j];
                if(j!=answer.size()-1){
                    cout<<", ";
                } 
            }

            cout<<"]"<<endl;

    }
    return 0;
}


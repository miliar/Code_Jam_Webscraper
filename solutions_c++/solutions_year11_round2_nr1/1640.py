#include <cstdio>

#include <iostream>
#include <cstdlib>

#include <vector>
#include <string>
#include <algorithm>

#define pb(n,v) n.push_back(v)
#define all(n) n.begin(),n.end()


using namespace std;

int main(){
    int T;
    cin>>T;
    int cc=0;
    while(T--){
        ++cc;
        int N;
        cin>>N;
        vector<string> table;
        for(int i=0;i<N;i++){
            string s;
            cin>>s;
            pb(table,s);
        }
        double wp[100];
        double wpeo[100][100];
        for(int i=0;i<N;i++){
            int totplayed = N - count(all(table[i]),'.');
            int totwins = count(all(table[i]),'1') ;
            wp[i] = totwins / (double) totplayed ;
            for(int j=0;j<N;j++){
                if(j!= i){
                    if(table[i][j]=='1'){
                        wpeo[i][j] = (totwins-1) / (double) (totplayed-1) ;
                    } else if(table[i][j]=='0'){
                        wpeo[i][j] = (totwins) / (double) (totplayed-1) ;
                    } else {
                        wpeo[i][j] = wp[i];
                    }
                }
            }
        }

        double work[100][3];
        for(int i=0;i<N;i++){
            work[i][0]=wp[i];
            work[i][1]=0;
            int oc = 0;
            for(int j=0;j<N;j++){
                if(table[i][j]!='.'){
                    oc ++;
                    work[i][1]+=wpeo[j][i];

                }

            }
            work[i][1] /= (double)oc;            

        }

        cout<<"Case #"<<cc<<":"<<endl;

        for(int i=0;i<N;i++){
            work[i][2]=0;
            int oc=0;
            for(int j=0;j<N;j++){
                if(table[i][j]!='.'){
                    oc ++;
                    work[i][2]+=work[j][1];
                }

            }
            work[i][2] /= (double)oc;

            printf("%.8f\n",(0.25*work[i][0]+0.50*work[i][1]+0.25*work[i][2]));
        }


    }
    return 0;

}
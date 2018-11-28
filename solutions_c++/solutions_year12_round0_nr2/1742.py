#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<string>
using namespace std;

typedef struct score{
    int a,b,c;
    bool s;
}score;
int main(int argc, char *argv[]){
    int N;
    cin>>N;
    for(int k=1;k<=N;++k){
        int num = 0;
        int T, S, p;
        vector<int> totals;
        cin>>T>>S>>p;
        vector< vector<score> > punts;
        int numSgreaterP=0;
        int numNotSgreaterP =0 ;
        int numGreaterP = 0;
        
        for(int t=0;t<T;++t){
            int sum;
            cin>>sum;
            //cerr<<"Con la suma "<<sum<<endl;
            totals.push_back(sum);
            
            score s;
            bool p1=false,p2=false, p3=false ;
            vector<score> posibles;
            for(int i=0;i<11;++i){
                if(i> sum ) continue;
                    
                for(int j=i;j<11;++j){
                    if( (i+j) > sum) continue; 
                    if( abs(i-j) > 2 ) continue;
                    for(int k=j;k<11;++k){
                        if( abs(j-k)>2 || abs(i-k)>2) continue;
                        if( (i+j+k) == sum){
                            if(i >= p || j>=p || k>=p) {
                                p1=true;
                                s.a = i;
                                s.b = j;
                                s.c = k;
                                s.s = false;
                                if( abs(i-j)==2 || abs(i-k)==2 || abs(j-k)==2){
                                    p2 = true;
                                    s.s = true;
                                }else{
                                    p3 = true;
                                }
                                posibles.push_back(s);
                            }
                        }
                    }
                }
            }
            if(p1) 
                ++numGreaterP;
            if(p2)
                ++numSgreaterP;
            if(p3)
                ++numNotSgreaterP;
            /*for(size_t i=0;i<posibles.size();++i){
                cerr<<"Sum "<<sum<<" : "<< posibles[i].a<<" "<<posibles[i].b<<" "<<posibles[i].c<<" "<<posibles[i].s<<endl;
            }*/

            punts.push_back(posibles);

        }
        //cerr<<"S ("<<S<<")>= P ("<< p<<") "<<numGreaterP<<" surprising getting P "<<numSgreaterP<<" not surprising getting P "<<numNotSgreaterP<<endl;
        
        num = min(numGreaterP, numNotSgreaterP + min(S,numSgreaterP) );
        

        cout<<"Case #"<<k<<": "<<num<<endl;
    }
    return EXIT_SUCCESS;    
}



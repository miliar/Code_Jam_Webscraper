#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char** argv) {

    //freopen("input.txt", "rt", stdin);
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int T, N, S, p, t, y, s;
    
    scanf("%d\n", &T);
    
    for(int ii=0; ii<T; ++ii){
        printf("Case #%d: ", ii+1);
        
        scanf("%d", &N);
        scanf("%d", &S);
        scanf("%d", &p);

        y = 0;
        s = 0;
        vector<int> tt;
        vector<int> ss;

        
        tt.clear();
        ss.clear();
        
        for(int i=0; i<N; i++){
            scanf("%d", &t);

            for(int aa=0; aa<11; aa++){
                for(int bb=0; bb<11; bb++){
                    for(int cc=0; cc<11; cc++){
                        if(  (abs(aa-bb)<=2 && abs(aa-cc)<=2)&&(abs(bb-cc)<=2) ){
                            if(aa+bb+cc == t){
                                     
                                    if(aa>=p || bb>=p || cc>=p){
                                        
                                            if( abs(aa-bb)==2 || abs(aa-cc)==2 || abs(bb-cc)==2 ){
       
                                                if(find(tt.begin(), tt.end(), i) == tt.end()) {
                                                    tt.push_back(i);
                                                }
                                                        
                                            }else{

                                                if(find(ss.begin(), ss.end(), i) == ss.end()) {
                                                    ss.push_back(i);
                                                }
                                            }
                                    }   
                            }
                        }
                    }
                }
            }    
        }   

        for(int qq=0; qq<tt.size(); qq++){//tt>0 && ss==0
            if(s<S){
                if(find(ss.begin(), ss.end(), tt.at(qq)) == ss.end()) {
                    tt.erase(tt.begin()+qq);
                    s++;
                    y++;
                }
            }
        } 
        
        for(int qq=0; qq<tt.size(); qq++){
            if(s<S){
                s++;
                y++;
            
                int pos = -1; 
                pos = find(ss.begin(), ss.end(), tt.at(qq)) - ss.begin();
                if(pos < ss.size()){
                    ss.erase(ss.begin()+pos);
                }
                tt.pop_back();   
            }    
        }

        y += ss.size();
        
        printf("%d\n", y);

    }
    return 0;
}


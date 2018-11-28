#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

struct Button{
       char bot;
       int number;
       };
bool advance(Button* v,int size,int &pos,char bot){
     
     int origPos = pos;
     pos++;            
     while(v[pos].bot!=bot){
                    if(pos<size-1){
                          pos++;
                          }
                    else{//The bot has finished its job
                          pos = origPos;
                          return false;
                          }
     }  
                    
     return true;
     }
int main(){
    int ncases,nbuttons,buttonNumber;
    char bot;
    Button button;
    ifstream fi;
    ofstream fo;
    Button *v; 
    int o,b;
    int po,pb;
    int time;
    bool bfinish,ofinish;
    bool advanceo;
    bool advanceb;
    
    fi.open("input2.in");
    fo.open("bot.out");
    fi>> ncases;
    
    for (int caseNumber=0;caseNumber<ncases;caseNumber++){
        o=b=-1;
        po=pb=1;
        time=0;
        bfinish=ofinish=false,
        fi >> nbuttons;
        v= new Button[nbuttons+1];
    
        for (int i = 0 ;i<nbuttons;i++){
            fi >> bot;
            fi >> buttonNumber;
            button.bot = bot;
            button.number=buttonNumber;
            v[i]=button;
            }
            
            advance(v,nbuttons,o,'O');
            advance(v,nbuttons,b,'B');
            if(o==-1){
                      ofinish=true;
            }
            if(b==-1){
                      bfinish=true;
            }
    

    while(!ofinish || !bfinish){
                     time++;
                     advanceo = advanceb = false;
                     bot = v[o].bot;
                     buttonNumber=v[o].number;
                     if(buttonNumber>po){
                        po++;
                        // cout << "Orange: go to " << po<<" ___ " << buttonNumber<< "___" << o<<endl;
                     }
                     else if(buttonNumber<po){
                        po--;
                        //cout << "Blue: go to " << po<<" ___ " << buttonNumber<< "___" << o<<endl;
                          }
                        else if((o<b || bfinish) && !ofinish){
                            //cout << "Orange: Push button " << buttonNumber<<endl;
                            advanceo=true;
                        }
                        else{
                             // cout << "Orange: Stay at button " <<po<<endl;
                        }
                     
                     bot = v[b].bot;
                     buttonNumber=v[b].number;
                     if(buttonNumber>pb){
                                         pb++;
                                         //cout << "Blue: go to " << pb<<" ___ " << buttonNumber<< "___" << b<<endl;
                     }
                     else if(buttonNumber<pb){
                                              pb--;
                                              // cout << "Blue: go to " << pb<<" ___ " << buttonNumber<< "___" << b<<endl;
                          }
                                         else if((b<o || ofinish) && !bfinish){
                                             // cout << "Blue: Push button " << buttonNumber<<endl;
                                              advanceb=true;
                                              }
                                              else{
                                                   // cout << "Blue: Stay at button " <<pb<<endl;
                                                   }
                       if(advanceo){
                                   // cout << "advance O: " << o <<endl;
                                    ofinish = !advance(v,nbuttons,o,'O');
                                    //cout <<"ofinish: " << ofinish<<endl;
                                    }
                       if(advanceb){
                                    bfinish = !advance(v,nbuttons,b,'B');
                                    }                               
                     } 

    
    cout << endl<<"Time: " << time<<endl<<endl<<endl;
    fo<<"Case #"<<caseNumber+1<<": " <<time<<endl;
}
    system("pause");
    
    fi.close();
    fo.close();
}

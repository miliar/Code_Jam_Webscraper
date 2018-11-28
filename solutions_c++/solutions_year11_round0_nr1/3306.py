#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
int main(){
    int oindex,opos,olimit;
    int bindex,bpos,blimit;
    int i,j,k,pos;
    int n,length;
    int diff=0;
    int otrack[2][100],btrack[2][100];
    char c;
    ifstream readfile("ts.txt");
    readfile>>n;
    int results[n];
    for(i=0;i<n;i++){
        results[i]=0;
        opos=1;
        bpos=1;
        olimit=-1;
        blimit=-1;
        oindex=0;
        bindex=0;
        readfile>>length;
        for(j=1;j<=length;j++){
            readfile>>c;
            readfile>>pos;
            if(c=='O'){
                olimit++;
                otrack[0][olimit]=j;
                otrack[1][olimit]=pos;

            }
            else if(c=='B'){
                blimit++;
                btrack[0][blimit]=j;
                btrack[1][blimit]=pos;
            }
        }
        while(true){
            if((oindex<=olimit)&&(bindex<=blimit)){
                if(otrack[0][oindex]<btrack[0][bindex]){
                if(opos<otrack[1][oindex]){
                   diff=otrack[1][oindex]-opos;
                   results[i]=results[i]+diff;
                   opos=otrack[1][oindex];
                   if(bpos<(btrack[1][bindex])){
                       if((btrack[1][bindex]-bpos)<diff){
                           bpos=btrack[1][bindex];
                       }
                        else if((btrack[1][bindex]-bpos)>=diff){
                            bpos=bpos+diff;
                        }
                   }
                   else if(bpos>btrack[1][bindex]){
                       if((bpos-btrack[1][bindex])<diff){
                            bpos=btrack[1][bindex];
                        }
                        else if((bpos-btrack[1][bindex])>=diff){
                            bpos=bpos-diff;
                        }
                   }
                }
                else if(opos>otrack[1][oindex]){
                   diff=opos-otrack[1][oindex];
                   results[i]=results[i]+diff;
                   opos=otrack[1][oindex];
                   if(bpos<btrack[1][bindex]){
                       if((btrack[1][bindex]-bpos)<diff){
                           bpos=btrack[1][bindex];
                       }
                        else if((btrack[1][bindex]-bpos)>=diff){
                            bpos=bpos+diff;
                        }
                   }
                   else if(bpos>btrack[1][bindex]){
                       if((bpos-btrack[1][bindex])<diff){
                           bpos=btrack[1][bindex];
                       }
                        else if((bpos-btrack[1][bindex])>=diff){
                            bpos=bpos-diff;
                        }
                   }
                }
                else{
                    results[i]++;
                    if(bpos<btrack[1][bindex]){
                        bpos++;
                    }
                    else if(bpos>btrack[1][bindex]){
                        bpos--;
                    }
                   oindex++;
                }
            }
                else if(otrack[0][oindex]>btrack[0][bindex]){
                if(bpos<btrack[1][bindex]){
                   diff=btrack[1][bindex]-bpos;
                   results[i]=results[i]+diff;
                   bpos=btrack[1][bindex];
                   if(opos<otrack[1][oindex]){
                       if((otrack[1][oindex]-opos)<diff){
                           opos=otrack[1][oindex];
                       }
                        else if((otrack[1][oindex]-opos)>=diff){
                            opos=opos+diff;
                        }
                   }
                   else if(opos>otrack[1][oindex]){
                       if((opos-otrack[1][oindex])<diff){
                           opos=otrack[1][oindex];
                       }
                        else if((opos-otrack[1][oindex])>=diff){
                            opos=opos-diff;
                        }
                   }
                }
                else if(bpos>btrack[1][bindex]){
                   diff=bpos-btrack[1][bindex];
                   results[i]=results[i]+diff;
                   bpos=btrack[1][bindex];
                   if(opos<otrack[1][oindex]){
                       if((otrack[1][oindex]-opos)<diff){
                           opos=otrack[1][oindex];
                       }
                        else if((otrack[1][oindex]-opos)>=diff){
                            opos=opos+diff;
                        }
                   }
                   else if(opos>otrack[1][oindex]){
                       if((opos-otrack[1][oindex])<diff){
                           opos=otrack[1][oindex];
                       }
                        else if((opos-otrack[1][oindex])>=diff){
                            opos=opos-diff;
                        }
                   }
                }
                else{
                    results[i]++;
                    if(opos<otrack[1][oindex]){
                        opos++;
                    }
                    else if(opos>otrack[1][oindex]){
                        opos--;
                    }
                    bindex++;
                }
            }

            }

        else if((oindex>olimit)&&(bindex<=blimit)){
            for(j=bindex;j<=blimit;j++){
                if(bpos<btrack[1][j]){
                    results[i]=results[i]+btrack[1][j]-bpos+1;
                }
                else if(bpos>btrack[1][j]){
                    results[i]=results[i]+bpos-btrack[1][j]+1;
                }
                else{
                    results[i]++;
                }
                bpos=btrack[1][j];
            }
            bindex=j;
        }
        else if((bindex>blimit)&&(oindex<=olimit)){
            for(j=oindex;j<=olimit;j++){
                if(opos<otrack[1][j]){
                    results[i]=results[i]+otrack[1][j]-opos+1;
                }
                else if(opos>otrack[1][j]){
                    results[i]=results[i]+opos-otrack[1][j]+1;
                }
                else{
                    results[i]++;
                }
                opos=otrack[1][j];
            }
            oindex=j;
        }
        else if((bindex>blimit)&&(oindex>olimit)){
            break;
        }
    }
}
    ofstream outfile;
    outfile.open("OH.txt");
    for(i=0;i<n;i++){
        outfile<<"Case #"<<i+1<<": "<<results[i]<<endl;
        //cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
    }
    return 0;
}



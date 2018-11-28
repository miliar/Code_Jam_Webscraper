#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char c[200];
int o[200];
int b[200];
int o_ind=0;
int b_ind=0;

int xd(int m){
    int o_pos=1;
    int b_pos=1;
    int j=0;
    int t=0;
    int s=0;
    while(j<m){
              // cout<<c[j]<<endl;
                if(c[j]=='O'){
                              if(o_pos==o[o_ind]){
                                                  t += 1;
                                                  o_ind++;
                                                  j++;
                                                       if(b_pos<b[b_ind])   b_pos++;
                                                       else if(b_pos>b[b_ind])     b_pos--;
                              } else if(o_pos<o[o_ind]){
                                                       o_pos++;
                                                       if(b_pos<b[b_ind])   b_pos++;
                                                       else if(b_pos>b[b_ind])     b_pos--;
                              } else if(o_pos>o[o_ind]){
                                                       o_pos--;
                                                       if(b_pos<b[b_ind])   b_pos++;
                                                       else if(b_pos>b[b_ind])     b_pos--;
                              }
                } else {
                              if(b_pos==b[b_ind]){
                                                  t += 1;
                                                  b_ind++;
                                                  j++;
                                                       if(o_pos<o[o_ind])   o_pos++;
                                                       else if(o_pos>o[o_ind])     o_pos--;
                              } else if(b_pos<b[b_ind]){
                                                       b_pos++;
                                                       if(o_pos<o[o_ind])   o_pos++;
                                                       else if(o_pos>o[o_ind])     o_pos--;
                              } else if(b_pos>b[b_ind]){
                                                       b_pos--;
                                                       if(o_pos<o[o_ind])   o_pos++;
                                                       else if(o_pos>o[o_ind])     o_pos--;
                              }
                }
                //cout<<
                s++;
    } 
    return s;               
}
    
int main(){
        ifstream fin("input.txt");
    ofstream fout("output.txt");
    int cases=0;
    int mv=0;
    fin>>cases;
    for(int x=1;x<=cases;x++){
                          fin>>mv;
                          o_ind=0;
                          b_ind=0;
                          for(int ctr=0;ctr<mv;ctr++){
                                  fin>>c[ctr];
                                  if(c[ctr]=='O'){     
                                                       fin>>o[o_ind];
                                                       o_ind++;
                                  } else {
                                                       fin>>b[b_ind];
                                                       b_ind++;
                                  }
                          }
                          o_ind=0;
                          b_ind=0;
                          fout<<"Case #"<<x<<": "<<xd(mv)<<endl;
    }

    return 0;
}

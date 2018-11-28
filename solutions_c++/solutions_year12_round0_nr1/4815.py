#include<iostream>
#include<conio.h>
#include<fstream>

using namespace std;

int t;
string s;
char g[30][100];
string spare;
int linesize;
int i[200];

 
main(){
int j=0;       
i[32] = 32 ;
i[121] = 97;
i[110] = 98;
i[102] = 99;
i[105] = 100; 
i[99] = 101;
i[119] = 102;
i[108] = 103;
i[98] = 104;
i[107] = 105 ;
i[117] = 106;
i[111] = 107 ;
i[109] = 108 ;
i[120] = 109 ;
i[115] = 110 ;
i[101] = 111;
i[118] = 112;
i[122] = 113;
i[112] = 114;
i[100] = 115;
i[114] = 116;
i[106] = 117;
i[103] = 118 ;
i[116] = 119;
i[104] = 120;
i[97] = 121;
i[113] = 122;
i[0]=0;
       ifstream sobj("A-small-attempt3.in");
       ofstream gobj("op1.in");
              sobj>>t;
              getline(sobj,spare);
              while(getline(sobj,s)){
                            
                                     linesize=s.size();
                                     for(int a=0;a<=linesize;a++){
                                     g[j][a]=i[s[a]];
                                     }    
                                       j++;     }
                                       for(int j=0;j<30;j++){
                                               gobj<<"Case #"<<j+1<<": ";
                                               for (int k=0;k<100;k++){
                                                   if(g[j][k]=='\0')
                                                   break;
                                                   else
                                                   gobj<<g[j][k];}
                                                   gobj<<endl;
                                                   }
                                            
                              sobj.close();
                              gobj.close();
                              getch();
                              }             
                                                          

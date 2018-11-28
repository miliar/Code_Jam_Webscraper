#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int n,i;
    string output[5]={"","X won","Draw","Game has not completed","O won"};//              0      1     2               3              4
    cin>>n;
    for(i=1;i<=n;i++){
        int j,k,flag=2,empty=0;
        string m[5][5],tt[5];
        for(j=1;j<=4;j++){cin>>tt[j];}
        for(j=1;j<=4;j++){
            m[j][1]=tt[j][0];
            m[j][2]=tt[j][1];
            m[j][3]=tt[j][2];
            m[j][4]=tt[j][3];
        }
        for(j=1;j<=10;j++){
            if(j<=4){
                for(k=1;k<=4;k++){
                    string tp;
                    if(m[k][1]=="."){tp=".";}
                    else if(m[k][1]=="X"){tp="X";}
                    else if(m[k][1]=="T"){tp="T";}
                    else if(m[k][1]=="O"){tp="O";}
                    if(tp=="X"){
                        
                        if(m[k][2]==tp||m[k][2]=="T"){
                            if(m[k][3]==tp||m[k][3]=="T"){
                                if(m[k][4]==tp||m[k][4]=="T"){
                                    flag=1;break;
                                }
                            }
                        } 
                    }else if(tp=="O"){
                        if(m[k][2]==tp||m[k][2]=="T"){
                            if(m[k][3]==tp||m[k][3]=="T"){
                                if(m[k][4]==tp||m[k][4]=="T"){
                                    flag=4;break;
                                }
                            }
                        } 
                    }else if(tp=="T"){
                        if(m[k][2]=="X" && m[k][3]=="X" && m[k][4]=="X")
                        {flag=1;break;    
                        }else 
                        if(m[k][2]=="O" && m[k][3]=="O" && m[k][4]=="O")
                        {flag=4;break;}
                    }
                }

            }else if(j<=8&&j>4&&flag!=3){
                
                for(k=1;k<=4;k++){
                    string tp;
                    if(m[1][k]=="."){tp=".";}
                    else if(m[1][k]=="X"){tp="X";}
                    else if(m[1][k]=="O"){tp="O";}
                    else if(m[1][k]=="T"){tp="T";}
                    if(tp=="X"){
                        if(m[2][k]==tp||m[2][k]=="T"){
                            if(m[3][k]==tp||m[3][k]=="T"){
                                if(m[4][k]==tp||m[4][k]=="T"){
                                    flag=1;break;
                                }
                            }
                        } 
                    }else if(tp=="O"){
                        if(m[2][k]==tp||m[2][k]=="T"){
                            if(m[3][k]==tp||m[3][k]=="T"){
                                if(m[4][k]==tp||m[4][k]=="T"){
                                    flag=4;break;
                                }
                            }
                        } 
                    }else if(tp=="T"){
                        if(m[2][k]=="X"&&m[3][k]=="X"&&m[4][k]=="X"){
                        flag=1;break;    
                        }else 
                        if(m[2][k]=="O"&&m[3][k]=="O"&&m[4][k]=="O")
                        {flag=4;break;}
                    }
                }
            }else if(j==9&&flag!=3){
                    string tp;
                    if(m[1][1]=="."){tp=".";}
                    else if(m[1][1]=="X"){tp="X";}
                    else if(m[1][1]=="O"){tp="O";}
                    else if(m[1][1]=="T"){tp="T";}
                    if(tp=="X"){
                        if(m[2][2]==tp||m[2][2]=="T"){
                            if(m[3][3]==tp||m[3][3]=="T"){
                                if(m[4][4]==tp||m[4][4]=="T"){
                                    flag=1;
                                }
                            }
                        } 
                    }else if(tp=="O"){
                        if(m[2][2]==tp||m[2][2]=="T"){
                            if(m[3][3]==tp||m[3][3]=="T"){
                                if(m[4][4]==tp||m[4][4]=="T"){
                                    flag=4;
                                }
                            }
                        } 
                    }else if(tp=="T"){
                        if(m[2][2]=="X"&&m[3][3]=="X"&&m[4][4]=="X"){
                        flag=1;   
                        }else 
                        if(m[2][2]=="O"&&m[3][3]=="O"&&m[4][4]=="O")
                        {flag=4;}
                    }
            }else if(j==10&&flag!=3){
                    string tp;
                    if(m[1][4]=="."){tp=".";}
                    else if(m[1][4]=="X"){tp="X";}
                    else if(m[1][4]=="T"){tp="T";}
                    else if(m[1][4]=="O"){tp="O";}
                    if(tp=="X"){
                        if(m[2][3]==tp||m[2][3]=="T"){
                            if(m[3][2]==tp||m[3][2]=="T"){
                                if(m[4][1]==tp||m[4][1]=="T"){
                                    flag=1;
                                }
                            }
                        } 
                    }else if(tp=="O"){
                        if(m[2][3]==tp||m[2][3]=="T"){
                            if(m[3][2]==tp||m[3][2]=="T"){
                                if(m[4][1]==tp||m[4][1]=="T"){
                                    flag=4;
                                }
                            }
                        } 
                    }else if(tp=="T"){
                        if(m[2][3]=="X"&&m[3][2]=="X"&&m[4][1]=="X"){
                        flag=1;   
                        }else 
                        if(m[2][3]=="O"&&m[3][2]=="O"&&m[4][1]=="O")
                        {flag=4;}
                    }
            }
 
            

        } 
        int x,y;
       
        for(x=1;x<=4;x++){
            for(y=1;y<=4;y++){
                if(m[x][y]=="."){empty=1;break;}
            }
            if(empty==1){break;}
        }     
        if(empty==1&&flag==2){flag=3;}

        cout<<"Case #"<<i<<": "<<output[flag]<<endl;
    }

      
    return 0;
}
   
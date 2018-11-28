#include <stdio.h>
#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

double mid,p[202],pos[21000];
int st;
int t,c,d,num[202];
    
bool isok(double dis){
     double ppos[21000];
     ppos[0] = pos[0]-dis;
     for (int i = 1;i<st;i++){
         if ((pos[i]+dis-ppos[i-1])<d) return false;
         else
         if ((pos[i]-dis-ppos[i-1])<=d){
            ppos[i] = ppos[i-1]+d;
         }
         else
            ppos[i] =  pos[i]-dis;
     }
     return  true;
}

int main(){
    
    ifstream in("b.in");
    ofstream out("b.out");  
    

    
    in >> t;
    
    for(int i=0;i<t;i++){
            
            in >> c >> d;
            
            for(int j=0;j<c;j++){
                    in >> p[j] >>num[j];
            }
            
            for (int j=0;j<c;j++){
                int tmp = j;
                for (int k =j+1;k<c;k++){
                    if (p[tmp]> p[k]) tmp = k;
                }
                if (tmp != j){
                   double temp = p[tmp];
                   p[tmp] = p[j];
                   p[j] = temp;
                   int tempp = num[tmp];
                   num[tmp] = num[j];
                   num[j] = tempp;
                }
            }
            
            st = 0;
            
            for(int j=0;j<c;j++){
                for (int k =0;k<num[j];k++){ 
                    pos[st++] = p[j]; 
                }   
            }
            int sb = 1;
            
            double aa = 0;
            bool ss = isok(aa);
            if (ss){
                out << "Case #" << i+1<<": "<< 0.0<<endl;
            }
            else{
                double mm = 20000000;
                double bo = 0;
                //double dis = mm;
                while((mm-bo)>0.000001){
                   mid = (bo+mm)/(double)2;
                   if (isok(mid)){
                      mm = mid;
                   }
                   else{
                      bo = mid;  
                   }
                }
                out << "Case #" << i+1<<": "<<mid<<endl;
            }
    }
    
    system("pause");
    
}

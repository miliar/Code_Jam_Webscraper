#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

int t,n,pO,pB,index;
vector<char> list_r;
vector<int> list_p;
list<int> list_pO;
list<int> list_pB;
int main(void){
    char r[2];
    int p,fO,fB;
    FILE *in,*out;
    in=fopen("A-large.in","r");
    out=fopen("out.txt","w");
    fscanf(in,"%d",&t);
    for (int i=1;i<=t;i++){
        list_r.clear();
        list_p.clear();
        pO=1;
        pB=1;
        index=0;
        fscanf(in,"%d",&n);   
        for (int j=0;j<n;j++){
            fscanf(in,"%s %d",&r,&p);
            list_p.push_back(p);
            list_r.push_back(r[0]);         
            if (r[0]=='O')
               list_pO.push_back(p);
               else
                   list_pB.push_back(p);
            }
        
        int j;
        for (j=1;index<list_r.size();j++){
            fO=0;
            fB=0;
            switch (list_r[index]){
                   case 'O':
                        if (list_p[index]==pO){
                           index++;            
                           list_pO.pop_front();
                           fO=1;
                           }            
                        break;
                   case 'B':
                        if (list_p[index]==pB){
                           index++;
                           list_pB.pop_front();
                           fB=1;
                           }
                        break;
                   }
            if (list_pO.front()>pO&&fO==0)
               pO++;
            if (list_pO.front()<pO&&fO==0)
               pO--;
            if (list_pB.front()>pB&&fB==0)
               pB++;            
            if (list_pB.front()<pB&&fB==0)
               pB--;            
            }            
        fprintf(out,"Case #%d: %d\n",i,j-1);
        }
    fclose (in);
    fclose (out);
    return 0;
    }

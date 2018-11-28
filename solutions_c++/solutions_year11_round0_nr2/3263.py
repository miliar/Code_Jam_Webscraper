//18min 49seg
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

    int t,c,d,n;
    vector<string> list_combine;
    vector<string> list_opp;

char busca(char p1,char p2){
     string p;
     for (int i=0;i<c;i++){
         p=list_combine[i];
         if ((p[0]==p1&&p[1]==p2)||(p[1]==p1&&p[0]==p2))
            return p[2];
         }
     return '\0';
     }

bool busca_opp(char p1,char p2){
     string p;
     for (int i=0;i<d;i++){
         p=list_opp[i];
         if ((p[0]==p1&&p[1]==p2)||(p[1]==p1&&p[0]==p2))
            return true;
         }
     return false;
     }

int main(void){
    int salta=0;
    char t2;
    char cad[101];
    vector<char> pal;
    string temp;
    FILE *in,*out;
    in=fopen("B-large.in","r");
    out=fopen("outLarge.txt","w");
    fscanf(in,"%d",&t);
    for (int i=1;i<=t;i++){
        list_combine.clear();
        list_opp.clear();
        pal.clear();
        fscanf(in,"%d",&c);   
        for (int j=0;j<c;j++){
            fscanf(in,"%s",&cad);
            temp.assign(cad);
            list_combine.push_back(temp);
            }
        fscanf(in,"%d",&d);        
        for (int j=0;j<d;j++){
            fscanf(in,"%s",&cad);
            temp.assign(cad);
            list_opp.push_back(temp);
            }
        fscanf(in,"%d",&n);        
        fscanf(in,"%s",&cad);
        for (int j=0;j<n;j++){
            pal.push_back(cad[j]);            
            if (pal.size()>=2){
               t2=busca(pal[pal.size()-1],pal[pal.size()-2]);
               if (t2){
                  pal.pop_back();
                  pal.pop_back();
                  pal.push_back(t2);            
                  }
                }
            for (int k=0;k<pal.size();k++)
                if (busca_opp(pal[k],pal[pal.size()-1])){
                   pal.clear();
                   salta=1;
                   break;
                   }
            }
        fprintf(out,"Case #%d: [",i);
        for (int k=0;k<pal.size();k++){
            fprintf(out,"%c",pal[k]);
            if (k<pal.size()-1){
               fprintf(out,", ");
               }               
            }
            fprintf(out,"]\n");                            
        }
    fclose (in);
    fclose (out);
    return 0;
    }

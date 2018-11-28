#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <string>
#include <vector>

using namespace std;

int main(void){
    int l,d,n,k,t,temp;
    FILE *out;
    out=fopen("1-large.out","w");
    string p;
    scanf("%d %d %d",&l,&d,&n);
    vector <string> v(d);
    vector <string> pat;
    for (int i=0;i<d;i++){
        cin >> v[i];
        }

    for (int i=0;i<n;i++){
       k=0;
       cin >> p;
       pat.clear();
       
       t=-1;
       temp=0;
       for (int j=0;j<p.size();j++){       
           if (p.at(j)=='('){
              temp=1;
              t++;
              }
           else if(p.at(j)==')'){
                temp=0;
                }
           else{
                if (temp==0)
                   t++;
                if (pat.size()>t){
                    if (pat[t].size()==0){
                       pat.push_back((string)"");
                       pat[t].append(1,p.at(j));
                       }
                       else
                           pat[t].append(1,p.at(j));
                   }
                   else{
                        pat.push_back((string)"");
                        pat[t].append(1,p.at(j));
                        }
                }
           }

       for (int j=0;j<pat.size();j++){       
           cout << pat[j] << endl;
           }   
       
        for (int j=0;j<d;j++){
            temp=0;        
            for (int a=0;a<l&&temp==0;a++){            
                if (pat[a].find(v[j].at(a))==string::npos)
                   temp=1;
                }
            if (temp==0)
               k++;
            }
      
        
        fprintf(out,"Case #%d: %d\n",i+1,k);
        }
    getch();
    }

#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int t,n,m,r;
    char *pch;
    char *apch;
    char *p;
    scanf("%d",&t);
    vector<string> v;
    vector<string>::iterator it;
    string s;
    for (int t2=1;t2<=t;t2++){
        r=0;
        v.clear();
        scanf("%d %d",&n,&m);
        for (int n2=0;n2<n;n2++){
            cin >>  s;  
            p = new char [s.size()+1];         
            strcpy (p, s.c_str());
            s.clear();
            pch = strtok (p,"/");
            while (pch != NULL){
                  //printf ("%s ",pch);
                  s.append(pch);
                  it=find(v.begin(),v.end(),s);                  
                  if (it==v.end()){
                     v.push_back(s);
                     //cout << s << endl;
                     }
                  pch = strtok (NULL, "/");
                  }            
            }


        for (int m2=0;m2<m;m2++){
            cin >>  s;  
            p = new char [s.size()+1];         
            strcpy (p, s.c_str());
            s.clear();
            pch = strtok (p,"/");
            while (pch != NULL){
                  //printf ("%s ",pch);
                  s.append(pch);
                  it=find(v.begin(),v.end(),s);                  
                  if (it==v.end()){
                     v.push_back(s);
                     //cout << s << endl;
                     r++;
                     }
                  pch = strtok (NULL, "/");
                  }            
            }
                
        printf("Case #%d: %d\n",t2,r);
        }
    getch();
    return 0;
    }

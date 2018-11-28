#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include<conio.h>
using namespace std;

#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt7.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

    int i,j,k,n;
    char T[]=" abcdefghijklmnopqrstuvwxyz";
    char N[]=" yhesocvxduiglbkrztnwjpfmaq";
    //char P[100];
    
    char c;
    cin>>n;
    string P; 
    getline(cin,P);
    for(k=0; k<n;k++){
    i=0;
    getline(cin,P);
    
    cout<<"Case #"<<k+1<<": ";

    while(P[i]!='\0')
    {
                     for(j=0;j<strlen(T);j++)
                     {
                                      if(P[i]==T[j])
                                      {
                                                    cout<<N[j];
                                                    break;
                                                    }
                                                    
                                      
                                      }
                     i++;
                     }
                     cout<<"\n";
   }
   
        
    return 0;
    }
 

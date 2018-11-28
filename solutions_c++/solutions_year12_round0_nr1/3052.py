/*

 E-Mail : mayank.ry@gmail.com
 Just For You :)

 */

#include <cstring>
#include <string.h>
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

using namespace std;


#define SMALL
//#define LARGE
int main() {
int N,i,j,k,l,m;
char ch[1001],code[]={ 'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large-practice.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
    cin>>N;
    cin.getline(ch,1000);
    for(j =1;j<=N;j++)
    {
          cin.getline(ch,1000);
          printf("Case #%d: ",j);
          for(i =0;ch[i]!='\0';i++)
           {
                if(ch[i]==' ')
                        cout<<' ';
                else
                    printf("%c",code[int(ch[i])-97]);
                
           }
           cout<<"\n";
    }
    /*for(j =1;j<=N;j++)
    {
          cin.getline(ch,1000);
          for(i =0;ch[i]!='\0';i++); 
         
          printf("Case #%d: ",j); 
        do 
           {  for(k =i-1;ch[k]!=' '&&k>=0;k--);
            for(l=k+1;l<i;l++)   
            cout<<ch[l];
            cout<<' ';
            // printf("%c",ch[k]);
             i=k;
        //cout<<k;
        }while(k>=0);
        cout<<'\n';
            } */
              
  

	return 0;

}

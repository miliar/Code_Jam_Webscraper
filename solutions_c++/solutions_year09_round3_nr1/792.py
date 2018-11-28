#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

int main(){
    int n,caso=1;
    string s;
    scanf("%d\n",&n);
    while(n--){
               getline(cin,s);
               string aux=s;
               sort(aux.begin(),aux.end());
               set <char> se;
               map <char,int> mm;
               mm[s[0]]=1;
               int val=0;
               se.insert(s[0]);
               for(int i=0;i<s.size();i++){
                       if(find(se.begin(),se.end(),s[i])==se.end()){ 
                           if(val==1) val++;
                           mm[s[i]]=val++;
                           //printf("%c\n",s[i]);
                           se.insert(s[i]);
                       }
               }
               /*set <char> :: iterator it= se.begin();
               int pos=0;
               for(i;it!=se.end();it++,pos++){
                    if(*it==s[0]) continue;
                     mm[*it]=pos;
               }*/
               char c=se.size(),c1;
               if(c==1)
                c++;
               //printf("%d\n",c);
               /*if(c<=57) 
                   c=c-47;
               else 
                   c=(c-'a')+11;
               */long long int suma=0;
               //printf("%d\n",c);
               for(int i=0;i<s.size();i++){
                   suma=suma*c+mm[s[i]];
               }
               printf("Case #%d: ",caso++);
               printf("%lld\n",suma);
    }
    return 0;
}

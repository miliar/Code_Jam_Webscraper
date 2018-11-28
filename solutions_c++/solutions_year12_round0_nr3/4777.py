#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;
 
int val(string s){
        int res=0;
        for( int i=0;i<s.length();i++ )
                res=res*10+s[i]-'0';
        return res;
}
 
void procesa(int a, int b,set<pair<int,int> > &s){
        int aa=a;
        string num="";
        while( a>0 ){
                num+=a%10+'0';
                a/=10;
        }
        reverse( num.begin(), num.end() );
        for(int i=0;i<num.length()-1;i++){
                string nv=num;char t=nv[0];nv.erase(nv.begin());
                nv+=t;
                if( val(nv)>aa && val(nv)<=b ) s.insert( make_pair(aa,val(nv)) );
                num=nv;
        }
}
 
int main(){
        
        int t;
        int cont=1;
        int a, b;
        scanf("%d", &t);
        while(t--){
                set< pair<int,int> > s;
                scanf("%d%d", &a, &b);
                for( int i=a;i<=b;i++ ){
                        procesa(i,b,s);
                }
                cout<<"Case #"<<cont++<<": "<<s.size()<<endl;
        }
         
        return 0;
}
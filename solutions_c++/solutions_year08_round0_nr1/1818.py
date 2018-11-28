#include <algorithm>
#include<iostream>
#include<map>
#include<string>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
            int s,u,q,out,ch=0,max;
            int odl[100],wej[1000];
            string in;
            map <string,int> m;
            cin >>s;
            cin.ignore(7,'\n'); 
            for(int j=0;j<s;j++){
                    getline(cin,in);
                    m[in]=j;
                    };
            u=s; out=0;
            cin >> q;
            cin.ignore(7,'\n'); 
            for(int j=0;j<q;j++){
                    getline(cin,in);
                    wej[j]=m[in];
                    };
            out=0; bool go=true;
            while(go){
                      go=false;
                      for(int j=0;j<s;j++) odl[j]=2000;
                      for(int j=q-1;j>=ch;j--)  odl[wej[j]]=j;
                      max=*max_element(odl,odl+s);
                      if(max<2000){
                                   out++;
                                   go=true;
                                   ch=max;
                                   };                      };
            cout << "Case #"<<i<<": "<<out<<endl;
            };
    
    return 0;   
};

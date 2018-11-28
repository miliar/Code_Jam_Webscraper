#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

map <string , int> m;
vector <string > v;

int tama,cont;

void checa(int val,string s){
    //printf("%d %d %s\n",val,tama,s.c_str());
    if(val==tama) {
        //printf("%s %d\n",s.c_str(),m[s]);
        cont+=m[s];
        return;
    }
    int tamm=v[val].size();
    string aux;
    for(int i=0;i<tamm;i++){
        aux=s+v[val][i];
        //puts(aux.c_str());
        checa(val+1,aux);
        //puts("regreso");
    }
}


int main(){
    int n,mm,x;
    char buffer[1000];
    string g;
    scanf("%d%d%d\n",&n,&mm,&x);
    for(int i=0;i<mm;i++){
        //puts("aa");
        gets(buffer);
        m[buffer]++;
        //printf("%s %d\n",buffer,m[buffer]);
    }
    for(int i=1;i<=x;i++){
        gets(buffer);
        int tam=strlen(buffer);
        //printf("%d\n",tam);
        v.clear();
        string s="";
        for(int j=0;j<tam;j++){
            if(buffer[j]=='('){
                j++;
                for(;buffer[j]!=')';j++)
                    s+=buffer[j];
                v.push_back(s);
                s="";
            }else{
                s+=buffer[j];
                v.push_back(s);
                s="";
            }
        }
        //puts("salio");
//        for(int i=0;i<v.size();i++)
//            puts(v[i].c_str());
        tama=v.size();
        cont=0;
        checa(0,"");
        printf("Case #%d: %d\n",i,cont);
    }
    return 0;

}


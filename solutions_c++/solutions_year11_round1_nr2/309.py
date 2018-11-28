#include<cstdio>
#include<iostream>
#include<set>
#include<vector>
#include<cstring>

using namespace std;

#define max_n 105
#define max_m 15

int n,m;
char dict[max_n][15];
char list[max_m][30];

int wyn[max_n][max_m];
int aktList;

void rob(int k){
    set<int> slowa;
    set<char> litery;
    int ileZgadlem=0;
    for(int i=0;i<n;i++){
        if(strlen(dict[i])==strlen(dict[k])){
            slowa.insert(i);
            for(int j=0;j<strlen(dict[i]);j++)
                litery.insert( dict[i][j]);
        }
    }
    int wynik=0;
    for(int dupa=0;dupa<26;dupa++){
        char i = list[aktList][dupa];
        if(slowa.size()==1){
            wyn[k][aktList]=wynik;
            return;
        }
        litery.clear();
        for(set<int>::iterator it=slowa.begin();it!=slowa.end();it++){
            for(int j=0;j<strlen(dict[k]);j++)
                litery.insert(dict[*it][j]);
        }
        if(litery.find(i)!=litery.end()){
           vector<int> wslowie;
           for(int j=0;j<strlen(dict[k]);j++)
               if(dict[k][j]==i){ wslowie.push_back(j);}//cout<<"DORZUCAM "<<j<<" do wslowie"<<endl;}
           
           vector<int> doUsuniecia;

           for(set<int>::iterator it = slowa.begin(); it!=slowa.end();it++){
              vector<int> wslowie2;
              for(int j=0;j<strlen(dict[*it]);j++)
                if(dict[*it][j]==i) wslowie2.push_back(j);
                
              if(wslowie.size()!=wslowie2.size()) doUsuniecia.push_back(*it);
              else{
                for(int ii=0;ii<wslowie.size();ii++){
                    if(wslowie[ii]!=wslowie2[ii]) doUsuniecia.push_back(*it);
                }
              }
           }
           ileZgadlem+=wslowie.size();
           if(wslowie.size()==0) wynik++;
           for(int kij=0;kij<doUsuniecia.size();kij++)
               slowa.erase(doUsuniecia[kij]);
           if(ileZgadlem == strlen(dict[k])){
               wyn[k][aktList] = wynik;
               return;
            }
        }
        if(slowa.size()==1){
            wyn[k][aktList]=wynik;
            return;
        }
    }
    if(slowa.size()==1){
        wyn[k][aktList]=wynik;
        return;
    }


}


int main(){
    int Z;
    scanf("%d",&Z);
    for(int z=1;z<=Z;z++){
        scanf("%d%d",&n,&m);
        for(int j=0;j<n;j++)
          scanf("%s",dict[j]);
        
        for(int j=0;j<m;j++)
            scanf("%s",list[j]);
        printf("Case #%d:",z);
       
      

        for(int j=0;j<m;j++){
            aktList = j;
            for(int k=0;k<n;k++) 
                rob(k);
            int best=wyn[0][aktList];int dla=0;
            for(int k=1;k<n;k++){
                if(best<wyn[k][aktList]){
                    dla=k;
                    best = wyn[k][aktList];
                }
            }
            printf(" %s",dict[dla]);
        }
        printf("\n");

    }

    return 0;
}

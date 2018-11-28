#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

const double PI=3.14159265358979323846264338327950288;
ifstream fin;
ofstream fout;

int prime[1001];
int C=1;

void prepare(){
     int i,j,k;
     prime[0]=2;
     //count=1;
     bool p;
     for (i=3;i<1001;i++){
         p=1;
         for (j=0;j<C;j++){
             if (i%prime[j] == 0) p=0;
         }
         if(p){
               prime[C]=i;
               C++;
         }
     }
     return;
}

void _main(){
     int N;
     fin>>N;
     if(N==1){
              fout<<0;
              return;
     }
     int i,j,k;
     int app[1001];
     memset(app,0,sizeof(app));
     for (i=0;i<C;i++) app[i]=floor(log(double(N))/log(double(prime[i])));
     
     int max,min;
     min=0;max=1;
     for (i=0;i<C;i++){
         if(app[i]){
                    min++;
                    max += app[i];
         }
     }
     fout<<max-min;
     return;
}

int main(){
    fin.open("sample.in");
    fout.open("result.out");
    int T;
    fin>>T;
    prepare();
    for(int i=0;i<T;i++){
            fout<<"Case #"<<i+1<<": ";
            _main();
            fout<<endl;
    }
}

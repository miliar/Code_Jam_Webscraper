#include <fstream>
#include <iostream>
using namespace std;
int l,d,n;
char da[5000][15],na[500];
int w[5000];
int main(){
    ifstream fin("A-small-attempt0.txt");
    ofstream fout("A-small.out");
    fin>>l>>d>>n;
    for(int i=0;i!=d;i++){
     for(int k=0;k!=l;k++)
      fin>>da[i][k];}
    cout<<n<<l;
    for(int i=0;i!=n;i++){
        for(int k=0;k!=d;k++){
            w[k]=0;
            }
        for(int k=0;k!=l;k++){
            char temp;
            fin>>temp;
            if(temp=='('){
                fin>>temp;
                while(temp!=')'){
                    for(int f=0;f!=d;f++){
                        if(da[f][k]==temp) w[f]++;
                        }
                    fin>>temp;
                    }
                }
            else{
                for(int f=0;f!=d;f++){
                        if(da[f][k]==temp) w[f]++;
                        }
                }
            }
          int sum=0;
          for(int f=0;f!=d;f++){
                        if(w[f]==l) sum++;
                        }
        fout<<"Case #"<<i+1<<": "<<sum<<endl;
        }
    }

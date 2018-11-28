#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<fstream>
using namespace std;
int poz[2];
int t,n,h; char c;
struct korak{
    int b,br;
    korak(int _b=0, int _br=0){b=_b; br=_br;}
}a[110];

int pomakni(int x){
    //cout<<x<<" "<<poz[0]<<" "<<poz[1]<<" "<<h<<endl;
    int pz1,pz2,f1,f2;
    pz1=poz[0]; pz2=poz[1]; f1=f2=-1;
    for (int i=x; i<n; ++i){
        if(f1==-1&&a[i].b==0&&a[i].br!=poz[0]) {pz1=a[i].br; f1=0;}
        if(f2==-1&&a[i].b==1&&a[i].br!=poz[1]) {pz2=a[i].br; f2=0;}
        if (!f1&&!f2) break;
    }
    if (!f1&&!f2) --h;
    if (poz[0]<pz1){ poz[0]++; ++h;} else if (poz[0]>pz1){ poz[0]--; ++h;}
    if (poz[1]<pz2){ poz[1]++; ++h;} else if (poz[1]>pz2){ poz[1]--; ++h;}
    //cout<<x<<" "<<poz[0]<<" "<<poz[1]<<" "<<h<<endl;
    return 0;
}



int main(){
    ifstream fin("in.in");
    ofstream fout("out.out");
    fin>>t;
    for (int tt=0; tt<t; ++tt){
        fin>>n;
        for (int i=0; i<n; ++i){
            fin>>c>>h;
            a[i]=korak(c=='B',h-1);
        }h=0;
        poz[0]=poz[1]=0;
        for(int i=0; i<n;++i){
            while(poz[a[i].b]!=a[i].br){ pomakni(i);}
            ++h; int pz1,f1;
                pz1=poz[!a[i].b]; f1=-1;
                for (int j=i; j<n; ++j){
                    if(f1==-1&&a[j].b==!a[i].b){ pz1=a[j].br; f1=0; break;}
                }
                if (poz[!a[i].b]<pz1){ poz[!a[i].b]++; } else if (poz[!a[i].b]>pz1){ poz[!a[i].b]--; }
                //cout<<"MOV "<<poz[0]<<" "<<poz[1]<<" "<<h<<endl;
        }
        fout<<"Case #"<<tt+1<<": "<<h<<endl;
    }
    return 0;
}

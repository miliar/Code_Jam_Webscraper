#include <iostream>
#include <fstream>
using namespace std;
int f_min(int a,int b,int c){
    if(a<=b&&a<=c)return a;
    if(b<=a&&b<=c)return b;
    if(c<=a&&c<=b)return c;
}
int f_max(int a,int b,int c){
    if(a>=b&&a>=c)return a;
    if(b>=a&&b>=c)return b;
    if(c>=a&&c>=b)return c;
}

int main()
{
    int T,N,S,p,ti;
    ifstream ifile;
    ifile.open("input.txt");
    ofstream ofile;
    ofile.open("output.txt");
    ifile>>T;
    for(int i=0;i<T;i++){
        ifile>>N>>S>>p;
        int aS=0,cS=0;
        int max_score=0;
        for(int y=0;y<N;y++){
            ifile>>ti;
            if(ti/3>=p){
                cS++;
                max_score++;
            }
            else{
                int a,b,c;
                a=p;
                if(ti-p<0) continue;
                if(ti<2) continue;
                if((ti-p)%2==1){
                    b=(ti-p)/2;
                    c=b+1;
                }
                else{
                    b=(ti-p)/2;
                    c=b;
                }
                int dif=f_max(a,b,c)-f_min(a,b,c);
                if(dif>2&&ti>1){cS++;}
                else{
                    if(dif==2&&aS<S){
                        aS++;
                        max_score++;
                    }
                    if(dif==1){
                        cS++;
                        max_score++;
                    }
                }
            }
        }
        ofile<<"Case #"<<i+1<<": "<<max_score<<endl;
    }

    return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<fstream>
using namespace std;





int main(int argc,char *argv[]){
   // init();
    int T,N,S,p,g,n,a,b;
    //int googler[110];
    scanf("%d",&T);
    //getchar();
    ofstream f;
    f.open("D:/out.in");

    for(int i=1;i<=T;i++){

        cin>>N>>S>>p;
        f<<"Case #"<<i<<": ";
        cout<<"Case #"<<i<<": ";
        n=0;
        for(int t=0;t<N;t++){
            scanf("%d",&g);
            a = g/3;
            b = g%3;

            if(b==0){
                if(a>=p)
                    ++n;
                else{
                    if(S>0)
                        if((a!=0)&&(a+1>=p)){
                            ++n;
                            --S;
                        }
                }
            }
            else if(b==1){
                if(a+1>=p)
                    ++n;
            }
            else if(b==2){
                if(a+1>=p)
                    ++n;
                else{
                    if(S>0)
                        if(a+2>=p){
                            ++n;
                            --S;
                        }
                }
            }

        }

        f<<n<<endl;
        cout<<n<<endl;
    }



    f.close();

}

#include <fstream>
#include <math.h>

using namespace std;

int main(){
    ifstream fin;
    ofstream fout;
    int n,i,x,y,xc,yc,total,b;
    char a,pre;
    fin.open("A-large.in");
    fout.open("A-large.out");

    fin>>n;
    for(int j=1;j<=n;j++){
        fin>>i;
        fin>>a;
        fin>>b;
        x=1;y=1;xc=0;yc=0;total=b;

        pre=a;
        if(a=='O'){
            x=b;
            xc=b;
        }else{
            y=b;
            yc=b;
        }

        for(int k=2;k<=i;k++){
            fin>>a;
            fin>>b;
            if(a==pre){
                if(a=='O'){
                    total=total+fabs(x-b)+1;
                    xc=xc+fabs(x-b)+1;
                    x=b;
                }else{
                    total=total+fabs(y-b)+1;
                    yc=yc+fabs(y-b)+1;
                    y=b;
                }
            }else{
                if(a=='O'){
                    pre=a;
                    if(fabs(b-x)<=yc){
                        total++;
                        xc++;
                    }else{
                        total=total+fabs(b-x)+1-yc;
                        xc=fabs(b-x)+1-yc;
                    }
                    yc=0;
                    x=b;
                }else{
                    pre=a;
                    if(fabs(b-y)<=xc){
                        total++;
                        yc++;
                    }else{
                        total=total+fabs(b-y)+1-xc;
                        yc=fabs(b-y)+1-xc;
                    }
                    xc=0;
                    y=b;
                }
            }
        }
        fout<<"Case #"<<j<<": "<<total<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
    

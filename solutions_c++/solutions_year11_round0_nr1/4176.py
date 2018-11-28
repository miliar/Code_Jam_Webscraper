#include<iostream.h>
#include<fstream.h>
int main()
{
    ifstream f1;
    f1.open("input.in");
    ofstream f2;
    f2.open("output.txt");

    int t;
    f1>>t;
    int k=1;
    while(k<=t){

        int n;
        f1>>n;
        int o[100],b[100];
        int cnto=0,cntb=0;
        int ultm[100][2];
        for(int i=0;i<n;i++){
            char c;
            f1>>c;
            if(c=='O'){
                int t;
                f1>>t;
                ultm[i][0]=0;
                ultm[i][1]=t;

                o[cnto]=t;
                cnto++;
            }
     if(c=='B'){
                int t;
                f1>>t;
                ultm[i][0]=1;
                ultm[i][1]=t;

                b[cntb]=t;
                cntb++;
            }}

    int order=0;
    int inso=0,insb=0;
    int poso=1,posb=1;
    int sec=0;
    for(int i=0;i<n;i++){
        if(ultm[order][0]==0){
            if(abs(o[inso]-poso)>=abs(b[insb]-posb))
            {

                sec+=abs(o[inso]-poso)+1;
                 poso=o[inso];

                posb=b[insb];
                order++;     if(inso<cnto-1){ inso++;}
            }
            else {
                sec+=abs(o[inso]-poso)+1;

                if(b[insb]>posb){
                    posb=posb+abs(o[inso]-poso)+1;
                }
                else{
                    posb-=(abs(o[inso]-poso)+1);
                }
                poso=o[inso];

                order++;
                 if(inso<cnto-1){ inso++;}
            }
        }
        else {
            if(abs(b[insb]-posb)>=abs(o[inso]-poso))
            {
                sec+=abs(b[insb]-posb)+1;

                posb=b[insb];

                poso=o[inso];
                order++;    if(insb<cntb-1){ insb++;}
            }
            else {
                sec+=abs(b[insb]-posb)+1;

                if(o[inso]>poso){
                    poso=poso+abs(b[insb]-posb)+1;
                }
                else{
                    poso-=(abs(b[insb]-posb)+1);
                }
                posb=b[insb];

                order++;
                if(insb<cntb-1){ insb++;}
            }
        }
    }

    f2<<"Case #"<<k<<": "<<sec<<"\n";
    k++;
        }
}


#include <iostream>
#include <fstream>
using namespace std;
int T;
int N;
int onum,bnum,mnum;
int olist,blist;
int onow,bnow;
int mtime;
int seq[100];
char sstr[100];
int o[100];
int b[100];
char check;
int main()
{
    ifstream in;
    ofstream out;
    in.open("Bot Trust.in");
    out.open("Bot Trust.out");
    in>>T;
    for(int i=0;i<T;i++){
            onum=0;
            bnum=0;
            mnum=0;
            mtime=0;
            olist=0;
            blist=0;
            onow=1;
            bnow=1;
            in>>N;
            for(int j=0;j<N;j++)
            {
                    
                    in>>check;
                    sstr[mnum]=check;
                    if(check=='B') 
                    {
                                   in>>b[bnum];
                                   seq[mnum]=b[bnum];
                                   bnum++;                   
                    }
                    if (check=='O')
                    {
                        in>>o[onum];
                        seq[mnum]=o[onum];
                        onum++;   
                    }
            mnum++;
            }
    for (int k=0;k<mnum;k++){
        if(sstr[k]=='O'){
            olist++;
            mtime=mtime+abs(seq[k]-onow)+1;
            if(abs(bnow-b[blist])<=abs(seq[k]-onow)+1)
            {
                                           bnow=b[blist];
                                           }
            else{
                 if (bnow<b[blist]){
                 bnow=bnow+abs(seq[k]-onow)+1;
                 }
                 else 
                 bnow=bnow-abs(seq[k]-onow)-1;
                 }
                 onow=seq[k];  
                 //cout<<"onow"<<onow<<"      "<<"bnow"<<bnow<<"     "<<mtime<<endl;          
        }
        else {
            blist++;
            mtime=mtime+abs(seq[k]-bnow)+1;
            if(abs(onow-o[olist])<=abs(seq[k]-bnow)+1)
            {
                                           onow=o[olist];
                                           }
            else{
                 if (onow<o[olist]){
                 onow=onow+abs(seq[k]-bnow)+1;
                 }
                 else
                 onow=onow-abs(seq[k]-bnow)-1;
                 }
                 bnow=seq[k];  
                // cout<<"onow"<<onow<<"      "<<"bnow"<<bnow<<"      "<<mtime<<endl;  
             }
        }
    out<<"Case #"<<i+1<<":"<<" "<<mtime<<endl;
}
    in.close();
    out.close();
    system("Pause");
    
    
}

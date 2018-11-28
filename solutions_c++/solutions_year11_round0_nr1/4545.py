#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
main()
{
    int t,n,p,tt,r,i;
    char ch;
    int a[101],b[101],c[101],d[101];
    
    ifstream in("a.in");
    in>>t;
    ofstream out("a.out");
    int an,bn;
    for(tt=1;tt<=t;tt++) {
        in>>n;
        an=bn=0;
        for(i=0;i<n;i++) {
            in>>ch>>r;
            if(ch=='O') {
                c[an]=i;
                a[an++]=r;                
            } else {
                d[bn]=i;
                b[bn++]=r;
            }            
        }  
        int ai,bi;
        int l1,l2,a1,b1;
        a1=b1=0;
        ai=bi=1;
        int time=0;
        c[an]=d[bn]=n+1;
        while(a1<an || b1<bn) {
            l1=abs(a[a1]-ai);
            l2=abs(b[b1]-bi);
            if(c[a1]<d[b1]) {
                c[a1]=n+1;                
                l1++;
                if(l1>l2) {
                    bi=b[b1];                    
                } else {
                    if(bi>b[b1])bi-=l1;else bi+=l1;
                }   
                time+=l1;
                ai=a[a1];    
                a1++;
            } else {
                l2++;
                d[b1]=n+1;
                if(l2>l1) {
                    ai=a[a1];                    
                } else {
                    if(ai>a[a1])ai-=l2;else ai+=l2;
                }   
                time+=l2;
                bi=b[b1];
                b1++;                
            }    
            
        }      
        out<<"Case #"<<tt<<": "<<time<<endl;
    }    
    system("PAUSE");
}    

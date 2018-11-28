#include<iostream>
#include<cstring>
char s[8000];
int w,e1,l,c1,o1,m1,e2,sp1,t,o2,sp2,c2,o3,d,e3,sp3,j,a,m2;
main(){
    int tz,tt,i,len,MD=10000;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&tz);
    gets(s);
    for(tt=1;tt<=tz;tt++){
        gets(s);
        len = strlen(s);
        w=0;
        e1=0;
        e2=0;
        e3=0;
        l=0;
        c1=0;
        c2=0;
        o1=0;
        o2=0;
        o3=0;
        m1=0;
        m2=0;
        t=0;
        d=0;
        j=0;
        a=0;
        sp1=0;
        sp2=0;
        sp3=0;
        for(i=0;i<len;i++){
            if(s[i]=='w'){
                w++;    w%=MD;
            }
            if(s[i]=='e'){
                e1+=w;  e1%=MD;
                e2+=m1; e2%=MD;
                e3+=d;  e3%=MD;
            }
            if(s[i]=='l'){
                l+=e1;  l%=MD;
            }
            if(s[i]=='c'){
                c1+=l;  c1%=MD;
                c2+=sp2;c2%=MD;
            }
            if(s[i]=='o'){
                o1+=c1; o1%=MD;
                o2+=t;  o2%=MD;
                o3+=c2; o3%=MD;
            }
            if(s[i]=='m'){
                m1+=o1; m1%=MD;
                m2+=a;  m2%=MD;
            }
            if(s[i]=='t'){
                t+=sp1; t%=MD;
            }
            if(s[i]=='d'){
                d+=o3;  d%=MD;
            }
            if(s[i]=='j'){
                j+=sp3; j%=MD;
            }
            if(s[i]=='a'){
                a+=j;   a%=MD;
            }
            if(s[i]==' '){
                sp1+=e2;sp1%=MD;
                sp2+=o2;sp2%=MD;
                sp3+=e3;sp3%=MD;
            }
        }
        printf("Case #%d: ",tt);
        if(m2<1000){printf("0");}
        if(m2<100){printf("0");}
        if(m2<10){printf("0");}
        printf("%d\n",m2);
    }
}

#include<iostream>
double p[1000],x;
double combi(int nn,int rr){
    int ii;
    long long jj=1.0;
    if(nn<rr){return 0;}
    if(nn==rr||rr==0){return 1;}
    for(ii=rr+1;ii<=nn;ii++){
        jj*=ii;
    }
    for(ii=2;ii<=nn-rr;ii++){
        jj/=ii;
    }
    return jj;
}
main(){
    int ti,tt,n,c,i,j;
    scanf("%d",&tt);
    for(ti=1;ti<=tt;ti++){
        scanf("%d",&c);
        scanf("%d",&n);
        p[c]=0;
        for(i=0;i<=c;i++){
            p[i]=0.0;
        }
        for(i=c-1;i>=0;i--){
            //printf("%d\n",i);
            x=0.0;
            for(j=0;j<=n&&i+j<=c;j++){
                //printf("[%d %d] %lf %lf %lf\n",i,j,combi(i,n-j),combi(c-i,j),1.0+p[i+j]);
                x+=combi(i,n-j)*combi(c-i,j)*(1.0+p[i+j]);
                //printf("[%.6lf]\n",x);
            }
            p[i] = x/(combi(c,n)*(1.0-((combi(c-i,0)*combi(i,n))/combi(c,n))));
            //printf("dd<%.6lf>\n",combi(c-i,0));
            //printf("dd<%.6lf>\n",combi(i,n));
            //printf("dd %d %d <%.6lf>\n",c,n,combi(c,n));
            //printf("<%.6lf>\n",p[i]);
        }
        printf("Case #%d: %.6lf\n",ti,p[0]);
    }
}


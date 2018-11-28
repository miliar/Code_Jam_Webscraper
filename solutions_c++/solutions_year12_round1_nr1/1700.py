#include<cstdio>
#include<cstring>
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int Te,T=0;
    scanf("%d",&Te);
    while(Te--)
    {
    T++;printf("Case #%d: ",T);
    int Anum,Bnum;           
    scanf("%d%d",&Anum,&Bnum);
    float pro[Anum];
    float res[Anum+2];
    float tmp[Anum];
    for(int k=0;k<Anum;k++)
    scanf("%f",&pro[k]);
    res[Anum+1]=Bnum+2;
    double t=1;
    for(int i=0;i<Anum;i++)
    {
    t*=pro[i];
    tmp[i]=t;
    }
    res[Anum]=tmp[Anum-1]*(Bnum-Anum+1)+(1-tmp[Anum-1])*(2*Bnum-Anum+2);
    for(int j=0;j<Anum-1;j++)
    {
    res[j]=(Bnum-Anum+1+2*(j+1))*tmp[Anum-j-2]+(1-tmp[Anum-j-2])*(2*Bnum-Anum+2*(j+2));
    }
    res[Anum-1]=Anum+Bnum+1;
    double min=res[0];
    for(int l=1;l<Anum+2;l++)
    {
    if(res[l]<=min)
    min=res[l];                   
    }
    printf("%f\n",min);          
    }    
    return 0;
}

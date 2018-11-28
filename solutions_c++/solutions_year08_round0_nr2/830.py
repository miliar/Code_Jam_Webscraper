#include<stdio.h>
#include<conio.h>
#include<string.h>
void sorta(int *a,int l)
{
int i,flag=0,temp;
flag=1;
while(flag)
{
flag=0;
for(i=0;i<l-1;i++)
{
if(a[i]>a[i+1]){temp=a[i];a[i]=a[i+1];a[i+1]=temp;flag=1;}
}
}
}


int main()
{   
    int bnum,sav,cl,i,j,areq[150],breq[150],aavail[150],bavail[150];
    short int fareq[150],fbreq[150],faavail[150],fbavail[150];
    int cases,turn,na,nb,t1,t2,t3,t4,anum;
    FILE *fp,*tp;
    tp=fopen("output.txt","w");
    fp=fopen("B-large.in","r");
    fscanf(fp,"%d",&cases);
    for(j=0;j<cases;j++){
    fscanf(fp,"%d%d%d",&turn,&na,&nb);
    for(i=0;i<na;i++)
    {
                     fscanf(fp,"%d:%d%d:%d",&t1,&t2,&t3,&t4);
                     areq[i]=t1*60+t2;
                     bavail[i]=t3*60+t4+turn;
    }
    
    for(i=0;i<nb;i++)
    {
                     fscanf(fp,"%d:%d%d:%d",&t1,&t2,&t3,&t4);
                     breq[i]=t1*60+t2;
                     aavail[i]=t3*60+t4+turn;
    }
    
    for(i=0;i<na;i++)
    {
                     printf("areq=%d bavail=%d\n",areq[i],bavail[i]);
    }

    for(i=0;i<nb;i++)
    {
                     printf("breq=%d aavail=%d\n",breq[i],aavail[i]);
    }
    
    
    
    sorta(areq,na);   
    sorta(breq,nb);   
    sorta(aavail,nb);   
    sorta(bavail,na);   
    
    anum=0;
    for(cl=0;cl<na;cl++){fbavail[cl]=1;}
    for(cl=0;cl<nb;cl++){faavail[cl]=1;}
    for(i=0;i<na;i++)
    {
     for(sav=0;sav<nb;sav++)
     {
                            if(aavail[sav]<=areq[i]&&faavail[sav]){faavail[sav]=0;printf("%d satiesfied by %d\n",areq[i],aavail[sav]);break;}
     }
     if(sav==nb)anum++;
     }
     bnum=0;
    for(i=0;i<nb;i++)
    {
     for(sav=0;sav<na;sav++)
     {
                            if(bavail[sav]<=breq[i]&&fbavail[sav]){fbavail[sav]=0;printf("%d satiesfied by %d\n",breq[i],bavail[sav]);break;}
     }
     if(sav==na)bnum++;
     }

         
    
    printf("Case #%d: %d %d\n",j+1,anum,bnum);
    fprintf(tp,"Case #%d: %d %d\n",j+1,anum,bnum);
}

fclose(fp);
fclose(tp);
getch();
}

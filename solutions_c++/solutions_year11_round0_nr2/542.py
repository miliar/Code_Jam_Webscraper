#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    FILE *fin;
    FILE *fout;
    fin=fopen("B-large.in","r");
    fout=fopen("B-large.out","w");
    bool listchange;
    char form[37][3],clear[29][2],list[101];
    int t,c,d,n;
    fscanf(fin,"%d",&t);
    //cin>>t;
    for (int i=1;i<=t;++i)
    {
        fscanf(fin,"%d",&c);
        //cin>>c;
        for (int j=1;j<=c;++j)
            for (int k=0;k<=2;++k)
                fscanf(fin," %c",&form[j][k]);
                //cin>>form[j][k];
                
        fscanf(fin,"%d",&d);
        //cin>>d;
        for (int j=1;j<=d;++j)
            for(int k=0;k<=1;++k)
            fscanf(fin," %c",&clear[j][k]);
            //cin>>clear[j][k];
        
        fscanf(fin,"%d",&n);    
        //cin>>n;
        for (int j=1;j<=n;++j)
        {
            fscanf(fin," %c",&list[j]);
            //cin>>list[j];
            if(j==1)
                continue;
            listchange=1;
            while(listchange==1 && j>=2)
            {
                for (int k=1;k<=c;++k)
                {
                    if(form[k][0]==list[j-1])
                        if(form[k][1]==list[j])
                        {
                            list[j-1]=form[k][2];
                            j=j-1;
                            n=n-1;
                            listchange=1;
                            break;
                        }
                    if(form[k][0]==list[j])
                        if(form[k][1]==list[j-1])
                        {
                            list[j-1]=form[k][2];
                            j=j-1;
                            n=n-1;
                            listchange=1;
                            break;
                        }
                }
                listchange=0;
            }
            for (int k=1;k<=d;++k)
            {
                if(clear[k][0]==list[j])
                    for(int z=1;z<j;++z)
                        if(clear[k][1]==list[z])
                            for(int y=1;y<=j;++y)
                            {
                                list[y]=0;
                                n=n-j;
                                j=0;
                            }
                if(clear[k][1]==list[j])
                    for(int z=1;z<j;++z)
                        if(clear[k][0]==list[z])
                            for(int y=1;y<=j;++y)
                            {
                                list[y]=0;
                                n=n-j;
                                j=0;
                            }
            }
        }
        fprintf(fout,"Case #%d: [",i);
        for (int j=1;j<=n;++j)
        {
            fprintf(fout,"%c",list[j]);
            if(j!=n)
                fprintf(fout,", ");
            //cout<<list[j];
        }
        fprintf(fout,"]\n");
    }
}

#include<iostream>
#include<string>
char a[5000];
int b[20][5001];
int main()
{
    int n,i,t=1;
    FILE *p,*in;
    p=fopen("out.txt","w");
	in=fopen("C-large.in","r");
    fscanf(in,"%d",&n);
    while(n--)
    {
        
        fgets(a,6000,in);
        if(strcmp(a,"\n")==0)
        {
            n++;
            continue;
        }
        memset(b,0,sizeof(b));
        for(i=0;i<=5000;i++) b[0][i]=1;
        for(i=1;a[i-1]!='\0';i++)
        {
            if(a[i-1]=='w') b[1][i]+=b[0][i-1];
            else if(a[i-1]=='e')
            {
                b[2][i]+=b[1][i-1];
                b[7][i]+=b[6][i-1];
                b[15][i]+=b[14][i-1];
            }
            else if(a[i-1]=='l') b[3][i]+=b[2][i-1];
            else if(a[i-1]=='c') 
            {
                b[4][i]+=b[3][i-1];
                b[12][i]+=b[11][i-1];
            }
            else if(a[i-1]=='o') 
            {
                b[5][i]+=b[4][i-1];
                b[10][i]+=b[9][i-1];
                b[13][i]+=b[12][i-1];
            }
            else if(a[i-1]=='m')
            {
                b[6][i]+=b[5][i-1];
                b[19][i]+=b[18][i-1];
            }
            else if(a[i-1]==' ')
            {
                b[8][i]+=b[7][i-1];
                b[11][i]+=b[10][i-1];
                b[16][i]+=b[15][i-1];
            }
            else if(a[i-1]=='t') b[9][i]+=b[8][i-1];
            else if(a[i-1]=='d') b[14][i]+=b[13][i-1];
            else if(a[i-1]=='j') b[17][i]+=b[16][i-1];
            else if(a[i-1]=='a') b[18][i]+=b[17][i-1];
            b[1][i]+=b[1][i-1];
            b[2][i]+=b[2][i-1];
            b[3][i]+=b[3][i-1];
            b[4][i]+=b[4][i-1];
            b[5][i]+=b[5][i-1];
            b[6][i]+=b[6][i-1];
            b[7][i]+=b[7][i-1];
            b[8][i]+=b[8][i-1];
            b[9][i]+=b[9][i-1];
            b[10][i]+=b[10][i-1];
            b[11][i]+=b[11][i-1];
            b[12][i]+=b[12][i-1];
            b[13][i]+=b[13][i-1];
            b[14][i]+=b[14][i-1];
            b[15][i]+=b[15][i-1];
            b[16][i]+=b[16][i-1];
            b[17][i]+=b[17][i-1];
            b[18][i]+=b[18][i-1];
            b[19][i]+=b[19][i-1];
            b[1][i]%=10000;
            b[2][i]%=10000;
            b[3][i]%=10000;
            b[4][i]%=10000;
            b[5][i]%=10000;
            b[6][i]%=10000;
            b[7][i]%=10000;
            b[8][i]%=10000;
            b[9][i]%=10000;
            b[10][i]%=10000;
            b[11][i]%=10000;
            b[12][i]%=10000;
            b[13][i]%=10000;
            b[14][i]%=10000;
            b[15][i]%=10000;
            b[16][i]%=10000;
            b[17][i]%=10000;
            b[18][i]%=10000;
            b[19][i]%=10000;
            
        }
        if(b[19][i-1]>999) fprintf(p,"Case #%d: %d\n",t++,b[19][i-1]);
        else if(b[19][i-1]>99) fprintf(p,"Case #%d: 0%d\n",t++,b[19][i-1]);
        else if(b[19][i-1]>9) fprintf(p,"Case #%d: 00%d\n",t++,b[19][i-1]);
        else if(b[19][i-1]>-1) fprintf(p,"Case #%d: 000%d\n",t++,b[19][i-1]);
        
    }
    fclose(p);
	fclose(in);
    return 0;
}
        
            

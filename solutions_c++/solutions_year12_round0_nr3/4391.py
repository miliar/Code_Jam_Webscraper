#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>

 
                                 
int rot(char s[10],int j)
{
      int i,l,m,k;
      char c[15];
      for(i=j+1,k=0;i<strlen(s);i++,k++)
      {
              c[i]=s[k];
      }
      c[i]='\0';
      for(l=strlen(s)-1-j,m=0;s[l]!='\0';m++,l++)
      {
              c[m]=s[l];
      }
      cout<<"c: "<<c<<"\n";
      int z;
      z=atoi(c);
      return z;
}
              
int main()
{
    FILE *fi,*fo;
    fi=fopen("input.txt","r");
    fo=fopen("output.txt","w");
     int tn,cn=0,temp,cn1=0;
     char s[100],a[15],b[15],*c;
     int x,y,z;
     
    if(fi==NULL)
     {
         cout<<"Unable to open input.txt!!\n";
         getch();
         return 0;
     }
     
    fgets(s,100,fi);   //reading the no of cases
     //strcpy(s,"1");
     tn=atoi(s);
     
     cout<<"no of cases : "<<tn<<"\n";
     //strcpy(a,"100");
     //strcpy(b,"500");
     while(cn1<tn)
     {
        fscanf(fi,"%s %s\n",a,b);
        x=atoi(a);
        y=atoi(b);
        cout<<x<<" "<<y<<"\n";
        cn=0;
        for(int i=x;i<y;i++)
        { 
                itoa(i,a,10);
                cout<<"a : "<<a<<"\n";
                for(int j=0;j<strlen(a)-1;j++)
                {
                        z=rot(a,j);
                        cout<<"z : "<<z<<"\n";
                        if(i==y&&z==y)
                        break;
                        if(z>i&&z<=y)
                        cn++;
                }
                
        }
                        
        printf("Case #%d: %d",cn1+1,cn);                          
        fprintf(fo,"Case #%d: %d\n",cn1+1,cn);
        cn1++;
        
     }
   getch();


}

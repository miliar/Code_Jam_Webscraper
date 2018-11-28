#include<iostream.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>

/*input is read from input.txt and the output can be found in output.txt"*/

char chk(char a)
{
    char g[200]={"qzaejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"};
    char x[200]={"zqyourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"};
    
    for(int i=0;g[i]!='\0';i++)
    {
            if(g[i]==a)
            return(x[i]);
    }
}

int convrt(char s[5])
{
    int len,temp=0;
    len=strlen(s);
    for(int i=len-2,j=0;i>=0;i--,j++)
    {
            temp=temp+(s[i]-48)*pow(10,j);
    }
    return temp;
}  
            
    

int main()
{
     
     
     FILE *fi,*fo;
     int tn,cn=0,temp;
     char s[101];
     fo=fopen("output.txt","w");
     fi=fopen("input.txt","r");
     
     if(fi==NULL)
     {
         cout<<"Unable to open input.txt!!\n";
         getch();
         return 0;
     }
     
     fgets(s,101,fi);   //reading the no of cases
     tn=convrt(s);
     cout<<"no of cases : "<<tn<<"\n";

     while(cn<tn)
     {
        fgets(s,101,fi);
        cout<<s<<" "<<strlen(s);
        
        
        for(int i=0;s[i]!='\0';i++)
        {      
              if(isalpha(s[i]))
               s[i]=chk(s[i]);
        }
        fprintf(fo,"Case #%d: %s",cn+1,s);
        cn++;
     }
  
     cout<<"Output.txt created!!\n";
     getch();
     return 0;
}

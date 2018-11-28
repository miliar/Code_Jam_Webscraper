#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
int recycle(char * s,int i,int l)
{
    //cout<<"Recycle"<<endl;
    char str[2000];
    char str2[2000];
    char * p;
    p=s;
    strncpy(str,p,i);
    str[i]='\0';
   //puts(str);
    strncpy(str2,p+i,l-i);
    str2[l-i]='\0';
    strncat(str2,str,i);
    str2[l]='\0';

    int n = atoi(str2);
    //cout<<"Number"<<n<<endl;
    return n;
}
int main()
{

    FILE *fp=fopen("C-small-attempt2.in.txt", "r"), *ofp=fopen("C-small-attempt2.op.txt", "w");
     int T,A,B,r,i,n,j,no,count,count1;
     char s[2000];


         //  cout<<"In"<<endl;
       fscanf(fp, "%d", &T);



       for(int tc=1;tc<=T;tc++)
       {
    count=n=0;
               fscanf(fp,"%d%d",&A,&B);
               r=B-A+1;
               vector<int> g(r);

               for(i=0;i<r;i++)
               {

                   n=i+A;
                   itoa(n,s,10);
                  // puts(s);
                   int l=strlen(s);
                   count1=0;
                   for(j=1;j<l;j++)
                   {

                       if(s[j]!='0')
                       {
                           //cout<<"Number sent to recycle"<<endl;
                           //puts(s);
                           no=recycle(s,j,l);
                           if(no!=n)
                           {

                           no=no-A;
                           if(no>0)
                           {if(no<r)
                           {

                               if(g[no]==0)
                               {

                                    g[i]=1;
                                   g[no]=1;
                                   count1++;
                               }
                           }
                           }
                           }
                       }
                     //  cout<<"j"<<j<<endl;
                   }
                  count1++;
                  count=count+(count1*(count1-1)/2);


               }



               fprintf(ofp, "Case #%d: %d\n", tc, count);

       }
       return 0;
}

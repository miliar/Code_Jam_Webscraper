# include <stdio.h>
# include <math.h>
# include <iostream>
using namespace std;
int table[20][1000],size[20],ans[20][1000];
int main()
{
int num,i,x,j,cnt=0;
int put[100][4];
cin>>num;
char input[500];
char str[20]="welcome to code jam";
int max=strlen(str);
fflush(stdin);
for(i=0;i<num;i++)
{
fflush(stdin);
    gets(input);
         for(x=0;x<max;x++)
         {
            for(j=0;j<strlen(input);j++)
            {
                    if(input[j]==str[x])
                    {
                    table[x][cnt++]=j; //pos starts with 0
                    size[x]=cnt;
                    }
            }
         cnt=0;
         }

         cnt=0;
        for(int m=0;m<size[0];m++)
        ans[0][m]=1;
    for(int i=1;i<max;i++)
    {
            for(int j=0;j<size[i];j++)
            {
                    while(table[i][j]>table[i-1][cnt]&&cnt<=size[i-1])
                    {
                    ans[i][j]=ans[i][j]+ans[i-1][cnt];
                    cnt++;
                    }
            ans[i][j]%=10000;    //Only last 4 digits
            cnt=0;
            }
    }

int fin=0;
for(int i=0;i<size[max-1];i++)
{
        fin+=ans[max-1][i];
}
int rem=fin/1000;
        fin=fin-rem*1000;
        rem=rem%10;
put[i][0]=rem;
//cout<<rem;
for(int k=2;k<=4;k++)
{
rem=fin/pow(10,4-k);
      put[i][k-1]=rem;
      //  cout<<rem;
fin-=rem*pow(10,4-k);
}
cout<<"\n";
rem=0;
fin=0;
for(int i=0;i<1000;i++)
{
    for(int j=0;j<20;j++)
    {
            table[j][i]=0;
            ans[j][i]=0;
    size[j]=0;
    }

}
}//Storing so as to print all outputs together
for(i=0;i<num;i++)
cout<<"Case #"<<i+1<<": "<<put[i][0]<<put[i][1]<<put[i][2]<<put[i][3]<<"\n";

return 0;
}

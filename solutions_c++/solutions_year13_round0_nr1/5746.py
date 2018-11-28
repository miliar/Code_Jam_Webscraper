#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("C:\\Users\\DELL\\Desktop\\input.txt","r",stdin); 
freopen("C:\\Users\\DELL\\Desktop\\output.txt","w",stdout);

    int i,j,k,t,t1;
    char ch,ch1,ch2,ch3,ch4,ch5,ch6,ch7,a[4][4];
    scanf("%d",&t);
    for(t1=1;t1<=t;t1++)
    {
                        k=0;
              for(i=0;i<4;i++)
              {
              scanf("%s",&a[i]);
              }
              for(i=0;i<4;i++)
              {
              for(j=0;j<4;j++)
              {
              if(a[i][j]=='.')
              {
              k=1;
              break;
              }
              }
              }
              ch='#';
              ch1=a[0][0];
              ch2=a[0][1];
              ch3=a[0][2];
              ch4=a[0][3];
              ch5=a[1][0];
              ch6=a[2][0];
              ch7=a[3][0];
              if(ch1!='.')
              {
              if(ch1!='T')
              {
              if(((a[1][1]==ch1)||(a[1][1]=='T'))&&((a[2][2]==ch1)||(a[2][2]=='T'))&&((a[3][3]==ch1)||(a[3][3]=='T')))
              ch=ch1; 
              else if(((a[0][1]==ch1)||(a[0][1]=='T'))&&((a[0][2]==ch1)||(a[0][2]=='T'))&&((a[0][3]==ch1)||(a[0][3]=='T')))
              ch=ch1;
              else if(((a[1][0]==ch1)||(a[1][0]=='T'))&&((a[2][0]==ch1)||(a[2][0]=='T'))&&((a[3][0]==ch1)||(a[3][0]=='T')))
              ch=ch1;
              }
              else
              {
                  if(a[2][2]==a[1][1]&&a[3][3]==a[1][1])
                  ch=a[1][1];
                  else if(a[0][1]==a[0][2]&&a[0][1]==a[0][3])
                  ch=a[0][1];
                  else if(a[1][0]==a[2][0]&&a[1][0]==a[3][0])
                  ch=a[0][1];
                  }
                  }
                 // printf("%c\n",ch);
                  if(ch2!='.')
                  {
                  if(ch2!='T')
                  {
              if(((a[1][1]==ch2)||(a[1][1]=='T'))&&((a[2][1]==ch2)||(a[2][1]=='T'))&&((a[3][1]==ch2)||(a[3][1]=='T')))
              ch=ch2;
              }
              else 
              {
                   if(a[1][1]==a[2][1]&&a[1][1]==a[3][1])
                   ch=a[1][1];
                   }
                   }
                  // printf("%c\n",ch);
                   if(ch3!='.')
                   {
                   if(ch3!='T')
                   {
              if(((a[1][2]==ch3)||(a[1][2]=='T'))&&((a[2][2]==ch3)||(a[2][2]=='T'))&&((a[3][2]==ch3)||(a[3][2]=='T')))
              ch=ch3;
              }
              else
              {
                   if(a[1][2]==a[2][2]&&a[1][2]==a[3][2])
                   ch=a[1][2];
                   }
                   }
                  // printf("%c\n",ch);
                   if(ch5!='.')
                   {
              if(ch5!='T')
              {     
              if(((a[1][1]==ch5)||(a[1][1]=='T'))&&((a[1][2]==ch5)||(a[1][2]=='T'))&&((a[1][3]==ch5)||(a[1][3]=='T')))
              ch=ch5;
              }
              else
              {
                  if(a[1][1]==a[1][2]&&a[1][1]==a[1][3])
                  ch=a[1][1];
                  }
                  }
                //  printf("%c\n",ch);
                  if(ch6!='.')
                  {
                  if(ch6!='T')
                  {
              if(((a[2][1]==ch6)||(a[2][1]=='T'))&&((a[2][2]==ch6)||(a[2][2]=='T'))&&((a[2][3]==ch6)||(a[2][3]=='T')))
              ch=ch6;
              }
              else
              {
                  if(a[2][1]==a[2][2]&&a[2][2]==a[2][3])
                  ch=a[2][1];
                  }
                  }
                 // printf("%c\n",ch);
                  if(ch7!='.')
                  {
                  if(ch7!='T')
                  {
              if(((a[3][1]==ch7)||(a[3][1]=='T'))&&((a[3][2]==ch7)||(a[3][2]=='T'))&&((a[3][3]==ch7)||(a[3][3]=='T')))
              ch=ch7;
              }
              else
              {
                  
                  if(a[3][1]==a[3][2]&&a[3][2]==a[3][3])
                  ch=a[3][1];
                  }
                  }
                // printf("%c\n",ch);
              if(ch4!='.')
              {    
              if(ch4!='T')
              {
               if((a[0][0]==ch4||a[0][0]=='T')&&(a[0][1]==ch4||a[0][1]=='T')&&(a[0][2]==ch4||a[0][2]=='T'))
              ch=ch4;
              else if(((a[1][3]==ch4)||(a[1][3]=='T'))&&((a[2][3]==ch4)||(a[2][3]=='T'))&&((a[3][3]==ch4)||(a[3][3]=='T')))
              ch=ch4;
              else if(((a[1][2]==ch4)||(a[1][2]=='T'))&&((a[2][1]==ch4)||(a[2][1]=='T'))&&((a[3][0]==ch4)||(a[3][0]=='T')))
              ch=ch4;
              }
              else
              {
                  if(a[0][0]==a[0][1]&&a[0][0]==a[0][2])
                  ch=a[0][0];
                  else if(a[3][0]==a[2][1]&&a[3][0]==a[1][2])
                  ch=a[1][2];
                  else if(a[1][3]==a[2][3]&&a[1][3]==a[3][3])
                  ch=a[1][3];
                  }
                  }
                 // printf("%c\n",ch);
              if(ch=='X'||ch=='O')
              printf("Case #%d: %c won\n",t1,ch);
              else if(ch!='X'&&ch!='O'&&k==1)
              {
              printf("Case #%d: Game has not completed\n",t1);
              }
              else if(ch!='X'&&ch!='O'&&k==0) 
              printf("Case #%d: Draw\n",t1);
              }
              return 0;
              }
              
              
              
              
              

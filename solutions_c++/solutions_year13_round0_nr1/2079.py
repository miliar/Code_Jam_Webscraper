#include<iostream>
#include<fstream.h>
using namespace std;
int main()
{
    int t,i,j,k=0,l=-1,m=-1,z=1,flag=0,x1,o1,x2,o2;
    ifstream f1;
    ofstream f2;
    f1.open("786.txt");
    f2.open("won.txt");
     char a[4][4];
    f1>>t;
    while(t--)
    {
    flag=0;
    k=0,l=-1,m=-1;
    for(i=0;i<4;++i)
    {
     for(j=0;j<4;++j)
     {
    f1>>a[i][j];
}
}
    for(i=0;i<4;++i)
    {
     for(j=0;j<4;++j)
     {
      if(a[i][j]=='T')
      {
       l=i;m=j;
       }
       if(a[i][j]!='.')
       k++;
       }
       }
       for(i=0;i<4;++i)
       {
         if(a[i][0]==a[i][1]&&a[i][0]==a[i][2]&&a[i][0]==a[i][3]&&a[i][0]!='.')
         {
           f2<<"Case #"<<z<<": "<<a[i][0]<<" won"<<endl;
           flag=1;
           break;
           }
           if(a[0][i]==a[1][i]&&a[0][i]==a[2][i]&&a[2][i]==a[3][i]&&a[0][i]!='.')
         {
           f2<<"Case #"<<z<<": "<<a[0][i]<<" won"<<endl;
           flag=1;
           break;
           }
           }
           
           if(flag==0)
           {
           if(a[0][0]==a[1][1]&&a[0][0]==a[2][2]&&a[0][0]==a[3][3]&&a[0][0]!='.')
           {
            f2<<"Case #"<<z<<": "<<a[0][0]<<" won"<<endl;
            flag=1;
            }
             if(a[0][3]==a[1][2]&&a[0][3]==a[2][1]&&a[0][3]==a[3][0]&&a[3][0]!='.')
           {
            f2<<"Case #"<<z<<": "<<a[0][3]<<" won"<<endl;
            flag=1;
            }
            }
            x1=0,o1=0,x2=0,o2=0;
             if(flag==0&&l!=-1&&m!=-1)
            {
              for(i=0;i<4;++i)
              {
                if(m!=i)
                {
                if(a[l][i]=='X')
                x1++;
                else if(a[l][i]=='O')
                o1++;
                }
                if(l!=i)
                {
                if(a[i][m]=='X')
                x2++;
                else if(a[i][m]=='O')
                o2++;
                }
                }
                if(x1==3||x2==3)
                {
                 f2<<"Case #"<<z<<": "<<"X won"<<endl;
            flag=1;
            }
            if(o1==3||o2==3)
                {
                 f2<<"Case #"<<z<<": "<<"O won"<<endl;
            flag=1;
            }
            }
            
            
            
            if(flag==0)
            {
               if(l==0&&m==0||l==1&&m==1||l==2&&m==2||l==3&&m==3)
               {
                 x1=0,o1=0;
                 for(i=0;i<4;++i)
                 {
                  if(a[i][i]=='X')
                  x1++;
                  else if(a[i][i]=='O')
                  o1++;
                  }
                  if(x1==3)
                  {
                   f2<<"Case #"<<z<<": "<<"X won"<<endl;
            flag=1;
            }
            if(o1==3)
                {
                 f2<<"Case #"<<z<<": "<<"O won"<<endl;
            flag=1;
            }
            }
            if(l==0&&m==3||l==1&&m==2||l==2&&m==1||l==3&&m==0)
             {
                 x1=0,o1=0,j=3;
                 for(i=0;i<4;++i)
                 {
                  if(a[i][j]=='X')
                  x1++;
                  else if(a[i][j]=='O')
                  o1++;
                  j--;
                  }
                  if(x1==3)
                  {
                   f2<<"Case #"<<z<<": "<<"X won"<<endl;
            flag=1;
            }
            if(o1==3)
                {
                 f2<<"Case #"<<z<<": "<<"O won"<<endl;
                flag=1;
            }
            }
            }
            
            
            if(flag==0)
            {
              if(k==16)
              f2<<"Case #"<<z<<": "<<"Draw"<<endl;
              else
              f2<<"Case #"<<z<<": "<<"Game has not completed"<<endl;
              }
              z++;
              }
              f1.close();
              f2.close();
              return 0;
              }
                 
                
           
            

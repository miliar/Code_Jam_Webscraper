#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
       int t;
       freopen("input.in","r",stdin);
       freopen("output.in","w",stdout);
       //string owin[5],xwin[5];
       string owin[5]={"OOOO","OOOT","OOTO","OTOO","TOOO"};
       string xwin[5]={"XXXX","XXXT","XXTX","XTXX","TXXX"};
       char inp[4][4];
       cin>>t;
       string inpstr[10],str1,str2;
       int f_xwin,f_owin,f_dot,m,i,j,k;       
       for(i=1;i<=t;i++)
       {
              
              f_xwin=0,f_owin=0,f_dot=0,m=0;
              for(j=0;j<4;j++)
              {
                     for(k=0;k<4;k++)
                     {
                            cin>>inp[j][k];
                            if(inp[j][k]=='.')
                            f_dot=1;
                     }
              }
              cout<<"Case #"<<i<<": ";
              string str3,str4;
              for(j=0;j<4;j++)
              {
                     string str1;
                     string str2;
                     for(k=0;k<4;k++)
                     {
                            str1=str1+inp[j][k];
                            str2=str2+inp[k][j];
                            if(j==k)
                            str3+=inp[j][k];
                            if((j+k)==3)
                            str4+=inp[j][k];
                     }
                    // cout<<str1<<" "<<str2<<endl;
                     inpstr[m++]=str1;
                     inpstr[m++]=str2;
              }
              /*str1="",str2="";
              str1+=inp[0][0]+inp[1][1]+inp[2][2]+inp[3][3];
              inpstr[8]=str1;
              str2+=inp[0][3]+inp[1][2]+inp[2][1]+inp[3][0];
              inpstr[9]=str2;
              */
              inpstr[8]=str3;
              inpstr[9]=str4;
              //cout<<inpstr[8]<<" "<<inpstr[9]<<endl<<endl;
              for(j=0;j<5;j++)
              {
                     for(k=0;k<10;k++)
                     {
                            if(inpstr[k]==owin[j])
                            {
                                   cout<<"O won"<<endl;
                                   f_owin=1;
                                   break;
                            }
                            if(inpstr[k]==xwin[j])
                            {
                                   cout<<"X won"<<endl;
                                   f_xwin=1;
                                   break;
                            }
                     }
                     if(f_xwin==1 || f_owin==1)
                     break;
              }
              if(f_xwin==1 || f_owin==1)
              continue;
              else if(f_dot==0)
              cout<<"Draw"<<endl;
              else
              cout<<"Game has not completed"<<endl;
              //cout<<endl<<endl;;
       }
       return 0;
}

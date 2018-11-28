#include<iostream>
using namespace std;
bool checkcol(int a[100][100],int h,int w,int i,int j,int &i1,int &j1){
                        int min=10001,mini,minj;
                        if(i>0&&a[i-1][j]<min)
                        {
                            min=a[i-1][j];
                            mini=i-1;
                            minj=j;
                        }
                        if(j>0&&a[i][j-1]<min)
                        {
                            min=a[i][j-1];
                            mini=i;
                            minj=j-1;
                        }
                        if(j<w-1&&a[i][j+1]<min)
                        {
                            min=a[i][j+1];
                            mini=i;
                            minj=j+1;
                        }

                        if(i<h-1&&a[i+1][j]<min)
                        {
                            min=a[i+1][j];
                            mini=i+1;
                            minj=j;
                        }

i1=mini;
j1=minj;
return (a[i][j]>a[i1][j1]);
}
int main()
{
    int t,tno=1,w,h,a[100][100],fl[100][100],stx[10000],sty[10000],stp;
    int i,j,min,mini,minj,l,d,n,num=0;
    char c;
    char ca[100][100];
    cin>>t;
    while(tno<=t){
        cin>>h>>w;
        for(i=0;i<h;i++)
            for(j=0;j<w;j++){
            cin>>a[i][j];
            ca[i][j]=' ';
            fl[i][j]=0;
            }
            

       // ca[0][0]='a';
        for(c='a';c<='z';c++){
            stp=0;
            for(i=0;i<h*w;i++)
               if(ca[i/w][i%w]==' ')
               {
                    ca[i/w][i%w]=c;
                    stx[stp]=i/w;
                    sty[stp++]=i%w;
                    fl[i/w][i%w]=1;
                    break;
                    }

            if(stp==0)break;
            
            while(stp){
                i=stx[--stp];
                j=sty[stp];
                int flag=1;
                mini=minj=-1;
                if(checkcol(a,h,w,i,j,mini,minj)&&fl[mini][minj]==0){
                    fl[mini][minj]=1;
                    ca[mini][minj]=c;
                    stx[stp]=mini;
                    sty[stp++]=minj;
                }
                if(i>0&&fl[i-1][j]==0&&checkcol(a,h,w,i-1,j,mini,minj)&&i==mini&&j==minj){
                    fl[i-1][j]=1;
                    ca[i-1][j]=c;
                    stx[stp]=i-1;
                    sty[stp++]=j;
                }
                if(j>0&&fl[i][j-1]==0&&checkcol(a,h,w,i,j-1,mini,minj)&&i==mini&&j==minj){
                    fl[i][j-1]=1;
                    ca[i][j-1]=c;
                    stx[stp]=i;
                    sty[stp++]=j-1;
                }
                if(j<w-1&&fl[i][j+1]==0&&checkcol(a,h,w,i,j+1,mini,minj)&&i==mini&&j==minj){
                    fl[i][j+1]=1;
                    ca[i][j+1]=c;
                    stx[stp]=i;
                    sty[stp++]=j+1;
                }
                if(i<h-1&&fl[i+1][j]==0&&checkcol(a,h,w,i+1,j,mini,minj)&&i==mini&&j==minj){
                    fl[i+1][j]=1;
                    ca[i+1][j]=c;
                    stx[stp]=i+1;
                    sty[stp++]=j;
                }
                
                }//while
            }//color
            cout<<"Case #"<<tno<<": \n";
            for(i=0;i<h;i++){
                for(j=0;j<w;j++)
                cout<<ca[i][j]<<" ";
                cout<<endl;
                }
            tno++;

           }
        return 0;
    }

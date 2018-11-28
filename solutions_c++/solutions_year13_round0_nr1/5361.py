#include<iostream>
#include<cstdio>
using namespace std;

char a[4][4];

int check(char ch)
{
    if(ch=='X') return 1;
    else if(ch=='O') return 0;
    else if(ch=='.') return 999;
}

int checkheng(int n,int m)
{
    if(check(a[n][m])+check(a[n][m+1])+check(a[n][m+2])+check(a[n][m+3])==0)
       return 0;
    else if(check(a[n][m])+check(a[n][m+1])+check(a[n][m+2])+check(a[n][m+3])==4)
      return 1;
    else return -1;

}

int checkshu(int n,int m)
{
    if((check(a[n][m])+check(a[n+1][m])+check(a[n+2][m])+check(a[n+3][m]))==0)
       return 0;
    else if((check(a[n][m])+check(a[n+1][m])+check(a[n+2][m])+check(a[n+3][m]))==4)
      return 1;
    else return -1;
}

int checkxie(int n,int m)
{
    if(n>m){
    if((check(a[n][m])+check(a[n-1][m+1])+check(a[n-2][m+2])+check(a[n-3][m+3]))==0)
         return 0;
    else if((check(a[n][m])+check(a[n-1][m+1])+check(a[n-2][m+2])+check(a[n-3][m+3]))==4)
         return 1;
    }
    else{
    if((check(a[n][m])+check(a[n+1][m+1])+check(a[n+2][m+2])+check(a[n+3][m+3]))==0)
       return 0;
    else if((check(a[n][m])+check(a[n+1][m+1])+check(a[n+2][m+2])+check(a[n+3][m+3]))==4)
      return 1;
    }
    return -1;
}

void print(int n)
{
    if(n==1)
      cout<<"X won"<<endl;
    else if(n==0)
      cout<<"O won"<<endl;
    else return ;
}

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("input.txt","w",stdout);
    int t,k,i,j;
    int ansi,num,ansj,heng,shu,ak,xie,dot,ti,tj;
    cin>>t;
    for(int ncase=1;ncase<=t;ncase++){
        ansi=-1,ansj=-1,ti=-1,tj=-1;
        dot=0,heng=0,shu=0,xie=0;

        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>a[i][j];
                if(a[i][j]=='.') dot=1;
                else if(a[i][j]=='T') {ti=i;tj=j;}
            }
        }


        for(k=0;k<2;k++){
        if(k==0&&ti!=-1)
            a[ti][tj]='X';
        else if(k==1&&ti!=-1)
            a[ti][tj]='O';
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){

                if(i==0&&j==0){
                   if(checkheng(i,j)!=-1){
                       heng++;
                       ansi=i;
                       ansj=j;
                       ak=k;
                       goto loop;
                   }
                   else if(checkshu(i,j)!=-1){
                       shu++;
                       ansi=i;
                       ansj=j;
                       ak=k;
                       goto loop;
                   }
                   else if(checkxie(i,j)!=-1){
                       xie++;
                       ansi=i;
                       ansj=j;
                       ak=k;
                       goto loop;
                   }
                }
                else if(i!=0&&j==0){
                    if(checkheng(i,j)!=-1){
                        heng++;
                        ansi=i;
                        ansj=j;
                        ak=k;
                        goto loop;
                    }
                    if(checkxie(i,j)!=-1){
                        xie++;
                        ansi=i;
                        ansj=j;
                        ak=k;
                        goto loop;
                    }
                }
                else if(i==0&&j!=0){
                    if(checkshu(i,j)!=-1){
                        shu++;
                        ansi=i;
                        ansj=j;
                        ak=k;
                        goto loop;
                    }
                }
                else
                     continue;
                }

            }
        }
        if(ak==0&&ti!=-1) a[ti][tj]='X';
        else if(ak==1&&ti!=-1) a[ti][tj]='O';
    //    cout<<dot<<" "<<heng<<" "<<shu<<" "<<xie<<endl;
     /*   cout<<ansi<<" "<<ansj<<endl; */
       loop:
          cout<<"Case #"<<ncase<<": ";
        if(dot==1&&heng==0&&shu==0&&xie==0){

           cout<<"Game has not completed"<<endl;
        }
        else if(dot==0&&heng==0&&shu==0&&xie==0){
              cout<<"Draw"<<endl;
        }

       else if(heng==1)
        print(checkheng(ansi,ansj));
       else if(shu==1)
        print(checkshu(ansi,ansj));
        else if(xie==1);
        print(checkxie(ansi,ansj));

        }
    return 0;
}

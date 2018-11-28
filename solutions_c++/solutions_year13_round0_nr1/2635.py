#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<map>
using namespace std;

int game[4][4];

int main()
{
    freopen("C:\\Users\\vivek\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\vivek\\Desktop\\out.txt","w",stdout);
    int T,t,i,cntx=0,cnto=0,dots=0;
    string check1,check2,check3,check4,check5="",check6="",check7="",check8="",check9="",check10="";
    
    cin>>T;
    for(t=1;t<=T;t++)
    {
       cin>>check1>>check2>>check3>>check4;
       for(i=0;i<4;i++) if(check1[i]=='.') dots=1; for(i=0;i<4;i++) if(check2[i]=='.') dots=1;
       for(i=0;i<4;i++) if(check3[i]=='.') dots=1; for(i=0;i<4;i++) if(check4[i]=='.') dots=1;
       
       check5= check5 + check1[0] + check2[0] + check3[0] + check4[0];
       check6= check6 + check1[1] + check2[1] + check3[1] + check4[1];
       check7= check7 + check1[2] + check2[2] + check3[2] + check4[2];
       check8= check8 + check1[3] + check2[3] + check3[3] + check4[3];
       check9= check9 + check1[0] + check2[1] + check3[2] + check4[3];
       check10= check10 + check1[3] + check2[2] + check3[1] + check4[0];
       if(check1=="XXXX" || check1=="XXXT" || check1=="XXTX" || check1=="XTXX" || check1=="TXXX") cntx=1;
       if(check2=="XXXX" || check2=="XXXT" || check2=="XXTX" || check2=="XTXX" || check2=="TXXX") cntx=1;
       if(check3=="XXXX" || check3=="XXXT" || check3=="XXTX" || check3=="XTXX" || check3=="TXXX") cntx=1;
       if(check4=="XXXX" || check4=="XXXT" || check4=="XXTX" || check4=="XTXX" || check4=="TXXX") cntx=1;
       if(check5=="XXXX" || check5=="XXXT" || check5=="XXTX" || check5=="XTXX" || check5=="TXXX") cntx=1;
       if(check6=="XXXX" || check6=="XXXT" || check6=="XXTX" || check6=="XTXX" || check6=="TXXX") cntx=1;
       if(check7=="XXXX" || check7=="XXXT" || check7=="XXTX" || check7=="XTXX" || check7=="TXXX") cntx=1;
       if(check8=="XXXX" || check8=="XXXT" || check8=="XXTX" || check8=="XTXX" || check8=="TXXX") cntx=1;
       if(check9=="XXXX" || check9=="XXXT" || check9=="XXTX" || check9=="XTXX" || check9=="TXXX") cntx=1;
       if(check10=="XXXX" || check10=="XXXT" || check10=="XXTX" || check10=="XTXX" || check10=="TXXX") cntx=1;
       
       if(check1=="OOOO" || check1=="OOOT" || check1=="OOTO" || check1=="OTOO" || check1=="TOOO") cnto=1;
       if(check2=="OOOO" || check2=="OOOT" || check2=="OOTO" || check2=="OTOO" || check2=="TOOO") cnto=1;
       if(check3=="OOOO" || check3=="OOOT" || check3=="OOTO" || check3=="OTOO" || check3=="TOOO") cnto=1;
       if(check4=="OOOO" || check4=="OOOT" || check4=="OOTO" || check4=="OTOO" || check4=="TOOO") cnto=1;
       if(check5=="OOOO" || check5=="OOOT" || check5=="OOTO" || check5=="OTOO" || check5=="TOOO") cnto=1;
       if(check6=="OOOO" || check6=="OOOT" || check6=="OOTO" || check6=="OTOO" || check6=="TOOO") cnto=1;
       if(check7=="OOOO" || check7=="OOOT" || check7=="OOTO" || check7=="OTOO" || check7=="TOOO") cnto=1;
       if(check8=="OOOO" || check8=="OOOT" || check8=="OOTO" || check8=="OTOO" || check8=="TOOO") cnto=1;
       if(check9=="OOOO" || check9=="OOOT" || check9=="OOTO" || check9=="OTOO" || check9=="TOOO") cnto=1;
       if(check10=="OOOO" || check10=="OOOT" || check10=="OOTO" || check10=="OTOO" || check10=="TOOO") cnto=1;
       
       cout<<"Case #"<<t<<": ";
       if(cntx==1) cout<<"X won"<<endl;
       else if(cnto==1) cout<<"O won"<<endl;
       else if(dots==0) cout<<"Draw"<<endl;
       else cout<<"Game has not completed"<<endl;
       dots=0; cntx=0; cnto=0;
       check5="";check6="";check7="";check8="";check9="";check10="";
    }
    return 0;
}
                 

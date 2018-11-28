#include<stdio.h>
#include<conio.h>
#include<iostream.h>


int min(int a , int b)
{
 if(a<=b) return a;
 if(b<a) return b;
}


int max(int a , int b)
{
 if(a<=b) return b;
 if(b<a) return a;
}

void main()

{
int t,i=0,a,b;
int num[1000];
int tem,rev,di,rm,result=0;
int d1,d2,d3,num2,num3;
cin>>t;


while(t--)
{
for(int k=0;k<1000;k++) num[k]=0;

cin>>a>>b;
//cout<<"a b : "<<a<<" "<<b<<endl;
result=0;

if(b<10) cout<<"Case #"<<++i<<": 0"<<endl;

if(b<100&&b>10)
{     //  cout<<"in b 100\n" ;
	tem=a;
   while(tem<b)
   {
    rm=tem%10;
    di=tem/10;
    rev=rm*10+di;
  //  cout<<"num : rev ="<<tem<<" "<<rev<<endl;
    if(tem<rev)
    {  // cout<<tem<<"<"<<rev<<endl;
    if(rev<=b){ /*cout<<rev<<"<b---------------"<<endl; */num[tem]=1; }
    }
    tem++;
   }
   for(int j=a;j<=b;j++){ if(num[j]==1){ /*cout<<"*******"<<endl; */++result; }}
   cout<<"Case #"<<++i<<": "<<result<<endl; continue;

}

if(b<=1000&&b>100)
{

tem=a;
while(tem<b)
{
d1=tem/100;
d2=(tem%100)/10;
d3=(tem%100)%10;
num2=d2*100+d3*10+d1;
num3=d3*100+d1*10+d2;

//cout<<" tem num2 num 3 : "<<tem<<" "<<num2<<" "<<num3<<endl;

int mn=min(tem,min(num2,num3));
int mx=max(tem,max(num2,num3));
int men=tem+num2+num3-mn-mx;


if(mn>=a&&mx<=b){ num[mn]=3;} //cout<<"**3";}
if(mn>=a&&men<=b&&mx>b){num[mn]=1; }// cout<<"**1";}
if(mn<a&&men>=a&&men<=b&&mx<=b ){num[men]=1;} //cout<<"men**1";}
if(mn==mx){ num[mn]=0;}//cout<<"%%%";}


/*if(mn>=a&&mx<=b){ num[mn]=3; cout<<"*****3";}
if(mn>=a&&mx>b){ num[mn]=1; cout<<"*****1";}
if(mn<a&&mx<=b){ num[mx]=1; cout<<"****1";}
if(mn==mx) num[mn]=0;
 */

// cout<<"tem :"<<tem<<" num2="<<num2<<" num3="<<num3<<" mn="<<mn<<" mx="<<mx<<endl;


 tem++;
}

 for(int j=a;j<=b;j++){ if(num[j]>0){ /*cout<<"*******"<<endl; */result=result+num[j]; }}
  cout<<"Case #"<<++i<<": "<<result<<endl; continue;

}



}




}


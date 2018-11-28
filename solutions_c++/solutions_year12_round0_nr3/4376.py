#include<iostream>
#include<fstream>
#include<conio.h>
#include<string>
#include<map>
using namespace std;

int reverse(int num)
{
    int revNum=0;
    while(num!=0)
    {
           revNum*=10;
           revNum+=num%10;
           num/=10;
    }
    return revNum;
}
int findMsd(int b)
{
    return reverse(b)%10;
}
int main()
{   
    ifstream f;
    ofstream fop;
    fop.open("out.txt",ios::out);
    f.open("C-small-attempt2.in",ios::in);
    int t;
f>>t;
//cout<<reverse(t);
    for(int i=0;i<t;i++)
    {
            int a,b,num=0,bMsd;
            f>>a>>b;
            bMsd=findMsd(b);
            if(b<10) num=0;
            else if(a<10 && b>10) //1 digit numbers will be included
            {
                 num+= bMsd-a+1;
            }
            if(a<100) //2 digit numbers have to be included
            {
                 int lim=(b<100)?b:89;
                 int limSmall=(a>11)?a:12;
                 //fop<<lim<<" "<<limSmall;
                           for(int z=limSmall;z<=lim;z++)
                           {
                                   int rev=reverse(z);
                                   int num1=((z%10)*100 + (rev%10));
                                   if(rev>z && rev<b){
                                            //fop<<z<<" ";
                                            num++;}
                                   if(z*10 < b){
                                           //fop<<z<<" ";
                                           num++;} //017 --- 170
                                   if(num1 <b && num1>z)
                                   {
                                           //fop<<z<<" ";
                                           num++;} // 017--- 701
                                   //fop<<"*"<<z<<"&";
                                   //fop<<endl;
                           }
            }//getch();
            if(b>99) //3 digit numbers will be included
            {
                 int lim=(b<1000)?b:989;
                 int limSmall=(a>101)?a:101;
                  for(int z=limSmall;z<=lim;z++)
                           {
                                   int num1=((z%10)*100+ z/10);
                                   int num2=(z%100)*10 + findMsd(z);
                                   if(num1>z && num1<=b){//fop<<z<<" "<<num1<<"&";
                                   num++;} //abc---cab
                                   if(num2>z && num2<=b){
                                            // fop<<z<<" "<<num2<<"*";
                                             num++;} //abc---bca
                           }    
            }
            if(a==1 && b==1000){//fop<<"0001 ";
            num++;}
            
            fop<<"Case #"<<i+1<<": "<<num<<endl;
    }
    //getch();
    fop.close();
    f.close();
    return 0;
}

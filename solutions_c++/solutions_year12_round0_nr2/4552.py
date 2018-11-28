#include<cstdio>
#include<iostream>
#include<string>
#include<fstream>
using namespace std;
//string s;
char ch[110];
int t,a;

int n,s,p;
int u;
//int v[1000];
//int ans[1000];
int main()
{
   fstream x,y;
 x.open("ud.txt");
 y.open("ans.txt");
 //cin>>t;
 x>>t;
 a=t;
 while(t--)
 {
     int count =0;
     //scanf("%d %d %d",&n,&s,&p);
   x>>n>>s>>p;
     for(int z=0;z<n;z++)
     {
       //  scanf("%d",&u);
         x>>u;
  //       v[z]=u;
         if(u>(3*(p-1)))
         { //cout<<"ud";
             count++;
         }
         else if(s>0)
         {if((u+2)>(3*(p-1)) )
             {//cout<<"2";
             if(u>0&&(p-1)>0)
                 {count++;
                 s--;}
             }
         }

         }
        // cout<<endl;

     y<<"Case #"<<a-t<<": "<<count<<"\n";



 }

    return 0;
}

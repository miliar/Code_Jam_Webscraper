#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<cctype>
#include<cmath>
using namespace std;
int main()
{
    int t,t1,n,i,ans,count,pos1,pos2,temp,s1;
    char ch,ch1;
    //scanf("%d",&t);
    cin>>t;
    t1 = 1;
    while(t1<=t){
            //scanf("%d",&n);
            cin>>n;
            ch ='O';
            pos1 = 1;
            pos2 = 1;
            ans = 0;
            count = 0;
            for(i=0;i<n;i++){
                             //scanf("%1s%d",&ch1,&s1);
                             cin>>ch1>>s1;
                             if(ch1==ch){
                                         if(ch1=='O'){
                                                      temp = abs(s1 - pos1) + 1;
                                                      count = count-temp;
                                                      ans = ans+temp;
             //                                         printf("%d\n",ans);
                                                      pos1 = s1;
                                         }
                                         else
                                         {
                                                      temp = abs(s1-pos2)+1;
                                                      count = count-temp;
                                                      ans = ans+temp;
           //                                           printf("%d\n",ans);
                                                      pos2 = s1;
                                         }
                             }
                             else
                             {
                                         if(ch1=='B'){
                                                      temp = abs(s1-pos2);
                                                      if(abs(count)>temp)
                                                                         temp = 0;
                                                      else
                                                                         temp = temp+count;
                                                      temp = temp+1;
                                                      count = 0;
                                                      count = count-temp;
                                                      ans = ans+temp;
               // /                                      printf("%d\n",ans);
                                                      pos2 = s1;
                                                      ch = 'B';
                                         }
                                         else
                                         {            
                                                      temp = abs(s1-pos1);
                                                      if(abs(count)>temp)
                                                                         temp = 0;
                                                      else
                                                                         temp = temp+count;
                                                      temp = temp+1;
                                                      count = 0;
                                                      count = count-temp;
                                                      ans = ans+temp;
                 //                                     printf("%d\n",ans);
                                                      pos1 = s1;
                                                      ch = 'O';
                                         }
                             }
            }
            //printf("%d\n",ans);
            cout<<"Case #"<<t1<<": "<<ans<<endl;
            t1++;
    }
}   

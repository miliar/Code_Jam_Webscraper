#include<iostream>
#include<math.h>
using namespace std;
int main()
{
 int t;
 int ct=1;
 cin>>t;
 int arr[1001][2];
 int slope[1001];
 int total[16];
 int ub=0;
freopen ("myfile.txt","w",stdout);
 while(ct<=t)
 {
             int n;
             cin>>n;
             for(int i=0;i<n;i++)
             {
                     int a,b;
                 cin>>a>>b;   
                 arr[i][0]=a;
                 arr[i][1]=b; 
                 slope[i]=b-a;
             }

             //cout<<n;
              int count=0;
             for(int j=0;j<n;j++)
             {
                     for(int k=j+1;k<n;k++)
                     {
                      /*   if(slope[j]!=slope[k] && min(arr[j][0],arr[j][1])<max(arr[k][0],arr[k][1]))
                                               count++;    */
                           /*if(slope[j]!=slope[k] && max(arr[j][0],arr[j][1])<max(arr[k][0],arr[k][1]))*/
                           if(slope[j]==slope[k])
                                                 break;
                           else
                           {
                               if(slope[j]>0)
                               {
                                             if(slope[k]>0)
                                             {
                                                           if((arr[k][1]>arr[j][1] && arr[k][0]<arr[j][0]) || (arr[k][1]<arr[j][1] && arr[k][0]>arr[j][0]))
                                                                    count++;
                                                         /*  else
                                                               ;*/
                                             }
                                             else
                                             {
                                                 if((arr[k][0]>arr[j][0] && arr[k][1]<arr[j][1]) || (arr[k][0]<arr[j][0] && arr[k][1]>arr[j][1]))
                                                                        count++;
                                             }  
                               }
                               else
                               {
                                   if(slope[k]>0)
                                             {
                                                          if((arr[k][1]>arr[j][1] && arr[k][0]<arr[j][0]) || (arr[k][1]<arr[j][1] && arr[k][0]>arr[j][0]))
                                                                    count++;
                                                         /*  else
                                                               ;*/
                                             }
                                             else
                                             {
                                                 if((arr[k][0]>arr[j][0] && arr[k][1]<arr[j][1]) || (arr[k][0]<arr[j][0] && arr[k][1]>arr[j][1]))
                                                                        count++;
                                             }  
                               }                    
                           }
                     }
             }
             total[ub]=count;
             ub++;
 
 ct++;
 }
 
 for(int p=0;p<ub;p++)
         cout<<"Case #"<<p+1<<": "<<total[p]<<endl;
 
    return 1;
}

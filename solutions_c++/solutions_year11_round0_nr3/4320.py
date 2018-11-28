#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
    int t;
    int case_no=0;
    cin>>t;
    while(t--){
               int i,n;
               case_no++;
               cin>>n;
               int arr[n];
               for(i=0;i<n;i++)
               cin>>arr[i];
               
               for(int x=0;x<n;x++)
               for(int y=x+1;y<n;y++)
               if(arr[y]<arr[x]){
                                 int temp;
                                 temp=arr[x];
                                 arr[x]=arr[y];
                                 arr[y]=temp;
                                 }
               
               int k1=1<<n;
               int flag=0;
               
               for(int i=1;i<k1;i++){
                       int sum_pat=0;
                       int sum_sean=0;
                       long long unsigned int sum=0;
                       
                       
                       for(int j=0;j<n;j++){
                               if(i&(1<<j)) sum_pat^=arr[j];
                               else {sum_sean^=arr[j]; sum+=arr[j];//cout<<sum_sean<<" for "<<i<<endl;
                               }
                               }
                       if(sum_pat==sum_sean){
                                             //cout<<sum_pat<<" "<<sum_sean<<endl;
                                             printf("Case #%d: %ld\n",case_no,sum);
                                             flag=1;
                                             break;
                                             }
                                             }
                       
               if(!flag) printf("Case #%d: NO\n",case_no);
               }
    return 0;
}

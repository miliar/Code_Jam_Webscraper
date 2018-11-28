#include<iostream>
using namespace std;
int main(){
    int t,len,i,j,k,pos;
    char arr[100],tmp,mn;
    cin>>t;
    for(i=1;i<=t;i++){
                      cin>>arr;
                      len=strlen(arr);
                      for(j=len-1;j>0;j--){
                      if(arr[j-1]<arr[j])
                      break;}
                             mn=100,pos=-1;
                             for(k=j;k<len;k++){
                              if(arr[k]>arr[j-1] && arr[k]<mn){
                                           
                                           pos=k;mn=arr[k];}}
                        tmp=arr[j-1];
                        arr[j-1]=arr[pos];
                        arr[pos]=tmp;
                        sort(arr+j,arr+len);
                        if(j==0){
                                 for(k=len-1;k>0;k--)
                                 arr[k+1]=arr[k];
                                 arr[len+1]='\0';
                                 arr[1]='0';}
                                 k=0;
                                 if(arr[0]=='0'){
                                 while(arr[k]=='0')k++;
                                 arr[0]=arr[k];
                                 arr[k]='0';}     
                      cout<<"Case #"<<i<<": "<<arr<<"\n";}}
                      
               

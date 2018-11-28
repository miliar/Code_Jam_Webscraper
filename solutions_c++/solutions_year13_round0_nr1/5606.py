#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
    int n,x,flag=1 ,count;
    char temp;
    
    cin>>n;
    char arr[n][16],arr1[n][4][4];
    
    for(int i=0;i<n;i++)
    {
       for(int j=0;j<4;j++)
         for(int k=0;k<4;k++){
            cin>>arr1[i][j][k];
              }       
             cout<<"\n"; 
    } 
   for(int i=0;i<n;i++)
    {  
           int l=0;
       for(int j=0;j<4;j++)
         for(int k=0;k<4;k++){
         arr[i][l++]=arr1[i][j][k];
              }       
    } 

    for(int i=0;i<n;i++){
      for(int j=0;j<4;j++){
             temp= arr[i][4*j]; count=1; 
             
            for(int k=1;k<4;k++)
             if(arr[i][4*j]!='.'&&(arr[i][4*j+k]=='T' || arr[i][4*j+k]==arr[i][4*j]))
               count = count+1;
             
             if(count==4) {
             cout<<"Case #"<<i+1<<": "<<temp<<" won\n"; flag=0;break;
              }
             count=1;
         temp = arr[i][j];
         for(int k=1;k<4;k++)
           if(arr[i][4*j]!='.'&&(arr[i][j+k*4]=='T' || arr[i][j+k*4]==arr[i][j])&&flag==1 )
            count= count+1;
            
            if(count==4){
                           cout<<"Case #"<<i+1<<": "<<arr[i][j]<<" won\n";flag=0;break;
                           
          }  }
          temp=arr[i][3];count=1;
         for(int k=2;k<5;k++)
          if(arr[i][3]!='.'&&(arr[i][3*k]=='T'|| arr[i][3*k]==arr[i][3])&&flag==1)
           count=count+1;
          
          if(count==4&&flag==1){
                         cout<<"Case #"<<i+1<<": "<<arr[i][3]<<" won\n";flag=0;
                       }
        temp=arr[i][0];count=1;
         for(int k=1;k<4;k++)
          if(arr[i][0]!='.'&&(arr[i][5*k]=='T'|| arr[i][5*k]==arr[i][0])&&flag==1)
           count=count+1;
          
          if(count==4&&flag==1){
                         cout<<"Case #"<<i+1<<": "<<arr[i][0]<<" won \n";flag=0; }
        for(int j=0;j<16;j++)
            if(arr[i][j]=='.'&&flag==1) {cout<<"Case #"<<i+1<<": Game has not completed\n"; flag=0;break;}
            
            if(flag==1)cout<<"Case #"<<i+1<<": "<<"Draw \n";
            flag=1;
        
         } 
      getch();
      return 0; 
}

#include<iostream>
using namespace std;
int main(){
    int N,i,j,k;
    cin>>N;
    getchar();
    for(i=0;i<N;i++){
                     char text[1000],str[20]="welcome to code jam";
                     cin.getline(text,1000);
                     int len=strlen(text);
                     int arr[19][1000];
                     int cnt=1;
                     for(j=0;j<len;j++){
                     if(text[j]=='w')
                     arr[0][j]=cnt++;
                     else
                     arr[0][j]=(j-1>=0?arr[0][j-1]:0);}
                     for(j=1;j<19;j++){
                                       for(k=0;k<len;k++){
                                       if(k<j)
                                       arr[j][k]=0;
                                       else{
                                       if(str[j]==text[k])
                                       arr[j][k]=(arr[j-1][k]+arr[j][k-1])%10000;
                                       else
                                       arr[j][k]=arr[j][k-1];}}}
                                       char ans[5]="0000";
                                       int an=arr[18][len-1],in=3;
                                       while(an>0){
                                                   ans[in]=(char)(an%10+'0');
                                                   an/=10;
                                                   in--;}
                                                   ans[4]='\0';
                                                   cout<<"Case #"<<i+1<<": "<<ans<<"\n";}}
                                       
                                                                  

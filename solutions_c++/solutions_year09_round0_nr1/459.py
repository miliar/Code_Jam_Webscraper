#include<iostream>
using namespace std;
int main(){
    int L,D,N,i,j,k,l,m;
    cin>>L>>D>>N;
    char wrds[5000][100];
    for(i=0;i<D;i++)
    cin>>wrds[i];
    for(i=0;i<N;i++){
                     char arr[100][100];
                     char patt[1000];
                     cin>>patt;
                     k=0,j=0,l;
                     while(patt[k]!='\0'){
                     if(patt[k]=='('){
                                k++;
                                l=0;
                                while(patt[k]!=')')
                                arr[j][l++]=patt[k++];
                                arr[j][l]='\0';
                                j++,k++;}
                                else{
                                     arr[j][0]=patt[k++];
                                     arr[j][1]='\0';
                                     j++;}}
                                     int count=0;
                                     for(j=0;j<D;j++){
                                     for(l=0;l<L;l++){
                                     for(m=0;arr[l][m];m++){
                                                            if(arr[l][m]==wrds[j][l])
                                                            break;}
                                                            if(arr[l][m]=='\0')
                                                            break;}
                                                            if(l==L)
                                                            count++;}
                                                            cout<<"Case #"<<i+1<<": "<<count<<"\n";}}
                                
                     
                     
                     
                                        

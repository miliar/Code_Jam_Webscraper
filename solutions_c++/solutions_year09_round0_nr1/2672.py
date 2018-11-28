#include<iostream>

using namespace std;
int main()
{
int L,D,N,m,t,counter,c,i,j;
bool flag;  char in[5000][16],out[1100];
  cin>>L>>D>>N;
  for(i=0;i<D;i++)
  {
  cin>>in[i];
  }
  for(t=0;t<N;t++)
  {    c=0;
  cin>>out;
  

  for(j=0;j<D;j++){
  i=0; counter=0; m=0;  
  while(out[i]!='\0'){ 
                         flag=false;
  if(out[i]=='(') { 
                    while(out[i]!=')'){ 
                                          if(out[i]==in[j][m]) {
                                                                 if(flag==false) {
                                                                                  counter++;  flag=true;
                                                                                  }}
                                                                                  i++;
                                                                 }}
  else if(out[i]==in[j][m]) {counter++; }
  i++;
  m++;
    
  } if(counter==L) c++;
  
  }
  cout<<"Case #"<<(t+1)<<": "<<c<<endl;
  }
  return 0;


  }

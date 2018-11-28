#include<iostream>
using namespace std;
bool isPossible(char * s,bool inp[][30])
{
     int i;
     for(i=0;s[i]!='\0';i++) if(inp[i][s[i]-'a']==false) return false;
     return true;
}
int main()
{
    int L,D,N,i,j,k,p,n;
    char dict[5010][20],inp1[1000];
    bool inp[20][30],in;
    cin>>L>>D>>N;
    for(i=0;i<D;i++) cin>>dict[i];
    for(i=0;i<N;i++) {
                      cin>>inp1;
                      for(j=0;j<=L;j++) for(k=0;k<30;k++) inp[j][k]=false;p=n=0;in=false;
                      for(j=0;inp1[j]!='\0';j++) {
                                                  if(inp1[j]=='(') in=true;
                                                  else if(inp1[j]==')') {in=false;p++;}
                                                  else {inp[p][inp1[j]-'a']=true;if(!in) p++;}
                                                  
                                                 }
                      for(j=0;j<D;j++) if(isPossible(dict[j],inp)) n++;
                      cout<<"Case #"<<i+1<<": "<<n<<endl;
                     }
    return 0;
}

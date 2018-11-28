using namespace std;
#include<iostream>
#include<cstring>
#include<string>

int main()
{
int l,i,j,k=1,n;
char st[111],nt[10],ch;
//char ar[]={'y','h','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char ar[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
freopen("A-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);

cin.getline(nt,10);
n = atoi(nt);
while(n--)
{
          cin.getline(st,111);
          
          for(i=0;i<strlen(st);i++)
          {   
              j = (int)st[i];
              //cout<<st[i]<<" "<<ar[j-97];
              if(st[i]==' ') st[i]=' ';
              else  st[i] = ar[j-97];
              //cout<<st[i]<<"\n";
          }

          //cout.write("Case #"); cout.write(k);cout.write(": ");
          cout<<"Case #"<<k<<": ";
          cout.write(st,strlen(st));
          cout<<endl; k++;
}

return 0;
}   


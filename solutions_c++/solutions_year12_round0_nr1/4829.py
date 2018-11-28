#include<iostream.h>
#include<conio.h>
int main()
{
    char a,t;
    char g[30][101];
    int i,n,cases,j;
    char s[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    cin>>cases;
    gets(g[0]);
    for(i=0;i<cases;i++){
                         gets(g[i]);
                         }
    for(j=0;j<cases;j++){
                           cout<<"Case #"<<j+1<<": ";
                     for(i=0;g[j][i]!='\0';i++){
                          if(g[j][i]!=' '){
                                  t=s[((int)(g[j][i]) - 97)];
                                  cout<<t;
                                 }
                         else cout<<g[j][i];
                         }
                     if(j!=(cases-1)) cout<<"\n";
                     }
    return 0;
}

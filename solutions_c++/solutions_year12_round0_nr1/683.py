#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#define LOCAL
#define MAXN 200
char buf[MAXN];
char y[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char to[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
using namespace std;
int main()
{


#ifdef LOCAL
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
#endif
int T;
char cc;
cin>>T;int tim=1;;
scanf("%c",&cc);
while(T--)
{ 
  memset(buf,0,sizeof(buf));
fgets(buf,sizeof(buf),stdin);

for(int i=0;i<MAXN;i++)
{ for(int j=0;j<26;j++)
    {
   if(buf[i]==y[j]){buf[i]=to[j];break;}
    }
}
cout<<"Case #"<<tim<<": ";
printf("%s",buf);
tim++;
}



return 0;
}


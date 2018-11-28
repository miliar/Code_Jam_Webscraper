#include <iostream>
#include <string.h>

using namespace std;
int p[20];
char buf[10010];

int main()
{
    int T,i,j,k;
    freopen("C-large.in","r",stdin);  
    freopen("p3.out","w",stdout);
    scanf("%d",&T);
    gets(buf);
    for(i=1;i<=T;i++) {
       gets(buf);
       //cout<<buf<<endl;
       memset(p,0,sizeof(p));
       for(j=0;j<strlen(buf);j++) {//1234567890123456789
                                   //welcome to code jam
          switch(buf[j]) {
            case ' ' : { p[8]=(p[7]+p[8])%10000; 
                         p[11]=(p[10]+p[11])%10000;
                         p[16]=(p[15]+p[16])%10000;
                         break;
                         }
            case 'w' : { p[1]++; break; }
            case 'e' : p[2]=(p[2]+p[1])%10000;   
                   p[7]=(p[6]+p[7])%10000;
                   p[15]=(p[15]+p[14])%10000;
                   break;
            case 'l' : p[3]=(p[2]+p[3])%10000;
                   break;
            case 'c' : p[4]=(p[3]+p[4])%10000;
                   p[12]=(p[11]+p[12])%10000;
                   break;
            case 'o' : p[5]=(p[4]+p[5])%10000;
                   p[10]=(p[9]+p[10])%10000;
                   p[13]=(p[12]+p[13])%10000;
                   break;
            case 'm' : p[6]=(p[5]+p[6])%10000;
                   p[19]=(p[18]+p[19])%10000;
                   break;
            case 't' : p[9]=(p[8]+p[9])%10000;
                   break;
            case 'd' : p[14]=(p[13]+p[14])%10000;
                   break;
            case 'j' : p[17]=(p[16]+p[17])%10000;
                   break;
            case 'a' : p[18]=(p[17]+p[18])%10000;
                   break; 
          }
         
       }//for
       printf("Case #%d: ",i);
       if(p[19]<10) printf("000");
       else if(p[19]<100) printf("00");
       else if(p[19]<1000) printf("0");
       printf("%d\n",p[19]);       
    }//for   
    return 0;   
}
    

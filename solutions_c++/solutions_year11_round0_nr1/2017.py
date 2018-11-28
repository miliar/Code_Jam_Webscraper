#include<iostream>
using namespace std;
int f(int a){return a>0?a:-a;}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int k = 1;
    scanf("%d",&t);
    while(t--)
    {
         int sum = 0;
         int n,i;
         scanf("%d",&n);
         
         int Opos = 1;
         int Bpos = 1;
         char ch[10];
         char Line[200];
         int Bline[200];
         int Oline[200];
         int pos;
         int len = 0,Olen = 0, Blen = 0;
         for(i=1;i<=n;i++)
         {
             scanf("%s %d",ch,&pos);
            // cout << ch << " " << pos << " " ;
             Line[len++] = ch[0];
             if(ch[0]=='O')
                Oline[Olen++] = pos;
             if(ch[0]=='B')
                Bline[Blen++] = pos;
         }
         int Oi=0,Bi=0;
         for(i=0;i<len;i++)
         {
                           
             if(Line[i]=='O')
             {
                int tempa = f(Oline[Oi]-Opos)+1;
                Opos = Oline[Oi];
                Oi++;
                sum += tempa;
                if(Bi!=Blen)
                {
                   if(tempa >= f(Bline[Bi] - Bpos)) Bpos = Bline[Bi];
                   else Bpos = (Bline[Bi] - Bpos) > 0 ? Bpos + tempa : Bpos - tempa;   
                }
             }
             
             if(Line[i]=='B')
             {
                int tempb = f(Bline[Bi]-Bpos)+1;
                Bpos = Bline[Bi];
                Bi++;
                sum += tempb;
                if(Oi!=Olen)
                {
                   if(tempb >= f(Oline[Oi] - Opos)) Opos = Oline[Oi];
                   else Opos = (Oline[Oi] - Opos) > 0 ? Opos + tempb : Opos - tempb;   
                }
             }
             //cout << Opos << " " << Bpos << endl;
         }
         printf("Case #%d: %d\n",k++,sum);
    }
    return 0;
}

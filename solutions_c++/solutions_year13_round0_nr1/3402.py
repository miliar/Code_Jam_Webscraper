#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

char map[5][5];

int main()
{
    int i,j,ans,cas=0;
    int t,a,b,c,d,ok,ok1,ok2,num;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while(t--){
       for(i=0;i<4;i++)
		   scanf("%s",map[i]);
       printf("Case #%d: ",++cas);
       ok=0,ok1=0,ok2=0,num=0;
       for(i=0;i<4;i++)
       {
         a=0,b=0;
         for(j=0;j<4;j++)
         {
            if(map[i][j]=='O')
               a++,num++;
            else if(map[i][j]=='X')
               b++,num++;
            else if(map[i][j]=='T')
            {
                a++;
                b++;
				num++;
            }

         }
		 if(a==4)
         {
             ok1=1;
             break;
         }
		 if(b==4)
		 {
		     ok2=1;
			 break;
		 }
       }
       if(num==16)
          ok=1;
	   for(j=0;j<4;j++)
       {
         a=0,b=0;
         for(i=0;i<4;i++)
         {
            if(map[i][j]=='O')
               a++;
            else if(map[i][j]=='X')
               b++;
            else if(map[i][j]=='T')
            {
                a++;
                b++;
            }

         }
		 if(a==4)
         {
             ok1=1;
             break;
         }
		 if(b==4)
		 {
		     ok2=1;
			 break;
		 }
       }
       a=0,b=0,c=0,d=0;
       for(i=0;i<4;i++)
       {
           if(map[i][i]=='O')
               a++;
           else if(map[i][i]=='X')
               b++;
           else if(map[i][i]=='T')
           {
               a++;
               b++;
           }
           if(map[i][3-i]=='O')
               c++;
           else if(map[i][3-i]=='X')
               d++;
           else if(map[i][3-i]=='T')
           {
               c++;
               d++;
           }
       }
       if(a==4||c==4)
           ok1=1;
       if(b==4||d==4)
           ok2=1;
       if(ok1)
         printf("O won\n");
       else if(ok2)
         printf("X won\n");
       else if(ok&&ok1==0&&ok2==0)
         printf("Draw\n");
      else if(ok==0&&ok1==0&&ok2==0)
         printf("Game has not completed\n");

    }
    return  0;
}

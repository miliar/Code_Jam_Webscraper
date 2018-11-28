# include<stdio>
# include<string>
# include<conio>
# include<algorithm>
using namespace std;
main()
{
freopen("input.txt","r",stdin);
char decode[27]="yhesocvxduiglbkrztnwjpfmaq";
freopen("output.txt","w",stdout);
int m;
scanf("%d",&m);
scanf("\n");
for(int i=0;i<m;i++)
 {
  char a[1000];
  gets(a);
  printf("Case #%d: ",(i+1));
  for(int j=0;a[j]!='\0';j++)
   {
    if(a[j]==' ')
     printf(" ");
    else
     printf("%c",decode[(int)a[j]-97]);
   }
  printf("\n");
 }
//getch();
}
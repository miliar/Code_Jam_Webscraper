#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    
    int t,a,b,i,count,num;
    int one,ten,hundred,thou,ten_thou,hund_thou,mil,New,New1,New2,New3,New4,New5;
    FILE *fp1,*fp2;
    if((fp1=fopen("C-large.in","r"))==NULL)exit(0);
    if((fp2=fopen("C-large.out","w"))==NULL)exit(0);
    fscanf(fp1,"%d",&t);
    for(count=1;count<=t;count++)
    {
         fscanf(fp1,"%d %d",&a,&b);                        
         fprintf(fp2,"Case #%d: ",count);
         num=0;
         for(i=a;i<=b;i++)
         {
             if(b<10){num=0;break;}
             if(b<100)
             {
                  ten=i/10;one=i%10;
                  New=one*10+ten;
                  if(i<New&&New<=b)num++;
             }    
             else if(b<1000)
             {
                  hundred=i/100;ten=i%100/10;one=i%10;
                  New=ten*100+one*10+hundred;
                  New1=one*100+hundred*10+ten;
                  if(i<New&&New<=b)num++;
                  if(i<New1&&New1<=b){if(New==New1)continue;else num++;}    
             }
             else if(b<10000)
             {
                  thou=i/1000;hundred=i%1000/100;ten=i%100/10;one=i%10;
                  New=hundred*1000+ten*100+one*10+thou;
                  New1=ten*1000+one*100+thou*10+hundred;
                  New2=one*1000+thou*100+hundred*10+ten;
                  if(i<New&&New<=b)num++;
                  if(i<New1&&New1<=b){if(New==New1)continue;else num++;}
                  if(i<New2&&New2<=b){if(New==New2||New1==New2)continue;else num++;}
             }
             else if(b<100000)
             {
                  ten_thou=i/10000;
                  thou=i%10000/1000;hundred=i%1000/100;ten=i%100/10;one=i%10;
                  New=thou*10000+hundred*1000+ten*100+one*10+ten_thou;
                  New1=hundred*10000+ten*1000+one*100+ten_thou*10+thou;
                  New2=ten*10000+one*1000+ten_thou*100+thou*10+hundred;
                  New3=one*10000+ten_thou*1000+thou*100+hundred*10+ten;
                  if(i<New&&New<=b)num++;
                  if(i<New1&&New1<=b){if(New==New1)continue;else num++;}
                  if(i<New2&&New2<=b){if(New==New2||New1==New2)continue;else num++;}
                  if(i<New3&&New3<=b){if(New==New3||New1==New3||New2==New3)continue;else num++;}
             }
             else if(b<1000000)
             {
                  hund_thou=i/100000;ten_thou=i%100000/10000;
                  thou=i%10000/1000;hundred=i%1000/100;ten=i%100/10;one=i%10;
                  New=ten_thou*100000+thou*10000+hundred*1000+ten*100+one*10+hund_thou;
                  New1=thou*100000+hundred*10000+ten*1000+one*100+hund_thou*10+ten_thou;
                  New2=hundred*100000+ten*10000+one*1000+hund_thou*100+ten_thou*10+thou;
                  New3=ten*100000+one*10000+hund_thou*1000+ten_thou*100+thou*10+hundred;
                  New4=one*100000+hund_thou*10000+ten_thou*1000+thou*100+hundred*10+ten;
                  if(i<New&&New<=b)num++;
                  if(i<New1&&New1<=b){if(New==New1)continue;else num++;}
                  if(i<New2&&New2<=b){if(New==New2||New1==New2)continue;else num++;}
                  if(i<New3&&New3<=b){if(New==New3||New1==New3||New2==New3)continue;else num++;}
                  if(i<New4&&New4<=b){if(New==New4||New1==New4||New2==New4||New3==New4)continue;else num++;}
             }
              else if(b<=2000000)
              {
                  mil=i/1000000;hund_thou=i%1000000/100000;ten_thou=i%100000/10000;
                  thou=i%10000/1000;hundred=i%1000/100;ten=i%100/10;one=i%10;
                  New=hund_thou*1000000+ten_thou*100000+thou*10000+hundred*1000+ten*100+one*10+mil;
                  New1=ten_thou*1000000+thou*100000+hundred*10000+ten*1000+one*100+mil*10+hund_thou;
                  New2=thou*1000000+hundred*100000+ten*10000+one*1000+mil*100+hund_thou*10+ten_thou;
                  New3=hundred*1000000+ten*100000+one*10000+mil*1000+hund_thou*100+ten_thou*10+thou;
                  New4=ten*1000000+one*100000+mil*10000+hund_thou*1000+ten_thou*100+thou*10+hundred;
                  New5=one*1000000+mil*100000+hund_thou*10000+ten_thou*1000+thou*100+hundred*10+ten;
                  if(i<New&&New<=b)num++;
                  if(i<New1&&New1<=b){if(New==New1)continue;else num++;}
                  if(i<New2&&New2<=b){if(New==New2||New1==New2)continue;else num++;}
                  if(i<New3&&New3<=b){if(New==New3||New1==New3||New2==New3)continue;else num++;}
                  if(i<New4&&New4<=b){if(New==New4||New1==New4||New2==New4||New3==New4)continue;else num++;}
                  if(i<New5&&New5<=b){if(New==New5||New1==New5||New2==New5||New3==New5||New4==New5)continue;else num++;}
             }
         }
         fprintf(fp2,"%d\n",num);                     
    }
    fclose(fp2);
    fclose(fp1);
    return 0;
}

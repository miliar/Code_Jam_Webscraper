#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int t,n;

main()
{
        FILE *f;
        f=fopen("ans.txt","w");
        int i,j,k;
        int curo,curb,so,sb,curs;
        char ch;
        int num;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
            curo=1;
            curb=1;
            so=0;
            sb=0;
            curs=0;
            scanf("%d",&n);
            for(j=0;j<n;j++)
            {
                scanf(" %c",&ch);
                scanf("%d",&num);
                if(ch=='O')
                {
                    if(abs(num-curo)+so<=curs)
                    {
                        curs++;
                        so=curs;   
                        curo=num;
                        
                    } 
                    else
                    {
                        curs=abs(num-curo)+so+1;
                        so=curs;
                        curo=num;
                        
                    }
                }
                else 
                {
                    if(abs(num-curb)+sb<=curs)
                    {
                        curs++;
                        sb=curs;  
                        curb=num;
                         
                    } 
                    else
                    {
                        curs=abs(num-curb)+sb+1;
                        sb=curs;
                        curb=num;
                        
                    }
                }
            } 
              //printf("Case #%d: %d\n",i+1,curs);
            fprintf(f,"Case #%d: %d\n",i+1,curs);
        }
        fclose(f);
        scanf(" ");
           
}

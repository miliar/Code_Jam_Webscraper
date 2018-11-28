#include<stdio.h>

char table[100]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    int tc;

    FILE *out,*in;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&tc);

    for(int q=0;q<tc;q++){
        int n,s,p;

        fscanf(in,"%d %d %d",&n,&s,&p);
        int ans=0;
        for(int i=0;i<n;i++){
            int t;

            fscanf(in,"%d",&t);
            if(t%3==2){
                t++;
            }
            if(t/3>=p) ans++;
            else if(t/3+1==p){
                if(t%3==1) ans++;
                else if(s>0 && p!=1){
                    s--;
                    ans++;
                }
            }
        }
        fprintf(out,"Case #%d: %d\n",q+1,ans);
    }



    return 0;
}

#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    FILE *input;
    FILE *output;
    input=fopen("small.in","r");
    output=fopen("output.out","w");
    int T;
    int N;
    int K;
    
    fscanf(input,"%d",&T);
    for( int i=1;i<=T;i++)
    {
        fscanf(input,"%d",&N);
        fscanf(input,"%d",&K);
        //printf("%d %d\n",N,K);
        int result=(K+1)%((int)pow(2,N));
        //string out="Case #"+itoa(i)+":";
        /*if(result==0) out+="ON";
        else out+="OFF/n";
        fprintf(output,"%s",out.c_str());*/
        if(result==0){
            //printf("Case #%d:ON\n",i);
            fprintf(output,"Case #%d: ON\n",i);
        }
        
        else {
            //printf("Case #%d:OFF\n",i);
            fprintf(output,"Case #%d: OFF\n",i);
        }
        
    }
    

    return 0;
    

}

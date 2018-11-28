#include <stdio.h>
#include <vector>

using namespace std;

vector<int> num(45);

int main()
{
    FILE *in,*out;
    int T,casen,i,j,k,n,ans,index;
    char d;
    
    
    in = fopen("in.txt","r");
    out = fopen("out.txt","w");
    
    fscanf(in,"%d\n",&T);
    for (casen = 1; casen <= T; casen++) {
        fscanf(in,"%d\n",&n);
       // printf("n = %d\n",n);
        for (i=1; i<=n; i++) {
            index = 0;
            for (j=1; j<=n; j++) {
                fscanf(in,"%c",&d);
        //        printf("i = %d,j = %d,%c\n",i,j,d);
                if (d == '1')
                    index = j;
            }
            num[i] = index;
            fscanf(in,"%c",&d);
        }
     /*   getchar();
        for (i=1; i<=n; i++)
            printf("%d\n",num[i]);
        printf("\n");
     */   
        ans = 0;
        for (i=1; i<=n; i++) 
            if (num[i] > i) {
                //search       
                for (j=i+1; j<=n; j++)
                    if (num[j] <= i)
                        break;
                        
                if (j>n) {
                    printf("ww");
                    getchar();
                }
                
                ans += j-i;
                num.erase(num.begin()+j);
                num.insert(num.begin(),0);
            }
        
        fprintf(out,"Case #%d: %d\n",casen,ans);
    }
    
    fclose(in);
    fclose(out);
   // getchar();
}
            

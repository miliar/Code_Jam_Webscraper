#include <stdio.h>
#include <stdlib.h>

int mult[] = {0,1,10,100,1000,10000,100000,1000000,10000000};

inline int getNumDigit(int inp)
{
    int i = 0;
    
    while(inp)
    {
        i++;
        inp = inp/10;
    }
    
    return i;
}

inline int rotateNum(int inp, int dig)
{
    int a, b, ret;
    //inp = 1234
    
    a = inp/10; //a = 123
    b = inp%10; //b = 4
    ret = b*mult[dig]+a;
    
    return ret;
}


int main()
{
    int T, A, B;
    int *arr = NULL;
    int i,j,k, arr_size, num_digit, rot, next_rot, pairs;    
    
    freopen ("E:\\input_recycle.txt","r",stdin);
    freopen ("E:\\output_recycle.txt","w",stdout);
    
    scanf("%d", &T);
    
    pairs = 0;
    
    for(i=1; i<=T; i++)
    {
        scanf("%d%d", &A,&B);
        
        arr_size = B-A+1;
        num_digit = getNumDigit(A);
        
        arr = (int*)calloc(arr_size, sizeof(int));
        pairs = 0;
        
        for(j=A; j<=B; j++)
        {
            if(arr[j-A])
            {
                continue;
            }
            
            rot = 0;
            next_rot = j;
            //printf("%d ", next_rot);
            arr[next_rot-A] = 1;
            
            for(k=0; k<num_digit; k++)
            {
                next_rot = rotateNum(next_rot,num_digit);
                
                if(A <= next_rot && next_rot <= B)
                {
                    if(arr[next_rot-A] == 0)
                    {
                        rot++;
                        arr[next_rot-A] = 1;
                        //printf("%d ", next_rot);
                    }
                }
            }
            
            pairs += (rot*(rot+1))/2;
            //printf("[%d]\n",(rot*(rot+1))/2);
            //if(rot) pairs++;
        }
        /*for(j=A; j<=B; j++)
        {
            printf("%d %d\n",j,arr[j-A]);
        }*/
        free(arr);
        arr = NULL;
        
        printf("Case #%d: %d",i,pairs);
        
        if(i<T)
            printf("\n");
    }

    fclose(stdin);   
    fclose(stdout);
}

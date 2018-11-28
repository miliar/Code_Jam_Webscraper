#include<stdio.h>
#include<cmath>
#include <queue>
#include <cstring>
#include <cstdlib>

using namespace std;

int Partition(int * pt_a, int left, int right) // exchange entity.
{
    int i=left;
    int j;
    int temp;
    
    for(j=left;j<=right-1;j++)
    {
        if(pt_a[j]<pt_a[right]) // the right one is pivot.
        {
            temp=pt_a[i];
            pt_a[i]=pt_a[j];
            pt_a[j]=temp;
            i++;
        }
    }
    temp=pt_a[i];
    pt_a[i]=pt_a[right];
    pt_a[right]=temp;
        
    return i;
}

void QSort(int * pt_a, int left, int right)
{
    if(left<right)
    {
        int mid=Partition(pt_a, left, right);
        QSort(pt_a, left, mid-1);
        QSort(pt_a, mid+1, right);
    }
}

int MaxFactor(int a, int b)
{
    if(a==0 || b==0)
    {
        return a+b;
    }
    
    int temp;
    if (a<=b)
        temp=b%a;
        else
        {
            temp=a%b;
            a=b;
        }
    if (temp==0)
        return a;
        else
        {
            return MaxFactor(temp, a);
        }   
}

int main()
{
    #ifndef ONLINE_JUDGE 
    freopen("in.txt","r",stdin); 
    freopen("out.txt","w",stdout); 
    #endif



     
    int i,j,n,case_num,max_factor,temp;
    
    int a[3];
    int b[3];
    
    scanf("%d", &case_num);    
    for(i=1;i<=case_num;i++)
    {
        memset(b,0,sizeof(b)*sizeof(int));
        scanf("%d", &n);
        
        for(j=0;j<n;j++)
        {
            scanf("%d", &a[j]);
        }
        
        QSort(a, 0, n-1);
        
        for(j=0;j<n-1;j++)
        {
            b[j]=a[j+1]-a[j];
        }
        
        QSort(a, 0, n-2);
        
        max_factor=MaxFactor(b[0], b[1]);
        
        temp=a[0]%max_factor;
        if(temp==0)
            printf("Case #%d: 0\n", i);
            else
                printf("Case #%d: %d\n", i, max_factor-temp);                     
     }
    
    #ifndef ONLINE_JUDGE 
    fclose(stdin); 
    fclose(stdout); 
    #endif


 

    return 0;
}

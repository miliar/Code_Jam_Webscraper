#include<stdio.h>

long pow(long a, long b)
{
    long ret=1;
    for(int i=0; i<b; i++) 
    {
        ret*=a;   
    }  
    return ret;
}

int main(void)
{
    FILE* fin = fopen("park.in", "r");
    FILE* fout = fopen("park.out", "w");  
    int n;
    fscanf(fin, "%d", &n);
    for(int i=1; i<=n; i++)
    {
        long a, b;
        int c;
        fscanf(fin, "%ld %ld %d", &a, &b, &c);
        long groups[c];
        for(int j=0; j<c; j++)
        {
            fscanf(fin, "%ld", &groups[j]);
        }
        long rides[c][2];
        int newIndex=0;
        int val=0;
        int size=0;
        for(int j=0; j<c; j++)
        {
            while(val+groups[newIndex]<=b && size<c)
            {
                val+=groups[newIndex];
                newIndex=(newIndex+1)%c;
                size++;
            }
            rides[j][0]=val;
            rides[j][1]=newIndex;
            val-=groups[j];
            size--;
        }
        int money=0, index=0;
        for(int j=0; j<a; j++)
        {
            money+=rides[index][0];
            index=rides[index][1];
        }
        fprintf(fout, "Case #%d: %d\n",  i, money);
    }
}

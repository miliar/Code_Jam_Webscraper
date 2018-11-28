#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<windows.h>

long long change(char buffer[100], int n)
{
        long long val = (long long)buffer[0];

		if( n == 0 )
			n = 2;

        int k;
        for(k = 1; buffer[k]!=100; k++)
        {
                val = val*n + (long long)buffer[k];
        }
		//printf("%d",n);
        return val;
}

long long go(char buffer[100])
{
        switch(strlen(buffer))
        {
                case 0:
                        return (long long)0;
                case 1:
                        return (long long)1;
                case 2:
                        if( buffer[0] == buffer[1] )
                                return (long long)3;
                        else
                                return (long long)2;
                default:
                        break;
        }
        int set[200];
		int k;
		for( k= 0; k< 200; k++)
		{
			set[k] = -1;
		}
        set[buffer[0]] = 1;
        buffer[0] = 1;
        int count;
        int temp;
        for( k = 1,count = 0; buffer[k] != '\0'; k++)
        {
                temp = set[buffer[k]];
                if( temp == -1 )
                {
                        set[buffer[k]] = count;
                        buffer[k] = count;
						if( count == 0 )
							count = 2;
						else
							count++;
                }
                else
                        buffer[k] = temp;
        }
        buffer[k] = 100;
        return change(buffer,count);
}

int main()
{
        FILE *in, *out;
        in = fopen("A-large.in","r");
        out = fopen("output.txt","w");

        int N;
        fscanf(in,"%d",&N);

        int k;
        char buffer[100];
        for(k = 0; k < N; k++)
        {
                fscanf(in,"%s",buffer);
                fprintf(out,"Case #%d: %lld\n",k+1,go(buffer));
        }
		system("pause");
}

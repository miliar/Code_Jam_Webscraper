#include<iostream>
using namespace std;

int main()
{
 	int t,a,b;
 	scanf("%d",&t);
    long long int s;

	for(int i=1; i<=t; i++)
	{
        s=0;
        scanf("%d %d",&a,&b);
        int arr[1001]={0};
        arr[0]=1;

        for(int j=a; j<=b; j++)
        {
            if(arr[j]==1) continue;
            else arr[j]=1;

            int old_j=j;
            int count=0,p=1;
            while(j)
            {
                count++;
                p=p*10;
                j=j/10;
            }
            j=old_j;
            p=p/10;
            int ctr=1;

            for(int k=1; k<count; k++)
            {
                j=(j/10)+((j%10)*p);
                if(j>old_j && j<=b)
                {
                   ctr++;
                   arr[j]=1;
                   //cout<<old_j<<" "<<j<<endl;

                }

            }
            if(ctr>1)
                  s=s+(ctr*(ctr-1))/2;

            j=old_j;

        }

        printf("Case #%d: %lld\n",i,s);
	}

 	return 0;
}

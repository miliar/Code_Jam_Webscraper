#include<stdio.h>
#include<math.h>
#include<iostream>
#include<map>
#include<string>
using namespace std;
//int h[2000000][2000000];
 map<int, map<int, int> > m1;
int find_len(int v)
{
    int s=0;
    while(v/=10)
        s++;
    return s+1;
}
int main()
{
    FILE *in,*o;
     in=fopen("input.in","r");
    o=fopen("output.txt","w");

        int t,i,j,k,temp,length,cnt,m,n,num,mul;
        fscanf(in,"%d",&t);
        //scanf("%d",&t);
        for(i = 1; i <= t; i++)
        {cnt = 0;
            fscanf(in,"%d%d",&m,&n);
            //scanf("%d%d",&m,&n);
            m1.erase(m1.begin(),m1.end());
            for(j =m; j <=n; j++)
            {length = find_len(j);
             temp = j;
              mul=pow(10,length);
                  while(length> 1)
                    {
                        num = (temp + (temp % 10)*mul ) / 10;
                                if((num <= n)&&(num > j)&&(num != temp)&&(!m1[j][num]))
                                        { // printf("%d==> %d\n",temp,num);
                                            m1[j][num]=1;
                                           // mymap.first=it;
                                            cnt++;
                                        }
                                temp = num;
                                length--;
                    }
                }
               printf("Case #%d: %d\n",i,cnt);
                fprintf(o,"Case #%d: %d\n",i,cnt);
        }
        return 0;
}

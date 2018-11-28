#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

int tests;

int A,B;
int dig;
int big_base;
int d[10];
long long ans;
void get(int num)
{
    int v = 1;
    int b = big_base;
    int temp;
	set<int> rec;
    for(int i = 0; i < (dig-1); i++)
    {
		int low = num%d[v];
        if (low >= (d[v-1]))
        {
            temp = (num / d[v]) + low*d[b];
			if ((temp != num)&&(temp >= A)&&(temp <= B)&&(rec.find(temp) == rec.end()))
            {
				rec.insert(temp);
	            ans++;
            }
        }
        b--;
		v++;
    }
}

int main()
{
	d[0] = 1;
    for(int i = 1; i < 9; i++)
		d[i] = d[i-1]*10;
    freopen("input.txt","r",stdin);    
    freopen("output.txt","w",stdout);    
    scanf("%d\n",&tests);
    for(int t = 0; t < tests; t++)
    {
        scanf("%d%d",&A,&B);
      	ans = dig = 0;
      	big_base = 1;
      	int temp = A;      	
        while(temp != 0)
        {
            temp/=10;
            dig++;            
        }
        big_base = dig - 1;
        for(int i = A; i <= B; i++)
            get(i);
        ans /= 2;
        printf("Case #%d: %lld\n",(t+1),ans);
    }
    
    return(0);
}


#include <iostream>

using namespace std;

int main()
{
    int t;
    int test = 0;
//freopen("C-large.in","r",stdin);
//freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
       test ++;
       int r,k,n;
       scanf("%d%d%d",&r,&k,&n);
       int num[1010];
       for(int i = 1; i <= n; i++) scanf("%d",&num[i]);
       int flag[1010] = {0};
       int val[1010] = {0};
       int head = 1;
       int cur = 0;
	   int start = 0;
	   int start_id;
       while(1)
       {
           cur++;
           int tmp_sum = 0;
           int tmp_i = head;
           int tmp_num = 0;
           while(1)
		   {
              tmp_sum += num[tmp_i];
			  tmp_num ++;
              if(tmp_sum > k)
              {                 
                 val[cur] = tmp_sum-num[tmp_i];
				 if(!flag[head])
				 {
					 flag[head] = cur;
				 }
				 else
				 {
					 start = cur;
					 start_id = head;
				 }
				 head = tmp_i;
				 break;
			  }
			  else if(tmp_num == n)
			  {
				  val[cur] = tmp_sum;				  
                  if(!flag[head])
				 {
					 flag[head] = cur;
				 }
				 else
				 {
					 start = cur;
					 start_id = head;
				 }
				 head = tmp_i + 1;
				 if(head > n) head = 1;
				 break;
			  }
			  else 
			  {
				  tmp_i ++;
				  if(tmp_i > n) tmp_i = 1;
			  }
		   }           
		   if(start) break;
		   if(cur == r) break;
	   }
       long long ans = 0;
	   if(cur == r)
	   {
           for(int i = 1; i <= cur; i++) ans += (long long)val[i];
	   }
	   else if(start)
	   {
		   for(int i = 1; i <= flag[start_id]; i++) ans += (long long)val[i];
		   long long tmp = 0;
		   for(int i = flag[start_id]+1; i <= cur; i++) tmp += (long long)val[i];
		   r -= flag[start_id];
		   int len = cur - flag[start_id];
		   int tmp1 = r/len;
		   int tmp2 = r%len;
		   ans += ((long long)tmp) * ((long long)tmp1);
		   for(int i = flag[start_id]+1; i <= flag[start_id]+tmp2; i++) ans += (long long)val[i];
	   }
	   printf("Case #%d: %I64d\n",test,ans);
	}
	return(0);
}



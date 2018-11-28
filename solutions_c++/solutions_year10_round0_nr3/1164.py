#include<iostream>
using namespace std;

typedef __int64 LL;
const int N = 1000005;
LL pos[N],cnt[N],a[N],sum[N];
LL n,k,r;

int main() {
    int test,i,j;
    freopen("C-large.in","r",stdin);
    freopen("C-out.txt","w",stdout);
    scanf("%d",&test);
    for( int tc = 1; tc <= test;tc++ ) {
         cin>>r>>k>>n;
         
         for( i = 0; i < n ;i++ )
              cin>>a[i];
         
         memset(pos,-1,sizeof(pos));
         memset(cnt,0,sizeof(cnt));
         memset(sum,0,sizeof(sum));
         
         LL nowpos = 0,times = 0;
         int flag = 0;
         while( times <= r ) {
                   LL nowcnt = 0;
                   int rec = 0;
                   for( ; rec < n;nowpos++,rec++ ) {
                        nowpos %= n;
                        if( nowcnt+a[nowpos] > k) break;
                        nowcnt += a[nowpos];
                   }
                  // cout<<nowcnt<<endl;
                   ++times;
                   sum[times] = sum[times-1] + nowcnt;
                 //  cout<<" here "<<times<<" "<<sum[times]<<" "<<sum[times-1]<<endl;
                   nowpos = (nowpos-1+n)%n;
                   if( pos[nowpos] > 0 ) {
                       flag = 1;
                       break;
                   }
                  // cout<<nowpos<<endl;
                   pos[nowpos++] = times; 
         }
         
         //for( i = 0 ; i <= r;i++ )
             // cout<<sum[i]<<endl;
        // cout<<flag<<endl;
         printf("Case #%d: ",tc);
         if( flag == 0 ) cout<<sum[r]<<endl;
         else {
              LL start = pos[nowpos];
              LL len = times - start;
              if( len == 0 ) {
				//	puts("sfdfdsfdsf");
				//	system("pause");
				}
              LL val = sum[times] - sum[start];
              LL tmp = (r-start)/len;
              LL ans = tmp*val+sum[start];
              
              LL mod = (r-start)%len;
              ans = ans+(sum[start+mod] - sum[start]);
              cout<<ans<<endl;
         }
    }    
    return 0;
}

 

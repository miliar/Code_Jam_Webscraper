#include <iostream>

using namespace std;
    
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out_c.txt","w",stdout);
    long long sum[1002];
    long long  g[1002];
    long long  R , k ,N;
    
    int  flag[1002];
    int ca;
    cin >> ca;
    for (int i = 0 ;i < ca ;i++){   
        cin >> R >> k >> N;
        for (int j = 0 ;j < N ;j++)
            cin >> g[j];
        
       // cout << "R " << R << endl;
        int s = 0 ;
        long long ss = g[s];
        s++;
        while (s < N && ss + g[s] <= k){
            ss += g[s];
            s++;
        }
        long long res = 0;
        if (s == N){
            res = R * ss;
        }else{
            memset(flag,-1,sizeof(flag));
            int sumlen = 0;
            sum[sumlen++] = ss;
            res += ss;
          //  cout << "s " << s << endl;
            flag[s-1] = sumlen-1;
            ss = g[s];
            s = (s+1) % N;
          //  cout << "R " << R << endl;
            while (sumlen < R){
                if (ss + g[s] > k){
                    sum[sumlen++] = ss;
                    res += ss;
                    ss = g[s];
                    int ts = s - 1;
                    if (ts < 0)
                        ts = N-1;
                    if (flag[ts] >= 0){
                        //cout << "ts " << ts << endl;
                        //cout << "R " << R << endl; 
                        int leftr = R - sumlen;
                       // cout << "sumlen " << sumlen << endl;
                        long long  cl = 0;
                        for (int j = flag[ts] + 1 ;j < sumlen ;j++){
                            cl += sum[j];
                        }
                        //cout << "xxxxxx" << endl;
                     //   cout << res << endl;
                       // cout << "cl " << cl << endl;
                        //cout << "leftr " << leftr << endl;
                        //cout << "s - f = " << sumlen - flag[ts] << endl;
                        res += (leftr /(sumlen - 1 - flag[ts])) * cl;
                      //  cout << res << endl;
                        int txx =  leftr % (sumlen - 1 - flag[ts]);
                        for (int j = 1 ; j <= txx ;j++){
                            res += sum[flag[ts]+j];
                        }
                        break;
                    }else{
                        flag[ts] = sumlen-1;
                    }
                    
                
                }else{
                    ss += g[s];
                }
                s = (s+1) % N;
            }    
        }
        cout << "Case #" << i+1 << ": " << res << endl;
   }
  //  while (1);
}

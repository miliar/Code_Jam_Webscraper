#include<iostream>
#include<fstream>
using namespace std;

long long R , k , N , g[2001];
long long linkto[1001];
long long val[1001];
long long sum;
long long loc[1001] , cir_a , cir_b , cir_sum;

int main()
{
    ifstream cin("C.in");
    ofstream cout("C.out");
    int T;
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
            cin>>R>>k>>N;
            sum = 0;
            for(int j = 0 ; j < N ; j++)
            {
                    cin>>g[j];
                    sum += g[j];
                    g[j+N] = g[j];
            }
            if(sum <= k)
                   cout<<"Case #"<<caseID<<": "<<R * sum<<endl;
            else
            {
                for(int i = 0 ; i < N ; i ++)
                {
                        long long t = 0;
                        for(int j = i ; ; j++)
                        {
                                if(t + g[j] > k)
                                {
                                     linkto[i] = j % N;
                                     val[i] = t;
                                     break;
                                }
                                else
                                    t += g[j];
                        }
                }
                loc[0] = 0;
                cir_sum = 0;
                for(int i = 1 ; ; i ++)
                {
                        bool haverep = false;
                        loc[i] = linkto[loc[i - 1]];
                        for(int j = 0 ; j < i ; j++)
                                if(loc[i] == loc[j])
                                {
                                          haverep = true;
                                          cir_b = i;
                                          cir_a = j;
                                          sum = 0;
                                          for(int k = j ; k < i ; k++)
                                                  cir_sum += val[loc[k]];
                                          for(int k = 0 ; k < j ; k++)
                                                  sum += val[loc[k]];
                                }
                        if(haverep)
                                   break;
                }


                long long ans = 0;
                if(R > cir_a)
                {
                     R -= cir_a;
                     ans += sum;
                     long long t = R / (cir_b - cir_a);
                     R %= (cir_b - cir_a);
                     ans += cir_sum * t;
                     for(int i = cir_a ; i < cir_a + R ; i++)
                             ans += val[loc[i]];
                }
                else
                {
                    for(int i = 0 ; i < R ; i ++)
                            ans += val[loc[i]];
                }
                cout<<"Case #"<<caseID<<": "<<ans<<endl;
            }
    }
    return 0;
}

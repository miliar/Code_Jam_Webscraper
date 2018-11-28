#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int T, Case = 0;
    int N;
    long K;
    long i,j;
    int flag_power[30],flag_on[30];
    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("small_1.out","w",stdout);
    
    cin >> T;
    while(Case < T)
    {
              cin >> N >> K;
              if(K == 0)
                   cout << "Case #" << ++Case << ": " <<  "OFF" << endl;
              else
              {
                  memset(flag_power,0,sizeof(flag_power));
                  memset(flag_on,0,sizeof(flag_on));
                  flag_power[0] = 1;
                  for(i = 0;i < K;i++) 
                  {
                        for(j = 0;j < N;j++)
                              if(flag_power[j])     
                                  flag_on[j] = (flag_on[j] ? 0 : 1);//toggle
                                                    
                        for(j = 0;j < N;j++)
                              if(flag_power[j] && flag_on[j])
                                  flag_power[j+1] = 1;
                              else
                                  flag_power[j+1] = 0;                            
                  }
                  if(flag_power[N-1] && flag_on[N-1])
                      cout << "Case #" << ++Case << ": " <<  "ON" << endl;
                  else
                      cout << "Case #" << ++Case << ": " <<  "OFF" << endl;
              }
    }    
    return 0;    
}

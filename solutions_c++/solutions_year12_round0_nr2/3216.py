/* 
 * File:   main.cpp
 * Author: joker
 *
 * Created on 14 Апрель 2012 г., 15:06
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;


bool is_surprise(int a, int b, int c)
{
    if(abs(a-b)==2) return true;
    if(abs(a-c)==2) return true;
    if(abs(b-c)==2) return true;
    return false;
}

bool ok(int a, int b, int c)
{
    if(abs(a-b)>2) return false;
    if(abs(a-c)>2) return false;
    if(abs(b-c)>2) return false;
    return true;
}

int main(int argc, char** argv) {

    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large-attempt0.out","w",stdout);
    int n;
    cin >> n;
    for(int i = 0; i<n; i++)
    {
        int N,S,p;
        cin >> N >> S >> p;
        int cnt = 0;
        for(int j = 0; j<N; j++)
        {
            int item;
            cin >> item;
            int item3 = item/3;
            bool find_not_surprise=false, find_surprise=false;
            for(int a=item3-2;a<=item3+2;a++)
            {
                for(int b=item3-2;b<=item3+2;b++)
                {

                    for(int c=item3-2;c<=item3+2;c++)
                    {
                        if(a+b+c!=item) continue;
                        if(a<0 || b<0 || c<0) continue;
                        if(!ok(a,b,c)) continue;
                        if((a>=p || b>=p || c>=p)) {
                            //printf(">>>%d=%d+%d+%d\n",item,a,b,c);
                            if(!is_surprise(a,b,c))
                                find_not_surprise = true;
                            else
                                find_surprise = true;
                        }
                    }
                }

            }
            if(find_not_surprise)
            {
                cnt++;
                //cout << "UnSurprised" << endl;
            }
            else if(find_surprise && S>0)
            {
                cnt++;
                S--;
                //cout << "Surprised" << endl;
            }
        }
        cout <<"Case #"<< i+1 <<": "<< cnt << endl;
    }
    return 0;
}


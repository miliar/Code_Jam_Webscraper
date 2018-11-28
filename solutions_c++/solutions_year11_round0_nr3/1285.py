#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>

using namespace std;
int arr[2000];
int main(int argc, char** argv) 
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TC;
    cin>>TC;
    for(int tc = 1; tc<=TC; ++tc)
    {
        int N;
        cin>>N;
        int S = 0;
        for(int i = 0; i < N; ++i)
        {
            cin>>arr[i];
            S ^= arr[i];
        }
        if(S!=0)printf("Case #%d: NO\n",tc);
        else{
            S=0;
            sort(arr, arr+N);
            reverse(arr,arr+N);
            for(int i = 0; i < N-1; ++i)
                S += arr[i];
            printf("Case #%d: %d\n",tc,S);
        }
    }
    return 0;
}



/* 
 * File:   C.cpp
 * Author: Carlos
 *
 * Created on May 7, 2011, 12:41 AM
 */

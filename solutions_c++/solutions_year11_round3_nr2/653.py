#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<fstream>

using namespace std;

int main( void ){
    ifstream inFile("data.in");
    ofstream outFile("data.out");
    int i,j;
    long long k,m,n,t,l,num;
    long long c[2000],top[2000];
    long long max = 0;
    long long time;
    inFile >> t;
    for( int q = 0 ; q < t ; q++ ){
        inFile >> l >> time >> n >> num;
        for( i = 0 ; i < num ; i++ ) inFile >> c[i];
        for( i = 0 ; i < n % num ; i++ ) top[i] = n / num + 1;
        for( i = n % num ; i < n ; i++ ) top[i] = n / num;
        for( i = 0 ; i < num ; i++ ) max += c[i] * top[i];
        int len = time / 2;
        i = 0;
        while( len >= c[i] && top[i] > 0 ){
            len -= c[i];
            top[i]--;
            i++;
            if( i >= num ) i = 0;
        }
        if( top[i] == 0 ){
            outFile << "Case #" << q + 1 << ": " << max * 2 << endl;
            max = 0;
            continue;
        }
        if( len > 0 ){
            len = c[i] - len;
            top[i]--;
        }
        for( i = 0 ; i < num - 1 ; i++ )
            for( j = 0 ; j < num - i - 1 ; j++ )
                if( c[j] < c[j+1] ){
                    int tmp = c[j];
                    c[j] = c[j+1];
                    c[j+1] = tmp;
                    tmp = top[j];
                    top[j] = top[j+1];
                    top[j+1] = tmp;
                }
        long long count = l;
        long long dis = 0;
        bool flag = false;
        for( i = 0 ; i < num && count > 0 ; i++ ){
            if( len > c[i] && !flag ){
                flag = true;
                count--;
                dis += len;
                if( count == 0 ) break;
            }
            int tmp = top[i];
            if( tmp > count ) tmp = count;
            dis += c[i] * tmp;
            count -= tmp;
        }
        if( count > 0 ) dis += len;
        long long noacc = max - dis;
        long long ans = dis + noacc * 2;
        outFile << "Case #" << q + 1 << ": " << ans << endl;
        max = 0;
    }
    inFile.close();
    outFile.close();
    return 0;
}

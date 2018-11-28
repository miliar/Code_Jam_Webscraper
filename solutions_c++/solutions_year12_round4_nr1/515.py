#include <iostream>
#include <fstream>
#include <algorithm>
//#include <string>
//#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <memory.h>


#define out(x) (cout<<#x<<":"<<x<<" ")
#define outln(x) (cout<<#x<<":"<<x<<endl)
#define outs(x) (cout<<x<<" ")
#define outline (cout<<endl)
#define mssleep(time) usleep((time)*(10*1000))

#define FOR_I(begin,end) for (int i=begin;i<end;i++)
#define FOR_J(begin,end) for (int j=begin;j<end;j++)
#define FOR_K(begin,end) for (int k=begin;k<end;k++)
#define FOR_I_J(B1,E1,B2,E2) FOR_I(B1,E1) FOR_J(B2,E2)
#define FOR_I_J_K(B1,E1,B2,E2,B3,E3) FOR_I_J(B1,E1,B2,E2) FOR_K(B3,E3)

using namespace std;

	template <typename T>
	void debug_a(T * data,int begin,int end){
		for (int i=begin;i<end;i++) cout<<"["<<i<<"]: "<<data[i]<<"\t";cout<<endl;
	}
	template <typename T>
	void debug_a(T * data,int end){
		debug_a(data,0,end);
	}
	template <typename T>
	void debug_a2(T * data,int end1,int end2){
		for (int i=0;i<end1;i++){cout<<"row "<<i<<endl; for (int j=0;j<end2;j++) cout<<"["<<i<<","<<j<<"] "<<data[i][j]<<"\t";cout<<endl;}
	}

	template <typename T>
	T checkmin(T & data,T value){
		data = min(data,value);
		return data;
	}


const int N = 10010;
int array[N];
int dist[N];
int dp[N];
int n;

int all;
bool ans = false;

	void work(){
	    FOR_I(0,n) dp[i] = 0;


	    ans = false;
	    dp[0] = min(array[0],dist[0]);
        if ( 2*dp[0] >= all ){
                        ans = true;
                        return ;
                    }


	    FOR_I(0,n){
	        int j;
            for ( j=i+1;j<n;j++ ){
                if ( dist[i] + dp[i] >= dist[j] ){
                    int temp = min( dist[j] - dist[i] , array[j] );
                    dp[j] = max(dp[j],temp);
                    if ( dp[j] + dist[j] >= all ){
                        ans = true;
                        return ;
                    }
                }
                else break;
            }
            //debug_a(dp,0,j);
	    }
	}

    void inputing(){
        scanf("%d",&n);
        FOR_I(0,n){
            scanf("%d",&dist[i]);
            scanf("%d",&array[i]);
        }
        scanf("%d",&all);
    }


int main(){
    //freopen("D:\\ACM\\in.txt","r",stdin);
    freopen("D:\\ACM\\A-large.in","r",stdin);
    freopen("D:\\ACM\\out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    FOR_I(0,cas){

        inputing();
        work();
        if (ans)
        printf("Case #%d: YES\n",i+1);
        else printf("Case #%d: NO\n",i+1);
        //break;
    }
    return 0;
}

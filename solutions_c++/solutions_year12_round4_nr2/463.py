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
int X,Y;

struct node{
    int x,y;
    int r;
};
int counts;
node queue[4*N];
node taken[N];
int n;

int ans_c = 0;


    void center(node & n ,double & x, double & y){
            x = (double)n.x + (double)n.r/2.0;
            y = (double)n.y + (double)n.r/2.0;
    }

    inline double disk(node &n1,node &n2){
        double x1,y1,x2,y2;
        center(n1,x1,y1);
        center(n2,x2,y2);
        x1 = (x1 - x2);
        y1 = (y1 - y2);
        return sqrt(x1*x1 + y1*y1);
    }

    bool checkboard(int index){
        double x1,y1;
        center(taken[index],x1,y1);
        if ( 0<= x1 && x1 <=X)
            if ( 0<= y1 && y1 <= Y)
                return true;
        return false;
    }

    bool interect(int index){
        if (!checkboard(index))
            return true;

        FOR_I(0,index){
            double dist = disk( taken[index], taken[i] );
//            printf("%d %d dist: %lf\n",i,index,dist);//debug

            if ( dist < (double)( taken[index].r + taken[i].r ) )
            return true;
        }
        return false;
    }

    bool dfs(int index,int count){
        if ( index>=n ){
            ans_c++;
//            cout<<"ANSWER"<<endl;
            return true;
        }
        int count2 = count;
        for (int i=0;i<count;i++){
            taken[index].x = queue[i].x;
            taken[index].y = queue[i].y;
            taken[index].r = array[index];
//            printf("try place [ %d ]( %d ) to  %d %d\n",index,array[index],queue[i].x,queue[i].y);//debug
            if (!interect(index)){
//                printf(" PLACE [ %d ]( %d ) to  %d %d\n",index,array[index],queue[i].x,queue[i].y);//debug
                //add 3 points
                queue[count2].x = taken[index].x + 2*taken[index].r;
                queue[count2].y = taken[index].y;
                count2++;
                queue[count2].x = taken[index].x;
                queue[count2].y = taken[index].y + 2*taken[index].r;
                count2++;
                queue[count2].x = taken[index].x + 2*taken[index].r;
                queue[count2].y = taken[index].y + 2*taken[index].r;
                count2++;
                if (dfs(index + 1,count2)){
                    return true;
                }
            }
        }
    }

int array2[N];

	void work(){
	    counts = 0;
	    queue[counts].x = queue[counts].y = 0;
	    counts++;

        FOR_I(0,n) array2[i] = array[i];
        sort(array,array+n);
        reverse(array,array+n);

//	    debug_a(array,n);
	    dfs(0,counts);
	}

	void outputing(){
	    double x,y;

	    bool v[N];
	    FOR_I(0,n) v[i] = false;
        FOR_I(0,n){
            int k = 0;
            FOR_J(0,n)
                if (!v[j] && array[j] == array2[i]){
                    v[j] = true;
                    k = j;
                    break;
                }
            center(taken[k],x,y);
//            printf("%d %d %d\n",taken[k].x,taken[k].y,taken[k].r);
            //printf("%d %d %d\n",taken[indexes[i]].x,taken[indexes[i]].y,taken[indexes[i]].r);
            printf(" %.1lf %.1lf",x,y);
        }

	}

    void inputing(){
        scanf("%d%d%d",&n,&X,&Y);
        FOR_I(0,n)
            scanf("%d",&array[i]);
    }


int main(){
    freopen("D:\\ACM\\B-large.in","r",stdin);
    //freopen("D:\\ACM\\A-large.in","r",stdin);
    freopen("D:\\ACM\\out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    FOR_I(0,cas){
        inputing();
        work();
        printf("Case #%d:",i+1);
        outputing();
        printf("\n");
    }
    //outln(ans_c);
    return 0;
}

/*
12

4 4 4
3 4 5 (*)

15           (multiple of 3 ==> exactly 2 possibilities)

5 5 5
4 5 6 (*)


13        (multiple of 3 +1 ==> 2 possibilities)

4 4 5
3 5 5 (*)

14  (multiple of 3+2) ==> 2 possibilities)

4 4 6 (*)
4 5 5

*/

#include<iostream>
#include<stdio.h>
#include<cmath>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include <utility>
#include <bitset>
#define pb push_back

using namespace std;

map < pair<int,int> , int > soln;


int n,surprise,check;
int arr[105];

int maximum_non_surprising(int total){
    if(total%3==0)
      return total/3;
    else
      return total/3+1;
}
int maximum_surprising(int total){
    
    if(total%3==2)
        return total/3+2;
    else
        return total/3+1;
}


int findbest(int index, int surprise_left){
    if(soln[make_pair(index,surprise_left)])
              return soln[make_pair(index,surprise_left)];                              
    
    if(index==0){
          if(surprise_left==0 && maximum_non_surprising(arr[0])>=check )
              return 1;
          else if(surprise_left==1 && maximum_surprising(arr[0])>=check )
              return 1;
          else if(surprise_left>1)
              return -999999;
          else return 0;       
    }
    int max1=0,max2=0;
    
    if(maximum_non_surprising(arr[index])>=check)
      max1=1+findbest(index-1,surprise_left);
    else
      max1=findbest(index-1,surprise_left);  
            
    if(surprise_left>0 && arr[index]>=2){
       if(maximum_surprising(arr[index])>=check)
            max2=1+findbest(index-1,surprise_left-1);
       else
            max2=findbest(index-1,surprise_left-1);
                        
    }
    int sol=max(max1,max2);
    soln[make_pair(index,surprise_left)]=sol;
    return sol;
}



int main(){
    int i,j,t;
  //  freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++){
               soln.clear();
               printf("Case #%d: ",i);
               scanf("%d %d %d",&n,&surprise,&check);
               for(j=0;j<n;j++)
                   scanf("%d",&arr[j]);
               
               printf("%d\n",findbest(n-1,surprise));
                          
    }
    return 0;
}

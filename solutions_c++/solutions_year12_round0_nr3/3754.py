#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <set>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    int a,b;
    for(int i=1;i<=t;++i){
            scanf("%d%d",&a,&b);
             set < pair <int,int> > myset;
            int c=0;
            for(int j=a;j<=b;++j){
                    vector <int> vec;
                    int num;
                    num=j;
                    while(num>0){
                                 vec.push_back(num%10);
                                 num/=10;
                                 }
                    for(int ii=0;ii<vec.size()-1;++ii){
                            int temp=vec[0];
                            for(int jj=0;jj<vec.size()-1;++jj){
                                    vec[jj]=vec[jj+1];
                                    }
                            vec[vec.size()-1]=temp;
                            int val=0;
                            for(int jj=vec.size()-1;jj>=0;--jj){
                                    val=10*val+vec[jj];
                                    }
                            
                            if(val>j && val<=b){
                                       myset.insert(make_pair(j,val));
                                       }
                            }
                    }
            printf("Case #%d: %d\n",i,myset.size());
            }
    return 0;
}
            
                                       
                            
                            
                    
                    

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <functional>
#include <iterator>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <cassert>
#include <list>

using namespace std;

#define FOR(i, l, u) for(int (i)=(l); (i) < (u); ++(i))
#define FORD(i, u, l) for(int (i) = (u); (i) >= (l); --(i))
#define SHIFTL(i,n) ((i) << (n))
#define SHIFTR(i,n) ((i) >> (n))
#define POW2(n) SHIFTL(1, n)

typedef vector<int> v_int;
typedef vector<string> v_string;
typedef map<string, int> map_s;
typedef set<string> set_s;
typedef set<int> set_i;
typedef pair<int,int> pair_i;




int main() {
	int H,W,N;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
    fin>>N;
    for(int i=0;i<N;i++){
            fout<<"Case #"<<i+1<<":\n";
            fin>>H>>W;
            int **arr=new int*[H];
            for(int j=0;j<H;j++)
                    arr[j]=new int[W];
            char **arr2 = new char*[H];
            for(int j=0;j<H;j++)
                    arr2[j]=new char[W];
            pair<int,int>**arr3 = new pair<int,int>*[H];
            for(int j=0;j<H;j++)
                    arr3[j] = new pair<int,int>[W];
            for(int a=0;a<H;a++){
                    for(int b=0;b<W;b++){
                            fin>>arr[a][b];
                            arr2[a][b]=0;
                    }
            }
            
            int tx,ty;
            char ch = 'a';
            for(int a=0;a<H;a++){
                    for(int b=0;b<W;b++){
                      tx=a;
                      ty=b;
                      if(a>0){
                              if(arr[a-1][b]<arr[tx][ty]){
                                                         tx = a-1;
                                                         ty = b;                            
                              }
                      }
                      if(b>0){
                              if(arr[a][b-1]<arr[tx][ty]){
                                                          tx = a;
                                                          ty = b-1;
                              }        
                      }
                      if(b<W-1){
                                if(arr[a][b+1]<arr[tx][ty]){
                                                           tx = a;
                                                           ty = b+1;
                                }
                      }
                      if(a<H-1){
                                if(arr[a+1][b]<arr[tx][ty]){
                                                            tx = a+1;
                                                            ty = b;
                                }
                      }
                      arr3[a][b]=pair<int,int>(tx,ty);
                    }
            }
            for(int a=0;a<H;a++){
                    for(int b=0;b<W;b++){
                            tx = a; ty =b;
                            while(arr3[tx][ty]!=pair<int,int>(tx,ty)){
                                                                      tx = arr3[tx][ty].first;
                                                                      ty = arr3[tx][ty].second;
                            }
                            if(arr2[tx][ty]==0){
                                               arr2[tx][ty]=ch;
                                               ch++;
                            }
                            fout<<arr2[tx][ty]<<" ";
                    }
                    fout<<endl;
            }
    }
	return 0;
}

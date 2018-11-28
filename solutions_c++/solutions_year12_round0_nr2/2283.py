#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int arr[128];
int N,S,p;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    for(int tt=1;tt<=cases;tt++){
        scanf("%d%d%d",&N,&S,&p);
        for(int i=0;i<N;i++){
            scanf("%d",&arr[i]);
        }
        int counter=0;
        for(int i=0;i<N;i++){
            if(arr[i]==0){
                counter += (p==0);
            }
            else if(arr[i]==1){
                counter += (p<=1);
            }
            /*else if(arr[i]==2){
                if(p==1){
                    counter++;
                }
                else if(p==2 && S){
                    counter++;
                    S--;
                }
            }*/
            else if(arr[i]>=28){
                counter++;
            }
            else{
                if(arr[i]%3==0){
                    if(p<=arr[i]/3) counter++;
                    else if( (p==arr[i]/3+1) && S){
                        counter++;
                        S--;
                    }
                }
                else if(arr[i]%3==1){
                    if(p<=arr[i]/3+1) counter++;
                }
                else{
                    if(p<=arr[i]/3+1) counter++;
                    else if((p==arr[i]/3+2) && S){
                        counter++;
                        S--;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",tt,counter);
    }
    return 0;
}

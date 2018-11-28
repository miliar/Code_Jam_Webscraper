#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int t, cse=0;
    int a1,a2;

    int tatime;
    int na,nb;
    int th,tm;

    scanf("%d",&t);
    while(t--){
        a1=0,a2=0;
        cse++;

        vector<int> dep_a;
        vector<int> dep_b;
        vector<int> arr_a;
        vector<int> arr_b;

        scanf("%d",&tatime);
        scanf("%d%d",&na,&nb);

        for(int i=0;i<na;i++){
            scanf("%d:%d",&th,&tm);
            dep_a.push_back((th*60+tm)%1440);

            scanf("%d:%d",&th,&tm);
            arr_b.push_back((th*60+tm+tatime)%1440);
        }

        for(int i=0;i<nb;i++){
            scanf("%d:%d",&th,&tm);
            dep_b.push_back((th*60+tm)%1440);

            scanf("%d:%d",&th,&tm);
            arr_a.push_back((th*60+tm+tatime)%1440);
        }

        sort(dep_a.begin(),dep_a.end());
        sort(dep_b.begin(),dep_b.end());
        sort(arr_a.begin(),arr_a.end());
        sort(arr_b.begin(),arr_b.end());

        for(int i=0,j=0;i<dep_a.size() && j<arr_a.size();i++){
            if(dep_a[i] >= arr_a[j]) a1++ , j++;
        }

        for(int i=0,j=0;i<dep_b.size() && j<arr_b.size();i++){
            if(dep_b[i] >= arr_b[j]) a2++ , j++;
        }

        printf("Case #%d: %d %d\n",cse, dep_a.size()-a1, dep_b.size()-a2);
    }
    return 0;
}

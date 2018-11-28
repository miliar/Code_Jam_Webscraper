#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

bool used[105]; //pake normal aja udah >= p
int arr[105];
int res;
void isGood(int i, int p){
    if(arr[i] % 3 == 2){
        if((arr[i]+1)/3 >= p){
            used[i] = true;
            res++;
        }
    } else if(arr[i] % 3 == 1){
        if((arr[i]-1)/3 + 1 >= p){
            used[i] = true;
            res++;
        }
    } else {
        if(arr[i]/3 >= p){
            used[i] = true;
            res++;
        }
    }
}
bool isSupAble(int n, int p){ //is the total score n can be made to be suprising, such that the max score is at least p?
    if(n % 3 == 2){
        if((n+1)/3 + 1 >= p)
            return true;
        return false;
    } else if(n % 3 == 1){
        if((n-1)/3 + 1 >= p)
            return true;
        return false;
    } else {
        if(n/3 + 1 >= p && n != 0)
            return true;
        return false;
    }
}

main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    int n,s,p;
    int supAble;
    cin>>tc;
    for(int i = 1; i <= tc; i++){
        for(int j = 0; j < 105; j++){
            used[j] = false;
        }
        res = supAble = 0;
        cin>>n>>s>>p;
        for(int j = 0; j < n; j++){
            cin>>arr[j];
        }

        for(int j = 0; j < n; j++){
            isGood(j, p);
        }
        for(int j = 0; j < n; j++){
            if(!used[j]){
                if(isSupAble(arr[j],p))
                    supAble++;
            }
        }
//        cout<<"# "<<res<<" "<<supAble<<endl;
        res += min(supAble, s);
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}

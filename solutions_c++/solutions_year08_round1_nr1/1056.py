#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

#include <set>
#include <map>

#include <queue>
#include <deque>
#include <stack>
#include <list>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#define all(c) (c).begin(), (c).end()
using namespace std;
int main(){
    freopen("A1.in", "r", stdin);
    freopen("A1.out", "w", stdout);
    
    int n;
    scanf ("%d\n", &n);
    for(int i=0; i<n; i++){
        int a,aa;
        scanf("%d\n", &a);
        vector<int> v1,v2;    
        string linea;
        getline(cin,linea,'\n');
        stringstream is(linea);
        while(is>>aa){v1.push_back(aa);}

        getline(cin,linea,'\n');
        stringstream is2(linea);
        while(is2>>aa){v2.push_back(aa);}
        sort(all(v1));
        long long minn=200000000,sum=0,cont=0; //cout<<minn<<endl;
        do{
            //cont++;
            sum=0;
            for(int j=0; j<v1.size();j++){
                sum+=v1[j]*v2[j];
            }    
            if(sum<minn)minn=sum;
        }while(next_permutation(all(v1)));
        int cas=i+1;
        cout<<"Case #"<<cas<<": "<<minn;
        if(i!=n-1)cout<<endl;
        //cout<<cont;
    }
return 0;
}

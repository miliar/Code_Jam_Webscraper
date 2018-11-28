#include<iostream>
#include<map>
#include<algorithm>
#include<string>
#include<cstdio>
using namespace std;
int main(){

    int ok[31][3] = { {0,0,0},{0,0,1},{0,1,1},{1,1,1},{1,1,2},
                      {1,2,2},{2,2,2},{2,2,3},{2,3,3},{3,3,3},
                      {3,3,4},{3,4,4},{4,4,4},{4,4,5},{4,5,5},
                      {5,5,5},{5,5,6},{5,6,6},{6,6,6},{6,6,7},
                      {6,7,7},{7,7,7},{7,7,8},{7,8,8},{8,8,8},
                      {8,8,9},{8,9,9},{9,9,9},{9,9,10},{9,10,10},{10,10,10}};

    int not_ok[31][3] = { {0,0,0},{0,0,1},{0,0,2},{0,1,2},{0,2,2},
                      {1,1,3},{1,2,3},{1,3,3},{2,2,4},{2,3,4},
                      {2,4,4},{3,3,5},{3,4,5},{4,4,5},{4,4,6},
                      {4,5,6},{5,5,6},{5,5,7},{5,6,7},{6,6,7},
                      {6,6,8},{6,7,8},{6,8,8},{7,8,8},{7,8,9},
                      {7,9,9},{8,9,9},{8,9,10},{8,10,10},{9,10,10},{9,10,11}};

    int mask[31]={1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0};

    int T, case_no = 1;

    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> T;

    while(T--){

        int N,m,p,i,j,a[101],c=0,masked=0,remove=0,c1=0;
        cin >> N >> m >> p;
        cout << "Case #"<<case_no<<": ";
        case_no++;
        int arr_ok[101]={0}, arr_not_ok[101] = {0};
        for(i=0;i<N;i++)
            cin >> a[i];

        for(i=0;i<N;i++){
            if(mask[a[i]]) masked++;
            for(j=0;j<3;j++){
                if(ok[a[i]][j] >= p){
                    arr_ok[i] = 1;
                }
                if(not_ok[a[i]][j] >= p){
                    arr_not_ok[i] = 1;
                }
            }
        }
        for(i=0;i<N;i++){
            if(arr_ok[i]==1){
                c++;
            }
        }
        if((N-c) == m){
            for(i=0;i<N;i++){
                if(arr_not_ok[i]==1 && arr_ok[i]==0){
                    c++;
                }
            }
            cout << c << endl;
        }
        else if((N-c) > m){
            for(i=0;i<N;i++){
                if(arr_not_ok[i]==1 && arr_ok[i]==0){
                    c1++;
                }
            }
            c1 = min(m,c1);
            cout << c + c1 << endl;
        }
        else if((N-c) < m){
            int x=0,c2=0;
            for(i=0;i<N;i++){
                if(arr_not_ok[i]==0) x++;
                if(arr_not_ok[i]==1 && arr_ok[i]==0){
                    c1++;
                }
            }
            for(i=0;i<N;i++){
                if(arr_not_ok[i]==1 && arr_ok[i]==1){
                    c2++;
                }
            }
            m = m - (N-c);
            if(c2 >= m){
                cout << c + c1 << endl;
            }
            else{
                c2 = m - c2;
                cout << c + c1 - c2 <<endl;
            }
        }
    }
    return 0;
}




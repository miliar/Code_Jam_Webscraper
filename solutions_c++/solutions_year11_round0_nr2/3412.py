#include <iostream>
#include <vector>
using namespace std;
int main(){
    freopen("gcj2.txt","r",stdin);
    freopen("gcj2.out","w",stdout);
    int N,c,d,n,cur;
    char e,c1,c2,c3,d1,d2;
    int a[26][26];
    int b[26][26];
    cin >> N;
    for(int I = 1;I <= N;++I){
        memset(a,0,sizeof(a));
        memset(b,-1,sizeof(b));
        cin >> c;
        for(int i = 0;i < c;++i){
            cin >> c1 >> c2 >> c3;
//            cout << c1 << c2 << c3 << endl;
            b[c1-'A'][c2-'A'] = b[c2-'A'][c1-'A'] = c3 - 'A';
        }
        cin >> d;
        for(int i = 0;i < d;++i){
            cin >> d1 >> d2;
//            cout << d1 << d2 << endl;
            a[d1-'A'][d2-'A'] = a[d2-'A'][d1-'A'] = 1;
        }
        /*
        for(int i = 0;i < 26;++i){
            for(int j = 0;j < 26;++j)
                cout << b[i][j];
            cout << endl;
        }
        */
        vector<int> V;
        int tmp;
        cin >> n;
        for(int i = 0;i < n;++i){
            cin >> e;
//            cout << e;
            cur = e - 'A';
            V.push_back(cur);
            if(V.size() > 1){
//                cout << V[V.size()-2] << V[V.size()-1] << endl;
                if((tmp = b[V[V.size()-2]][V[V.size()-1]]) != -1){
//                    cout << "!" << tmp;
                    V.pop_back();
                    V.pop_back();
                    V.push_back(tmp);
                }
                else{
                    for(int j = V.size()-2;j >= 0;--j){
                        if(a[V[j]][V[V.size()-1]]){
                            V.clear();
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: [",I);
        for(int i = 0;i < (int)V.size()-1;++i){
            printf("%c, ",V[i]+'A');
        }
        if(V.size() > 0){
            printf("%c",V[V.size()-1]+'A');
        }
        printf("]\n");
    }
}

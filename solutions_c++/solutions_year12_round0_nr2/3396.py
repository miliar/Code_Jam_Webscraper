#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

int t,n,s,p,c;

int main(){
    freopen("in2.in","r",stdin);
    freopen("out3.txt","w",stdout);

    cin >> t;

     for(int ti=0;ti<t;ti++){
        cin >> n >> s >> p;
        int m = 0;
        for(int i=0;i<n;i++)
        {
            cin >> c;
            switch(c % 3){
                case 0:
                    //cout << c << " " << c/3 << endl;
                    if(c/3 >= p)m++;
                    else if(c/3+1 >= p && s > 0 && c > 0){m++;s--;}
                    break;
                case 1:
                    //cout << c << " " << (c-1)/3+1 << endl;
                    if((c-1)/3+1 >= p)m++;
                    break;
                case 2:
                    //cout << c << " " << (c-2)/3+1 << endl;
                    if((c-2)/3+1 >= p)m++;
                    else if((c-2)/3+2 >= p && s > 0 && c > 1){m++;s--;}
                    break;
            }
        }
        cout << "Case #" << (ti+1) << ": " << m << endl;
     }

}

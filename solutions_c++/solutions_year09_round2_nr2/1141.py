#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>
#include <map>
#include <cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        string num,tmp;

        long long int m,n;

        cin>>num;
        istringstream iss(num);
         iss>>m;
        tmp=num;
        if(next_permutation(num.begin(),num.end())){
            cout<<"Case #"<<i<<": "<<num<<endl;
        }
        else{
            reverse(tmp.begin(),tmp.end());
            int j=0;
            for(;tmp[j]=='0';j++);

            //Debug
            //cout<<"else"<<endl;
            cout<<"Case #"<<i<<": "<<tmp[j]<<'0';
            int k=j+1;
            while(j>0){
                cout<<'0';
                j--;
            }
            while(k<tmp.size()){
                cout<<tmp[k];
                k++;
            }
            cout<<endl;
        }
            /*
        istringstream iss2(num);
        iss2>>n;


        if(n<=m ){
            reverse(tmp.begin(),tmp.end());
            if(tmp[0]!='0'){
            cout<<"Case #"<<i<<": "<<tmp[0]<<"0";
            for(int j=1;j<tmp.size();j++)
                cout<<tmp[j];
            cout<<endl;
            }
            else{

                int j=0;
                while(tmp[j]!='0')
                    j++;
                cout<<"Case #"<<i<<": "<<tmp[j];

                int k=j+1;
                while(j>0){
                    cout<<'0';
                    j--;
                }
                for( ;k<tmp.size();k++)
                    cout<<tmp[k++];
            }
        }*/

    }
    return 0;
}

#include <stack>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
int abs(int a)
{
    if(a<0) return 0-a;
    return a;
}
int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A_ret.txt");
    int ncase;
    cin>>ncase;
    for(int kcase=1;kcase<=ncase;kcase++){
        cout<<"Case #"<<kcase<<": ";
        int n,v;
        cin>>n;
        char ch;
        int a,b;
        a=b=0;
        int curr_o=1;
        int curr_B=1;
        int t_o=0;
        int t_b=0;
        int sum=0;
        for(int i=0;i<n;i++){
            cin>>ch>>v;
            if(ch=='O'){
                if(v<=curr_o+t_o&&v>=max(1,curr_o-t_o)){
                    sum+=1;
                    t_o=0;
                    curr_o=v;
                    t_b+=1;
                }else{
					if(v>curr_o){
						sum+=(v-curr_o-t_o+1);
						t_b+=(v-curr_o-t_o+1);
					}else{
						sum+=(curr_o-v-t_o+1);
						t_b+=(curr_o-v-t_o+1);
					}

					 curr_o=v;
					 t_o=0;
                }
            }
            if(ch=='B'){
                if(v<curr_B+t_b&&v>=max(1,curr_B-t_b)){
                    sum+=1;
                    t_b=0;
                    curr_B=v;
                    t_o+=1;
                }else{
					if(v>curr_B){
						sum+=(v-curr_B-t_b)+1;
						t_o=(v-curr_B-t_b)+1;
					}
					else{
						sum+=(curr_B-v-t_b)+1;
						t_o+=(curr_B-v-t_b)+1;
					}
                    t_b=0;
					curr_B=v;
                }
            }
        }
        cout<<sum<<endl;
        //cout<<(a>b?a:b)<<endl;
    }
}

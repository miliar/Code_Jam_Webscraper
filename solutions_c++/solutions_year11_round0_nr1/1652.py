#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        unsigned int steps=0;
        int b=1,o=1,step_b=0,step_o=0;
        char ch,last='B';
        int num,current;
        int n;
        cin>>n;
        cin>>ch>>num;
        switch(ch){
            case 'B':
                step_o=0;
                current=abs(num-b)+1;
                step_b+=current;
                b=num;
                steps+=current;
                last=ch;
                break;
            case 'O':
                step_b=0;
                current=abs(num-o)+1;
                step_o+=current;
                o=num;
                steps+=current;
                last=ch;
                break;
        }
        for(int i=1;i<n;i++){
            cin>>ch>>num;
            if(last==ch){
                switch(ch){
                    case 'B':
                        step_o=0;
                        current=abs(num-b)+1;
                        step_b+=current;
                        b=num;
                        steps+=current;
                        last=ch;
                        break;
                    case 'O':
                        step_b=0;
                        current=abs(num-o)+1;
                        step_o+=current;
                        o=num;
                        steps+=current;
                        last=ch;
                        break;
                }
            }else{
                switch(ch){
                    case 'B':
                        current=abs(num-b)-step_o;
                        if(current<0) current=0;
                        current+=1;
                        step_o=0;
                        step_b+=current;
                        b=num;
                        steps+=current;
                        last=ch;
                        break;
                    case 'O':
                        current=abs(num-o)-step_b;
                        if(current<0) current=0;
                        current+=1;
                        step_b=0;
                        step_o+=current;
                        o=num;
                        steps+=current;
                        last=ch;
                        break;
                }
            }
        }
        cout<<"Case #"<<z<<": "<<steps<<endl;
    }
    return 0;
}

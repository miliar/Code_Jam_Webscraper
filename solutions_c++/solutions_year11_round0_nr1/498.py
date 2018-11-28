#include <iostream>

using namespace std;
int test;
int n;
int a,b;
int lef[300],rig[300];
int robN[300];
int robP[300];
int answer;

void readinput(){
    scanf("%i",&n);
    a=0;
    b=0;
    int num;
    char c;
    for (int i=0;i<n;i++){
        while (true){
            scanf("%c",&c);
            //cout<<"!!"<<c;
            if (c=='O' || c=='B') break;    
        }    
        scanf("%i",&num);    
        if (c=='O'){
            lef[a]=num;
            a++;    
            robN[i]=0;
            robP[i]=num;
        }else
        if (c=='B'){
            rig[b]=num;
            b++;    
            robN[i]=1;
            robP[i]=num;
        }//else
        //printf("!!!");        
        //cout<<c<<" "<<num<<endl;
    }
    scanf("\n");            
}

void solve(){
    int posl=1;
    int posr=1;
    int indl = 0;    
    int indr = 0;
    int tim = 0;
    for (int i=0;i<n;i++){
        while (true){
            //cout<<posl<<" "<<posr<<endl;
            tim++;
            bool flag = 0;
            if (robN[i]==0){
                if (posl==lef[indl]){
                    flag = 1;    
                    indl++;    
                }else{
                    if (posl<lef[indl]){
                        posl++;
                    }else
                        posl--;
                }
                if (indr<b && posr<rig[indr]){
                    posr++;    
                }     
                if (indr<b && posr>rig[indr]){
                    posr--;    
                }   
            }else{
                if (posr==rig[indr]){
                    flag = 1;
                    indr++;        
                }else{
                    if (posr<rig[indr]){
                        posr++;
                    }else
                        posr--;
                }
                if (indl<a && posl<lef[indl]){
                    posl++;    
                }
                if (indl<a && posl>lef[indl]){
                    posl--;    
                }
            }
            if (flag){
                break;    
            }    
        }        
    }
    answer=tim;    
}

void writeoutput(int t){
    printf("Case #%i: %i\n",t+1,answer);        
}

int main(void){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
